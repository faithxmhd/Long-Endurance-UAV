import serial
import struct
import sys

PORT = "COM3"
BAUD = 115200
HEADER = b'\x20\x40'
PACKET_SIZE = 32
CHANNELS_COUNT = 14

def calculate_checksum(data):
    return 0xFFFF - sum(data[:30]) & 0xFFFF

def parse_packet(data):
    channels = struct.unpack('<14H', data[2:30])
    return list(channels)

def main():
    try:
        ser = serial.Serial(PORT, BAUD, timeout=1)
        print(f"Connected to {PORT} at {BAUD} baud")
    except serial.SerialException as e:
        print(f"Failed to open {PORT}: {e}")
        sys.exit(1)

    try:
        while True:
            data = ser.read(PACKET_SIZE)
            
            if len(data) != PACKET_SIZE:
                continue
                
            if data[:2] != HEADER:
                continue
                
            expected_checksum = calculate_checksum(data)
            received_checksum = struct.unpack('<H', data[30:32])[0]
            
            if expected_checksum == received_checksum:
                channels = parse_packet(data)
                print(channels)
                
    except KeyboardInterrupt:
        print("\nProgram terminated by user")
    finally:
        ser.close()
        print("Serial port closed")

if __name__ == "__main__":
    main()