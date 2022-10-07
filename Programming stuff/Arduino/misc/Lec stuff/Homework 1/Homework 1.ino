
void light( float fraction, int totalTime ){
  fraction = fraction<0?0:( fraction > 1?1:fraction );

  int onTime = (int) (PULSE_PERIOD*fraction);
  int offTime = PULSE_PERIOD - onTime;
  
  for ( ;totalTime>0; totalTime -= PULSE_PERIOD ){
    digitalWrite(11, HIGH);   
    delay(onTime);                     
    digitalWrite(11, LOW);
    delay(offTime); 
    
  }
}

void setup() {
  // put your setup code here, to run once:

  pinMode(11, INPUT  );
  pinMode(4,  OUTPUT );

}

void loop() {
  // put your main code here, to run repeatedly:

  if ( digitalRead( 11 ) > 1 ){
    light( ((float) ((millis()%1000)/10))/100 );
  }else{
    digitalWrite(11, LOW );
  }


}
