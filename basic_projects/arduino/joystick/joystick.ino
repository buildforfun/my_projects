#define VRX_PIN  A0
#define VRY_PIN  A1

int x = 0; 
int y = 0;

void setup() {
  Serial.begin(9600) ;
}

void loop() {
  // read analog X and Y analog values
  x = analogRead(VRX_PIN);
  y = analogRead(VRY_PIN);

  // print data to Serial Monitor on Arduino IDE
  Serial.print("x = ");
  Serial.print(x);
  Serial.print(", y = ");
  Serial.println(y);
  delay(200);
}
