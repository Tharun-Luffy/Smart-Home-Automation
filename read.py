import serial
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import time

# Load the pre-trained Logistic Regression model (assuming it's saved as logistic_model.pkl)
import joblib
model = joblib.load('logistic_model.pkl')

# Set up serial communication with Arduino
arduino_port = 'COM7'  # Update this with your actual port (e.g., 'COM3' on Windows, '/dev/ttyUSB0' on Linux)
baud_rate = 9600  # Match the baud rate used in Arduino code

# Start the serial connection
ser = serial.Serial(arduino_port, baud_rate)
time.sleep(2)  # Give time to establish the connection

# Load the same scaler that was used during training
scaler = joblib.load('scaler.pkl')

def process_sensor_data(sensor_data):
    # Convert the sensor data to a DataFrame
    columns = ["temp", "accX", "accY", "accZ", "gyroX", "gyroY", "gyroZ",
               "accAngleX", "accAngleY", "gyroAngleX", "gyroAngleY", "gyroAngleZ",
               "angleX", "angleY", "angleZ"]

    data = pd.DataFrame([sensor_data], columns=columns)

    # Scale the features using the fitted StandardScaler
    data_scaled = scaler.transform(data)

    return data_scaled

def predict_hand_up(data_scaled):
    # Predict if the hand is up or not using the trained logistic regression model
    prediction = model.predict(data_scaled)
    return prediction[0]  # 1 for hand up, 0 for not

try:
    while True:
        # Read a line from Arduino and decode it
        arduino_data = ser.readline().decode('utf-8').strip()
        

        # Split the data into a list of floats
        sensor_values = [float(val) for val in arduino_data.split(',')]

        # Process and scale the sensor data
        scaled_data = process_sensor_data(sensor_values)

        # Make the prediction
        hand_up = predict_hand_up(scaled_data)

        if hand_up == 1:
            print("Hand Up Detected")
        else:
            print("No Hand Up")

        time.sleep(0.5)  # Adjust the sleep time to match your reading frequency

except KeyboardInterrupt:
    print("Exiting...")
    ser.close()  # Close the serial port connection
