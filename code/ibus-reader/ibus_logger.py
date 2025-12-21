import serial
import struct
import csv
import time

PORT = "COM3"
BAUD = 115200
PACKET_SIZE = 32

def checksum_ok(packet):
    return (0xFFFF - sum(packet[:30]) & 0xFFFF) == struct.unpack("<H", packet[30:32])[0]

ser = serial.Serial(PORT, BAUD, timeout=1)

filename = f"ibus_log_{int(time.time())}.csv"
with open(filename, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["timestamp"] + [f"ch{i+1}" for i in range(14)])

    while True:
        packet = ser.read(PACKET_SIZE)

        if len(packet) != PACKET_SIZE:
            continue
        if packet[0] != 0x20 or packet[1] != 0x40:
            continue
        if not checksum_ok(packet):
            continue

        channels = struct.unpack("<14H", packet[2:30])
        writer.writerow([time.time()] + list(channels))
        f.flush()
