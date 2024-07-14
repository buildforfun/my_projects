import serial
import csv

# Connect to arduino
ser = serial.Serial('/dev/cu.usbmodem141101', 9600)

# Open data csv and append data to csv
with open('arduino/ultrasonic/ultrasonic_data.csv', 'a', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    while True:
        # Read a line from the serial port
        line = ser.readline().decode('utf-8').strip()

        # Split the line
        values = line.split(',')

        # Write the data to the CSV file
        csvwriter.writerow(values)

        # Flush the file to ensure data is written immediately
        csvfile.flush()

        print(f"Recorded: {line}")

# Close the serial port
ser.close()