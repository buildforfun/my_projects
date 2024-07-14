## LCD monitor
source: https://core-electronics.com.au/guides/use-lcd-arduino-uno/

The breadboard allows each pin has its own separate line to operate.

1. 5v and GND to the - and + rows in the breadboard.
2. VSS(GND) and K from the LCD screen to the GND.
3. VDD(5V) and A from the LCD to the 5V.
4. VO to center pin of your potentiometer, this will allow you to control the contrast.
5. RS to pin 12 - Register Select (0 for Command Register, 1 for Data Register)
6. RW - Read/write select (0 for write, 1 for read) - ground this
7. E - Data enable - connect this to pin 11
8. Connect data pins - D4, D5, D6, D7 to 5,4,3,2

# Heart emoji
Each cell is 5x8, you can check this by setting the potentiometer to max and seeing it's 32 cells of 5x8.
Each byte in the array represents one row of the 5x8 pixel grid. Although a byte has 8 bits, only the rightmost 5 bits are used for the character display on the LCD. The 0b prefix indicates that the following number is in binary format. '1' represents a pixel that's on, '0' represents a pixel that's off.