import ctypes
import serial
import time

# Constants for serial port settings
GENERIC_READ = 0x80000000
GENERIC_WRITE = 0x40000000
OPEN_EXISTING = 3
FILE_ATTRIBUTE_NORMAL = 128
INVALID_HANDLE_VALUE = -1

# Define the DCB structure
class DCB(ctypes.Structure):
    _fields_ = [
        ("DCBlength", ctypes.c_ulong),
        ("BaudRate", ctypes.c_ulong),
        ("fBinary", ctypes.c_byte),
        ("fParity", ctypes.c_byte),
        ("fOutxCtsFlow", ctypes.c_byte),
        ("fOutxDsrFlow", ctypes.c_byte),
        ("fDtrControl", ctypes.c_byte),
        ("fDsrSensitivity", ctypes.c_byte),
        ("fTXContinueOnXoff", ctypes.c_byte),
        ("fOutX", ctypes.c_byte),
        ("fInX", ctypes.c_byte),
        ("fErrorChar", ctypes.c_byte),
        ("fNull", ctypes.c_byte),
        ("fRtsControl", ctypes.c_byte),
        ("fAbortOnError", ctypes.c_byte),
        ("fDummy2", ctypes.c_byte * 4),
        ("wReserved", ctypes.c_ushort * 4),
        ("XonLim", ctypes.c_ushort),
        ("XoffLim", ctypes.c_ushort),
        ("ByteSize", ctypes.c_byte),
        ("Parity", ctypes.c_byte),
        ("StopBits", ctypes.c_byte),
        ("XonChar", ctypes.c_byte),
        ("XoffChar", ctypes.c_byte),
        ("ErrorChar", ctypes.c_byte),
        ("EofChar", ctypes.c_byte),
        ("EvtChar", ctypes.c_byte),
        ("wReserved1", ctypes.c_ushort * 16),
    ]

# Function to configure the serial port
def configure_serial_port(handle):
    dcb = DCB()
    dcb.DCBlength = ctypes.sizeof(DCB)
    dcb.BaudRate = 9600  # Set baud rate to 9600
    dcb.ByteSize = 8  # 8 data bits
    dcb.Parity = 0  # No parity
    dcb.StopBits = 0  # 1 stop bit

    # Set the DCB structure
    if not ctypes.windll.kernel32.SetCommState(handle, ctypes.byref(dcb)):
        print("Error setting DCB structure")
        return False

    return True

# Function to open the serial port
def open_serial_port(port_name):
    handle = ctypes.windll.kernel32.CreateFileW(
        port_name,
        GENERIC_READ | GENERIC_WRITE,
        0,  # No sharing
        None,  # No security attributes
        OPEN_EXISTING,
        FILE_ATTRIBUTE_NORMAL,
        None  # No template file
    )
    
    if handle == INVALID_HANDLE_VALUE:
        print(f"Error opening serial port {port_name}")
        return None

    # Configure the serial port
    if not configure_serial_port(handle):
        ctypes.windll.kernel32.CloseHandle(handle)
        return None
    
    return handle

# Main execution
if __name__ == '__main__':
    serial_port = r'\\.\COM7'  # Serial port name for Windows

    # Open the serial port
    handle = open_serial_port(serial_port)
    if not handle:
        exit(1)

    # Create a pyserial Serial object using the same settings
    ser = serial.Serial(serial_port, 9600, timeout=1)

    try:
        time.sleep(2)  # Wait for the connection to be established
        while True:
            if ser.in_waiting > 0:  # Check if there's data to read
                line = ser.readline().decode('utf-8', errors='ignore').strip()  # Read and decode
                print(f"Received: {line}")  # Output the received line
    except KeyboardInterrupt:
        print("Terminating...")

    # Close the serial port
    ctypes.windll.kernel32.CloseHandle(handle)
    ser.close()  # Close the pyserial connection
    print("Closed serial port.")
