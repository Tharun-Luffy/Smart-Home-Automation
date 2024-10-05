

# Smart Home Automation Using Hand Gestures with MPU 6050 Sensor

This project demonstrates a smart home automation system that utilizes hand gestures captured by the MPU 6050 sensor to control various home appliances.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Hardware Requirements](#hardware-requirements)
- [Software Requirements](#software-requirements)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Features

- Real-time hand gesture recognition using the MPU 6050 sensor.
- Control home appliances based on gestures (e.g., turning lights on/off, adjusting thermostat).
- User-friendly interface for monitoring gesture recognition.
- Integration with home automation platforms (optional).

## Prerequisites

- Python 3.x installed on your system.
- Libraries: `pyserial`, `numpy`, and any other dependencies required for your project.
  
  You can install them using pip:

  ```bash
  pip install pyserial numpy
  ```

## Hardware Requirements

- **MPU 6050 Sensor**: For capturing hand gestures.
- **Microcontroller**: Arduino or Raspberry Pi to interface with the MPU 6050.
- **Home Appliances**: Devices to be controlled (e.g., lights, fans, etc.).
- **Power Supply**: For the microcontroller and appliances.

## Software Requirements

- Arduino IDE: For uploading the MPU 6050 sketch to the Arduino.
- Python: For the main application that processes gesture data.
  
## Project Structure

```
Smart_Home_Automation/
│
├── Arduino/
│   ├── mpu6050_gesture_control.ino  # Arduino sketch for gesture recognition
│
├── Python/
│   ├── gesture_recognition.py         # Python script for processing gestures
│
└── README.md                          # Project documentation
```

## Setup Instructions

1. **Wiring the MPU 6050**:
   - Connect the MPU 6050 sensor to your microcontroller according to the following:
     - VCC to 5V
     - GND to Ground
     - SDA to A4 (for Arduino)
     - SCL to A5 (for Arduino)

2. **Upload Arduino Sketch**:
   - Open the Arduino IDE and load the `mpu6050_gesture_control.ino` file.
   - Make sure to install the required libraries (e.g., `MPU6050_tockn`).
   - Upload the sketch to your Arduino.

3. **Run the Python Script**:
   - Open a terminal or command prompt.
   - Navigate to the Python directory containing `gesture_recognition.py`.
   - Execute the script using:

   ```bash
   python gesture_recognition.py
   ```

   Ensure that the serial port in the script matches the one your Arduino is connected to.

## Usage

- Move your hand in specific gestures to control connected home appliances.
- The Python script will output the recognized gesture and the corresponding action taken.

### Example Gestures
- **Wave Left**: Turn off the lights.
- **Wave Right**: Turn on the lights.
- **Swipe Up**: Increase thermostat temperature.
- **Swipe Down**: Decrease thermostat temperature.

## Troubleshooting

- **Connection Issues**: Ensure the correct COM port is specified in the Python script.
- **Gesture Recognition Problems**: Check the MPU 6050 sensor wiring and calibration.
- **Performance Issues**: Ensure your Python environment is set up correctly, and no other applications are using the serial port.

## Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository and submit a pull request. 

## License

This project is open-source and available for modification and redistribution under the MIT License.

