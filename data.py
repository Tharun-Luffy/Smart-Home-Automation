import serial
import csv
import time

# Change this to your correct serial port (e.g., 'COM3' for Windows or '/dev/ttyUSB0' for Linux)
serial_port = 'COM7' # Removed the extra space at the end
baud_rate = 9600
file_name = 'mpu6050_data.csv'

# Open serial connection
ser = serial.Serial('COM7', baud_rate)

# Open CSV file for writing
with open(file_name, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    
    # Write header to CSV
    csv_writer.writerow(["temp", "accX", "accY", "accZ", "gyroX", "gyroY", "gyroZ", "accAngleX", "accAngleY", "gyroAngleX", "gyroAngleY", "gyroAngleZ", "angleX", "angleY", "angleZ"])
    
    try:
        while True:
            # Read a line from the serial port
            line = ser.readline().decode('utf-8').strip()
            
            # Split the line by commas and write to the CSV file
            data = line.split(',')
            csv_writer.writerow(data)
            
            print(data)  # Print data to console for verification
            time.sleep(0.001)  # 1 ms delay

    except KeyboardInterrupt:
        print("Logging stopped.")
        ser.close()  # Close serial connection