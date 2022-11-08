#include <Arduino.h>
#include <Stepper.h>
#include <Servo.h>

int RED_LED_PIN = 5;
//int GRN_LED_PIN = 10;
int BLU_LED_PIN = 6;

int LDR = A0;
int LDRval1;

int THR_PIN = A2; 

Servo jawServo; //Jaw Servo
int pos = 0;

Servo tailServo; // Tail Servo
int pos1 = 90;

 
void set_RGB_color(int Rval, int Gval, int Bval){ //Eyes
  analogWrite(RED_LED_PIN, Rval);
  //analogWrite(GRN_LED_PIN, Gval);
  analogWrite(BLU_LED_PIN, Bval);
}
 
#define TOTAL_LIGHT_PREVS (10)
double prevLight [TOTAL_LIGHT_PREVS];
int lightIndex = 0;
double getLight(){
  prevLight[lightIndex] = analogRead(LDR);
  double avLight = 0;
  for ( int i=0; i<TOTAL_LIGHT_PREVS; i++ ){ avLight += prevLight[i]; }
  lightIndex = (lightIndex+1)%TOTAL_LIGHT_PREVS;
  return (avLight/TOTAL_LIGHT_PREVS) ;
} 

 
#define TOTAL_TEMP_PREVS (10)
double prevTemps [TOTAL_TEMP_PREVS];
int tempIndex = 0;
double getTemp(){
  prevTemps[tempIndex] = analogRead(THR_PIN);
  double avTemp = 0;
  for ( int i=0; i<TOTAL_TEMP_PREVS; i++ ){ avTemp += prevTemps[i]; }
  tempIndex = (tempIndex+1)%TOTAL_TEMP_PREVS;
  return avTemp/TOTAL_TEMP_PREVS ;
} 


int US_OUP_PIN = 3 ; // ~ -> TRIG OUTPUT
int US_INP_PIN = 2 ; // . -> ECHO INPUT
int DEFULT_MAX_DISTANCE = 50;

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
#define TOTAL_DIST_PREVS (20)
double prevDistances [TOTAL_DIST_PREVS];
int distIndex = 0;
double getDistance(){
  prevDistances[distIndex] = getDistanceRAW();
  double avDistance = 0;
  for ( int i=0; i<TOTAL_DIST_PREVS; i++ ){ avDistance += prevDistances[i]; }
  distIndex = (distIndex+1)%TOTAL_DIST_PREVS;

  Serial.println( (avDistance/TOTAL_DIST_PREVS) );

  return round( (avDistance/TOTAL_DIST_PREVS)*10.0 )/10.0;
} 


int ROAR_PIN = 12; // ~ -> Buzzer OUTPUT
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

const int STEPS_PER_R = 300;
int ST_INP1_PIN = 8 ; // . -> STEPPER_INP1
int ST_INP2_PIN = 9 ; // . -> STEPPER_INP2
int ST_INP3_PIN = 10; // . -> STEPPER_INP3
int ST_INP4_PIN = 11; // . -> STEPPER_INP4
int MOTOR_RPM = 20;
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
  jawServo.write( open?0:60 );
}

void randomiseTailState( ){
  jawServo.write( rand()%60 );
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
            setJawState( true );
            break; 

          default:
            setJawState( false );
            break;
        }
      }

      // Tail response
      if ( tickedInterval( 2000000 ) && currentState==CALM ){
        randomiseTailState();
      }

      // Eye response
      if ( tickedInterval( 500000 ) ){
        switch ( currentState ){
          case FEAR:
            set_RGB_color( 255, 255, 0 );
            break;

          case CURIOSITY:
            set_RGB_color( 0, 0, 255 );
            break;
          
          case CALM:
            set_RGB_color( 0, 255, 0 );
            break;
          
          case IDLE:
            set_RGB_color( 200, 100, 100 );
            break;
          
          case BITING:
            set_RGB_color( 255, 0, 0 );
            break;
        }
      }

      prevMicroExecute = micros();
    }

    void updateState(){
      if ( getTemp() < 100 && false ){
        setState( CALM );
      }else if ( getLight() < 100 && false ){
        setState( BITING );
      }else if ( getDistance() < 10 ){
        setState( FEAR );
      }else if ( getDistance() > 13 ){
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

  jawServo.attach(A1);
  tailServo.attach(A3);
}


ResponseManager rManager;

void loop() {  

  rManager.executeResponses();
  rManager.updateState();
}

