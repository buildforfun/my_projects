#include <LiquidCrystal.h>

// Initialize the LCD. Adjust these pin numbers to match your wiring.
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

byte heart[8] = {
  0b00000,  // Row 1: No pixels on
  0b01010,  // Row 2: Pixels 2 and 4 on
  0b11111,  // Row 3: All pixels on
  0b11111,  // Row 4: All pixels on
  0b11111,  // Row 5: All pixels on
  0b01110,  // Row 6: Pixels 2, 3, and 4 on
  0b00100,  // Row 7: Pixel 3 on
  0b00000   // Row 8: No pixels on
};

void setup() {
  lcd.begin(16, 2);
  lcd.clear();
  lcd.createChar(0, heart);

  // Print the first line
  lcd.setCursor(0, 0);
  lcd.print("Hello World ");

  // Print the second line
  lcd.setCursor(0, 1);
  lcd.write(byte(0));
}

void loop() {}