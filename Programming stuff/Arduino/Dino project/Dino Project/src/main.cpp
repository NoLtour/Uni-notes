#include <Arduino.h>
#include <Stepper.h>
#include <Servo.h>

int RED_LED_PIN = 5;
//int GRN_LED_PIN = 10;
int BLU_LED_PIN = 6;

int ST_INP1_PIN = 8 ; // . -> STEPPER_INP1
int ST_INP2_PIN = 9 ; // . -> STEPPER_INP2
int ST_INP3_PIN = 10; // . -> STEPPER_INP3
int ST_INP4_PIN = 11; // . -> STEPPER_INP4

// RPM 16, SPR, 320

const int STEPS_PER_R = 320;
int MOTOR_RPM = 16;

Stepper stepperMotor = Stepper( STEPS_PER_R, ST_INP1_PIN, ST_INP2_PIN, ST_INP3_PIN, ST_INP4_PIN );


int US_OUP_PIN = 4 ; // ~ -> TRIG OUTPUT
int US_INP_PIN = 3 ; // . -> ECHO INPUT

int ROAR_PIN = 12; // ~ -> Buzzer OUTPUT

int TH_NOSE_PIN = A0;
int LDRval1;

int TH_MOTH_PIN = A2; 
int VINP_PIN    = A3; 

Servo jawServo; //Jaw Servo
int pos = 0;

Servo tailServo; // Tail Servo
int pos1 = 90;

// this sets the colour of the eye LED
void set_RGB_color(int Rval, int Gval, int Bval){ //Eyes
  analogWrite(RED_LED_PIN, Rval);
  //analogWrite(GRN_LED_PIN, Gval);
  analogWrite(BLU_LED_PIN, Bval);
}
  
#define TOTAL_LIGHT_PREVS (80)
double prevLight [TOTAL_LIGHT_PREVS];
int lightIndex = 0; 
// This averages out the light input
double getLight(){
  prevLight[lightIndex] = ((analogRead(VINP_PIN)/analogRead(TH_NOSE_PIN)) - 1) * 1000;
  double avLight = 0;
  for ( int i=0; i<TOTAL_LIGHT_PREVS; i++ ){ avLight += prevLight[i]; }
  lightIndex = (lightIndex+1)%TOTAL_LIGHT_PREVS;
  
  return (avLight/TOTAL_LIGHT_PREVS) ;
} 

 
#define TOTAL_TEMP_PREVS (80)
double prevTemps [TOTAL_TEMP_PREVS];
int tempIndex = 0;
double prevTempV = 0;
 
// gets the nose resistor value and averages it
double getTemp(){
  prevTemps[tempIndex] = ((analogRead(VINP_PIN)/analogRead(TH_MOTH_PIN)) - 1) * 1000;
  double avTemp = 0;
  for ( int i=0; i<TOTAL_TEMP_PREVS; i++ ){ avTemp += prevTemps[i]; }
  tempIndex = (tempIndex+1)%TOTAL_TEMP_PREVS;

  prevTempV = ((prevTempV*300)+prevTemps[tempIndex])/301;
  //Serial.print(prevTempV);
  //Serial.print("     ");
  //Serial.println(avTemp/TOTAL_TEMP_PREVS);
  return avTemp/TOTAL_TEMP_PREVS;
} 


int DEFULT_MAX_DISTANCE = 40;

// raw read on distance
double getDistanceRAW( int maxMicros=(DEFULT_MAX_DISTANCE/0.008) ){
  digitalWrite( US_OUP_PIN, LOW );
  delayMicroseconds(2);
  digitalWrite( US_OUP_PIN, HIGH );
  delayMicroseconds(10);
  digitalWrite( US_OUP_PIN, LOW );
  
  int travelTime = pulseIn( US_INP_PIN, HIGH, maxMicros );
  delayMicroseconds(10);

  return (travelTime==0?DEFULT_MAX_DISTANCE:(travelTime*0.016));
}
#define TOTAL_DIST_PREVS (25)
double prevDistances [TOTAL_DIST_PREVS];
int distIndex = 0;
// averager of distance reading to clean up noise
double getDistance(){
  prevDistances[distIndex] = getDistanceRAW();
  double avDistance = 0;
  for ( int i=0; i<TOTAL_DIST_PREVS; i++ ){ avDistance += prevDistances[i]; }
  distIndex = (distIndex+1)%TOTAL_DIST_PREVS; 

  return round( (avDistance/TOTAL_DIST_PREVS)*10.0 )/10.0;
} 


unsigned long sRoarTime = 0;
int roarState = -1; 

// starts roar, if one is in progress it will do nothing
void startRoar(){
  if ( roarState == -1 ){
    sRoarTime = millis(); 
    roarState = 0;
  }
}
// run as frequently as possible to control raw pitch
void updateRoar(){
  if ( roarState != -1 ){
    int r = millis() - sRoarTime;

    int cFreq = ( 20 + (r/40.0) + (pow((1+sin(r/15.0) ), 2.0)*40.0)  ) * (  1 - 1.0/( 2.6 - ( r/1800.0 ) )  );

    tone( ROAR_PIN, cFreq, 100 );
    if ( r > 3000 ){
      roarState = -1;
      noTone( ROAR_PIN );
    }
  }
}

// sets stepper rotation
void rotateStepper( int direction ){ 
  if ( direction == 0 ){
    return;
  }else{ 
    stepperMotor.step( (direction<0)?10:-10 ); 
  }
}

// updates the position of the jaw depending on if it's moving or held
void setJawState( bool moving ){
  if ( !moving ){
    jawServo.write( millis()%2000<1000?0:60 );
  }else{
    jawServo.write( 60 );
  }
  
}

// moves tail randomly
void randomiseTailState( ){
  tailServo.write( rand()%40 );
}

enum ResponseState{ FEAR, CURIOSITY, CALM, BITING, IDLE };


// calibration management system
class Calibration{
  public:
  double minReading;
  double maxReading;

  unsigned long startCalTime;
  unsigned long endCalTime;

  Calibration( int nST, int edT ){
    startCalTime = nST;
    endCalTime = edT;
  }

  // takes an input, if in calibration period it will take that as a potential new max/min
  void takeCalInput( double inp ){
    if ( millis() < endCalTime && millis() > startCalTime ){
      if ( inp > maxReading ){
        maxReading = inp;

      }else if( inp < minReading ){
        minReading = inp;
      }
    }
  }

  // checks if the input is below or above the halfway mark between max and min
  boolean lessThanHalf( double inp ){
    return ( inp < (minReading+maxReading)/2 );
  }
};

Calibration calibrationNose  = Calibration( 5000, 30000 );
Calibration calibrationMouth = Calibration( 5000, 30000 );

// Manages response
class ResponseManager{
  private:
    unsigned long prevMicroExecute = 0;

    void setState( ResponseState newState ){
      currentState = newState;
    }
  
  public:
    ResponseState currentState;

    bool tickedInterval( unsigned long microsLoopPeriod ){
      return (prevMicroExecute/microsLoopPeriod) != (micros()/microsLoopPeriod);
    }

    // activates the responses based on current emotional state
    void executeResponses(){

      // Buzzer response
      if ( currentState == FEAR ){
        startRoar();
      }
      updateRoar();

      // Movement response
      if ( tickedInterval( 100000 ) ){
        switch ( currentState ){
          case FEAR:
            rotateStepper( -1 );
            break;

          case CURIOSITY:
            rotateStepper( 1 );
            break;
          
          default:
            rotateStepper( 0 );
            break;
        }
      }

      // Jaw response
      if ( tickedInterval( 100000 ) ){
        switch ( currentState ){
          case BITING:
            setJawState( false );
            break; 

          default:
            setJawState( true );
            break;
        }
      }

      // Tail response
      if ( tickedInterval( 2000000 ) && currentState!=CALM ){
        randomiseTailState();
      }

      // Eye response
      if ( tickedInterval( 500000 ) ){
        switch ( currentState ){
          case FEAR:
            set_RGB_color( 10, 0, 0 );
            break;

          case CURIOSITY:
            set_RGB_color( 0, 0, 255 );
            break;
          
          case CALM:
            set_RGB_color( 0, 0, 20 );
            break;
          
          case IDLE:
            set_RGB_color( 200, 0, 100 );
            break;
          
          case BITING:
            set_RGB_color( 255, 0, 0 );
            break;
        }
      }

      prevMicroExecute = micros();
    }

    // reads input to change state if appropriate
    void updateState(){
      double noseV = getTemp();
      double mouthV = getLight();
      double distV = getDistance();

      calibrationMouth.takeCalInput( mouthV );
      calibrationNose.takeCalInput( noseV );

      Serial.print("T: ");
      Serial.print(noseV);
      Serial.print("\tM: ");
      Serial.print(mouthV);
      Serial.print("\tD: ");
      Serial.println(distV);

      if ( !calibrationNose.lessThanHalf( noseV ) ){
        setState( CALM );
      }else if ( !calibrationNose.lessThanHalf( mouthV ) ){
        setState( BITING );
      }else if ( distV < 13 ){
        setState( FEAR );
      }else if ( distV > 16 && distV < DEFULT_MAX_DISTANCE ){
        setState( CURIOSITY );
      }else{
        setState( IDLE );
      }
    }
};

ResponseManager rManager;



void setup() {
  pinMode(LED_BUILTIN, OUTPUT); 

  stepperMotor.setSpeed( MOTOR_RPM );

  Serial.begin(9600);
 

  pinMode(RED_LED_PIN,OUTPUT);
  //pinMode(GRN_LED_PIN,OUTPUT);
  pinMode(BLU_LED_PIN,OUTPUT);

  pinMode( US_INP_PIN, INPUT );
  pinMode( US_OUP_PIN, OUTPUT );

  jawServo.attach(A4);
  tailServo.attach(A5); 
}



void loop() {    

  digitalWrite(13, millis()%20000<10000?HIGH:LOW );

  rManager.executeResponses();
  rManager.updateState(); 
}

