#include <DHT.h>

#define DHTPIN 2     // Digital pin connected to the DHT sensor
#define DHTTYPE DHT11   // DHT 11

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  // initializes and sets the initial values, 
  Serial.begin(9600);
  dht.begin();
  
}

void loop() {
  //  loops consecutively - allowing your program to change and respond. 
  delay(5000);

  unsigned long timestamp = millis();
  float h = dht.readHumidity();
  float t = dht.readTemperature();

  if (isnan(h) || isnan(t)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  float hic = dht.computeHeatIndex(t, h, false);

  // Print data in CSV format
  Serial.print(timestamp);
  Serial.print(",");
  Serial.print(h);
  Serial.print(",");
  Serial.print(t);
  Serial.print(",");
  Serial.println(hic);
}