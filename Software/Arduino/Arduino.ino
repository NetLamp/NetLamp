unsigned char rd;
char pin = 13;

void setup() {
  // initialize serial communications at 9600 bps:
  Serial.begin(9600); 
  pinMode(pin, OUTPUT);
}

void loop() {
  while (Serial.available() == 0) {
  
  };
  
  rd = Serial.read();
  
  analogWrite(pin,rd);
  Serial.println(rd);
  
  delay(2);                     
}
