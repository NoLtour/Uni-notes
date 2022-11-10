#include <Arduino.h>
#include <Stepper.h>
#include <Servo.h>

int RED_LED_PIN = 10;
//int GRN_LED_PIN = 10;
int BLU_LED_PIN = 11;

int ST_INP1_PIN = 3 ; // . -> STEPPER_INP1
int ST_INP2_PIN = 4 ; // . -> STEPPER_INP2
int ST_INP3_PIN = 5; // . -> STEPPER_INP3
int ST_INP4_PIN = 6; // . -> STEPPER_INP4


int US_OUP_PIN = 9 ; // ~ -> TRIG OUTPUT
int US_INP_PIN = 8 ; // . -> ECHO INPUT

int ROAR_PIN = 12; // ~ -> Buzzer OUTPUT

int TH_NOSE_PIN = A0;
int LDRval1;

int TH_MOTH_PIN = A2; 
int VINP_PIN    = A3; 

Servo jawServo; //Jaw Servo
int pos = 0;

Servo tailServo; // Tail Servo
int pos1 = 90;

 
void set_RGB_color(int Rval, int Gval, int Bval){ //Eyes
  analogWrite(RED_LED_PIN, Rval);
  //analogWrite(GRN_LED_PIN, Gval);
  analogWrite(BLU_LED_PIN, Bval);
}
 
double prevLightV = 0;
#define TOTAL_LIGHT_PREVS (80)
double prevLight [TOTAL_LIGHT_PREVS];
int lightIndex = 0;
// 26 -> Touching, 127 -> NOT
double getLight(){
  prevLight[lightIndex] = ((analogRead(VINP_PIN)/analogRead(TH_NOSE_PIN)) - 1) * 1000;
  double avLight = 0;
  for ( int i=0; i<TOTAL_LIGHT_PREVS; i++ ){ avLight += prevLight[i]; }
  lightIndex = (lightIndex+1)%TOTAL_LIGHT_PREVS;
  prevLightV = ((prevLightV*300)+prevLight[lightIndex])/301;
  
  //Serial.print(prevLightV);
  //Serial.print("     ");
  //Serial.println(avLight/TOTAL_LIGHT_PREVS);
  return (avLight/TOTAL_LIGHT_PREVS) ;
} 

 
#define TOTAL_TEMP_PREVS (80)
double prevTemps [TOTAL_TEMP_PREVS];
int tempIndex = 0;
double prevTempV = 0;

// 100 -> Touching, 200 -> NOT
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
#define TOTAL_DIST_PREVS (40)
double prevDistances [TOTAL_DIST_PREVS];
int distIndex = 0;
double getDistance(){
  prevDistances[distIndex] = getDistanceRAW();
  double avDistance = 0;
  for ( int i=0; i<TOTAL_DIST_PREVS; i++ ){ avDistance += prevDistances[i]; }
  distIndex = (distIndex+1)%TOTAL_DIST_PREVS;

  //Serial.println( (avDistance/TOTAL_DIST_PREVS) );

  return round( (avDistance/TOTAL_DIST_PREVS)*10.0 )/10.0;
} 


unsigned long sRoarTime = 0;
int roarState = -1; 

void startRoar(){
  if ( roarState == -1 ){
    sRoarTime = millis(); 
    roarState = 0;
  }
}
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

const int STEPS_PER_R = 32;
int MOTOR_RPM = 200;
Stepper stepperMotor = Stepper( STEPS_PER_R, ST_INP1_PIN, ST_INP2_PIN, ST_INP3_PIN, ST_INP4_PIN );

void rotateStepper( int direction ){ 
  if ( direction == 0 ){
    return;
  }else{ 
    stepperMotor.step( (direction<0)?-20:20 );
    //stepperMotor.step( 20 );
  }
}

void setJawState( bool open ){
  if ( !open ){
    jawServo.write( millis()%2000<1000?0:60 );
  }else{
    jawServo.write( 60 );
  }
  
}

void randomiseTailState( ){
  tailServo.write( rand()%60 );
}

enum ResponseState{ FEAR, CURIOSITY, CALM, BITING, IDLE };

class DeviceOutput{

};

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
            set_RGB_color( 50, 0, 50 );
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

    void updateState(){
      double noseV = getTemp();
      double mouthV = getLight();
      double distV = getDistance();

      Serial.print("T: ");
      Serial.print(noseV);
      Serial.print("\tM: ");
      Serial.print(mouthV);
      Serial.print("\tD: ");
      Serial.println(distV);

      if ( noseV > 2100 ){
        setState( CALM );
      }else if ( mouthV > 2100 ){
        setState( BITING );
      }else if ( distV < 13.3 ){
        setState( FEAR );
      }else if ( distV > 15.3 && distV < DEFULT_MAX_DISTANCE ){
        setState( CURIOSITY );
      }else{
        setState( IDLE );
      }
    }
};



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


ResponseManager rManager;

void loop() {  

  if ( millis()%20000<10000 ){
    digitalWrite(13, HIGH );
    //stepperMotor.setSpeed(5);
  stepperMotor.step(30 );
  }else{
    
    digitalWrite(13, LOW ); 
  stepperMotor.step( -30 );
  }

  //digitalWrite(13, millis()%20000<10000?HIGH:LOW );

  //rManager.executeResponses();
  //rManager.updateState();
  //Serial.print( getLight() );
 // Serial.print("  -  ");
  //Serial.println( getTemp() );
}

