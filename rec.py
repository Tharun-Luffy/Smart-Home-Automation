import serial
import requests

# Open serial connection
ser = serial.Serial('COM7', 9600)  # Change 'COM3' to your port, or '/dev/ttyUSB0' on Linux
flask_url = 'http://127.0.0.1:5000/Sensor_data'

while True:
    if ser.in_waiting > 0:
        # Read a line from the serial port
        line = ser.readline().decode('utf-8').strip()
        # Split CSV data
        sensor_data = line.split(',')

        # Make sure you have enough values (match the number of sensor outputs)
        if len(sensor_data) == 15:  # This includes temperature, which you're not sending
            payload = {
                'accel_x': sensor_data[1],
                'accel_y': sensor_data[2],
                'accel_z': sensor_data[3],
                'gyro_x': sensor_data[4],
                'gyro_y': sensor_data[5],
                'gyro_z': sensor_data[6],
                'acc_angle_x': sensor_data[7],
                'acc_angle_y': sensor_data[8],
                'gyro_angle_x': sensor_data[9],
                'gyro_angle_y': sensor_data[10],
                'gyro_angle_z': sensor_data[11],
                'angle_x': sensor_data[12],
                'angle_y': sensor_data[13],
                'angle_z': sensor_data[14]
            }

            # Send data to Flask
            response = requests.post(flask_url, data=payload)
            print(response.json())
            print(payload['accel_x'])
        else:
            print("Fuck Off")
