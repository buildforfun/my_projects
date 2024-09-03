const int trigPin = 3;
const int echoPin = 2;

float duration, distance;
unsigned long timestamp;

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  Serial.begin(9600);
  
}

void loop() {
  // This sends out a short ultrasonic pulse by:
  // Set the trigPin LOW for 2 microseconds
  // Set the trigPin HIGH for 10 microseconds
  // Set the trigPin LOW again
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // The pulseIn() function measures the time it takes for the echo pin to go from
  // LOW to HIGH and back to LOW. This time represents how long it took for the 
  // ultrasonic pulse to travel to an object and back.
  duration = pulseIn(echoPin, HIGH);

  // This formula converts the duration into distance:
  // 0.0343 cm/µs is the speed of sound in air (343 m/s or 34,300 cm/s)
  // Multiply the duration by 0.0343 to get the round-trip distance in cm
  // Divide by 2 to get the one-way distance (from sensor to object)
  // This gives distance in cm
  distance = (duration*.0343)/2;
  
  // Get current timestamp
  timestamp = millis();
  
  // Print data in CSV format
  Serial.print(timestamp);
  Serial.print(",");
  Serial.println(distance);
  
  delay(5000);
}