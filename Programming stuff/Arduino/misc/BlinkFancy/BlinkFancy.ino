/*
  Blink

  Turns an LED on for one second, then off for one second, repeatedly.

  Most Arduinos have an on-board LED you can control. On the UNO, MEGA and ZERO
  it is attached to digital pin 13, on MKR1000 on pin 6. LED_BUILTIN is set to
  the correct LED pin independent of which board is used.
  If you want to know what pin the on-board LED is connected to on your Arduino
  model, check the Technical Specs of your board at:
  https://www.arduino.cc/en/Main/Products

  modified 8 May 2014
  by Scott Fitzgerald
  modified 2 Sep 2016
  by Arturo Guadalupi
  modified 8 Sep 2016
  by Colby Newman

  This example code is in the public domain.

  https://www.arduino.cc/en/Tutorial/BuiltInExamples/Blink
*/

#define PULSE_PERIOD 16

void light( float fraction, int totalTime ){
  fraction = fraction<0?0:( fraction > 1?1:fraction );

  int onTime = (int) (PULSE_PERIOD*fraction);
  int offTime = PULSE_PERIOD - onTime;
  
  for ( ;totalTime>0; totalTime -= PULSE_PERIOD ){
    digitalWrite(LED_BUILTIN, HIGH);   
    delay(onTime);                       
    digitalWrite(LED_BUILTIN, LOW);    
    delay(offTime); 
  }
}

void smoothLight( float stBright, float enBright, int transTime ){
  stBright = stBright<0?0:( stBright > 1?1:stBright );
  enBright = enBright<0?0:( enBright > 1?1:enBright );

  float onTime = (PULSE_PERIOD*stBright);
  float transRate = PULSE_PERIOD*PULSE_PERIOD*(enBright-stBright)/( (float) transTime);

  for ( int timePassed=0; timePassed<=transTime; timePassed +=PULSE_PERIOD ){
    digitalWrite(LED_BUILTIN, HIGH);   
    delay( (int) onTime );                       
    digitalWrite(LED_BUILTIN, LOW);    
    delay( PULSE_PERIOD - ( (int) onTime )  ); 

    onTime += transRate;
  }
}

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);
}

void randLight(){
  smoothLight( ( (float) (rand()%100) )/100, ( (float) (rand()%100) )/100, rand()%3000 );
}

// the loop function runs over and over again forever
void loop() {
  //randLight();
  smoothLight( 1, 0, 500 );

  smoothLight( 0, 1, 1500 );
  
  //digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
  //delay(1000);                       // wait for a second
  //digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
  //delay(1000);                       // wait for a second
}
