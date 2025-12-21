import serial
import struct

HEADER = bytes([0x20, 0x40])
PACKET_SIZE = 32
NUM_CHANNELS = 14


def calculate_checksum(packet):
    return 0xFFFF - sum(packet[:30]) & 0xFFFF


def validate_packet(packet):
    if len(packet) != PACKET_SIZE:
        return False
    if packet[:2] != HEADER:
        return False
    expected = calculate_checksum(packet)
    received = struct.unpack('<H', packet[30:32])[0]
    return expected == received


def parse_channels(packet):
    return list(struct.unpack('<14H', packet[2:30]))


class IBusReader:
    def __init__(self, port, baudrate=115200):
        self.port = port
        self.baudrate = baudrate
        self.serial = None

    def connect(self):
        self.serial = serial.Serial(self.port, self.baudrate, timeout=1)

    def disconnect(self):
        if self.serial and self.serial.is_open:
            self.serial.close()

    def read_packet(self):
        if not self.serial:
            return None
        data = self.serial.read(PACKET_SIZE)
        if validate_packet(data):
            return parse_channels(data)
        return None

    def sync(self):
        while True:
            byte = self.serial.read(1)
            if byte == bytes([0x20]):
                next_byte = self.serial.read(1)
                if next_byte == bytes([0x40]):
                    rest = self.serial.read(PACKET_SIZE - 2)
                    packet = HEADER + rest
                    if validate_packet(packet):
                        return parse_channels(packet)
        return None


if __name__ == "__main__":
    import sys
    port = sys.argv[1] if len(sys.argv) > 1 else "COM3"

    reader = IBusReader(port)
    try:
        reader.connect()
        print(f"Connected to {port}")
        channels = reader.sync()
        while True:
            channels = reader.read_packet()
            if channels:
                print(channels)
    except KeyboardInterrupt:
        pass
    finally:
        reader.disconnect()
