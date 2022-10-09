#define PULSE_PERIOD 14

void light( float fraction, int totalTime ){
  fraction = fraction<0?0:( fraction > 1?1:fraction );

  int onTime = (int) (PULSE_PERIOD*fraction);
  int offTime = PULSE_PERIOD - onTime;
  
  for ( ;totalTime>0; totalTime -= PULSE_PERIOD ){
    digitalWrite(4, HIGH);   
    delay(onTime);                     
    digitalWrite(4, LOW);
    delay(offTime); 
    
  }
}

void setup() {
  // put your setup code here, to run once:

  pinMode(11, INPUT  );
  pinMode(4,  OUTPUT );

  //Serial.begin();
}

void loop() {
  // put your main code here, to run repeatedly:
  
  //Serial.println( digitalRead( 11 ) );

  if (  digitalRead( 11 ) >= 1 ){
    float brightness = ((float) ((millis()%1000)/10))/100;

    light(   (millis()%2000 < 1000)?brightness:1-brightness , 30 );
  }else{
    digitalWrite(11, LOW );
  }


}
