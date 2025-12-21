import serial
import sys
import time


def test_connection(port, baudrate=115200, timeout=2):
    print(f"Testing {port} at {baudrate} baud...")

    try:
        ser = serial.Serial(port, baudrate, timeout=1)
    except serial.SerialException as e:
        print(f"FAILED: Could not open port - {e}")
        return False

    print(f"Port opened successfully")

    start = time.time()
    bytes_received = 0

    while (time.time() - start) < timeout:
        data = ser.read(32)
        bytes_received += len(data)

    ser.close()

    if bytes_received > 0:
        print(f"SUCCESS: Received {bytes_received} bytes in {timeout}s")
        return True
    else:
        print(f"WARNING: Port open but no data received")
        return False


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python serial_test.py <PORT> [BAUDRATE]")
        sys.exit(1)

    port = sys.argv[1]
    baudrate = int(sys.argv[2]) if len(sys.argv) > 2 else 115200

    success = test_connection(port, baudrate)
    sys.exit(0 if success else 1)
