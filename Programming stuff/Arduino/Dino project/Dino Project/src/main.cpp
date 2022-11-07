#include <Arduino.h>
#include <Stepper.h>


int US_OUP_PIN = 10; // ~ -> TRIG OUTPUT
int US_INP_PIN = 8 ; // . -> ECHO INPUT
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
#define TOTAL_DIST_PREVS (200)
double prevDistances [TOTAL_DIST_PREVS];
int distIndex = 0;
double getDistance(){
  prevDistances[distIndex] = getDistanceRAW();
  double avDistance = 0;
  for ( int i=0; i<TOTAL_DIST_PREVS; i++ ){ avDistance += prevDistances[i]; }
  distIndex = (distIndex+1)%TOTAL_DIST_PREVS;
  return round( (avDistance/TOTAL_DIST_PREVS)*10.0 )/10.0;
}




int ROAR_PIN = 5; // ~ -> Buzzer OUTPUT
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

    tone( ROAR_PIN, cFreq );
    if ( r > 3000 ){
      roarState = -1;
      noTone( ROAR_PIN );
    }
  }
}

const int STEPS_PER_R = 2048;
int ST_INP1_PIN = 8 ; // . -> STEPPER_INP1
int ST_INP2_PIN = 9 ; // . -> STEPPER_INP2
int ST_INP3_PIN = 10; // . -> STEPPER_INP3
int ST_INP4_PIN = 11; // . -> STEPPER_INP4
int MOTOR_RPM = 1;
Stepper stepperMotor = Stepper( STEPS_PER_R, ST_INP1_PIN, ST_INP2_PIN, ST_INP3_PIN, ST_INP4_PIN );

void rotateStepper( int direction ){
  stepperMotor.step( STEPS_PER_R * direction );
}


void setup() {
  pinMode(LED_BUILTIN, OUTPUT); 

  stepperMotor.setSpeed( MOTOR_RPM );

  Serial.begin(9600);
}

int state=0;

void loop() { 
  if ( millis() < 1000 && state == 0 ){
    rotateStepper( 1 );
    state = 1;
  }
  
  if ( millis() > 1000 && state == 1 ){
    //rotateStepper( -1 );
    state = 2;
  }
  
  if ( millis() > 3000 && state == 2 ){
    //rotateStepper( 0 );
    state = 3;
  }
  
  digitalWrite(LED_BUILTIN, millis()%5000<100?HIGH:LOW); 
 
}

