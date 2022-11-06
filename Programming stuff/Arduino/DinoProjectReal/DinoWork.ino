
















void setup() {
  Serial.begin( 9600 );


  pinMode(LED_BUILTIN, OUTPUT);
}



void loop() {
  Serial.println(micros());
  digitalWrite( LED_BUILTIN, millis()%800<100?HIGH:LOW );
}
