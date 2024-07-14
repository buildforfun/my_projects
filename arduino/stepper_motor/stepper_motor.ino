#include <Stepper.h>

const int stepsPerRevolution = 2038;
Stepper myStepper = Stepper(stepsPerRevolution, 8, 10, 9, 11);

int currentPosition = 0;  // Variable to track position

void setup() {
    Serial.begin(9600);  // Initialize serial communication
}

void loop() {
    // Rotate CW slowly at 5 RPM
    myStepper.setSpeed(5);
    myStepper.step(stepsPerRevolution);
    currentPosition += stepsPerRevolution;
    
    // Send position to Python
    Serial.println(currentPosition);
    
    delay(1000);
    
    // Rotate CCW quickly at 10 RPM
    myStepper.setSpeed(10);
    myStepper.step(-stepsPerRevolution);
    currentPosition -= stepsPerRevolution;
    
    // Send position to Python
    Serial.println(currentPosition);

    // This will print the stepsPerRevolution 2038 and 0 every time it rotates.
    
    delay(1000);
}