from flask import Flask, jsonify, Response
import serial
import time

app = Flask(__name__)

# Configure the serial port to match your Arduino's port and baud rate
ser = serial.Serial('COM7', 9600, timeout=1)  # Replace 'COM7' with your actual port

# Function to read data from Arduino
def read_arduino_data():
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').strip()  # Read line from serial and decode
        return line
    return None

# Route to stream live sensor data from Arduino
@app.route('/sensor_data', methods=['GET'])
def stream_sensor_data():
    def generate():
        while True:
            data = read_arduino_data()
            if data:
                yield f"data: {data}\n\n"
            time.sleep(1)  # Adjust the delay as needed

    return Response(generate(), mimetype='text/event-stream')

@app.route('/')
def index():
    return "Visit /sensor_data for live sensor readings!"

if __name__ == '__main__':
    app.run(debug=True)
