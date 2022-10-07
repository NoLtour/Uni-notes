

#define PULSE_PERIOD 14

void light( float fraction, int totalTime ){
  fraction = fraction<0?0:( fraction > 1?1:fraction );

  int onTime = (int) (PULSE_PERIOD*fraction);
  int offTime = PULSE_PERIOD - onTime;
  
  for ( ;totalTime>0; totalTime -= PULSE_PERIOD ){
    digitalWrite(LED_BUILTIN, HIGH);   
    digitalWrite(12, LOW);   
    delay(onTime);                       
    digitalWrite(LED_BUILTIN, LOW);  
    digitalWrite(12, HIGH);
    delay(offTime); 
  }
}

void smoothLight( float stBright, float enBright, int transTime ){
  stBright = stBright<0?0:( stBright > 1?1:stBright );
  enBright = enBright<0?0:( enBright > 1?1:enBright );
  
  float brightness = stBright;
  float transRate  = (enBright-stBright) * PULSE_PERIOD/( (float) transTime);

  for ( int timePassed=0; timePassed<=transTime; timePassed +=PULSE_PERIOD ){
    light( brightness, PULSE_PERIOD );

    brightness += transRate;
  }
}

class Task{
  public:
    Task(){
      
    }

};

class TaskManager{

  public:
    TaskManager(){

    }

  private:
  

};

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(12, OUTPUT);
  

}


// the loop function runs over and over again forever
void loop() {
  //randLight();
  smoothLight( 0, 1, 1000 );

  //light2( 0.06, 1000 );
  
  smoothLight( 1, 0, 1000 );
  
  //digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
  //delay(1000);                       // wait for a second
  //digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
  //delay(1000);                       // wait for a second
}
