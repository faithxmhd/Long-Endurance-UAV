import serial.tools.list_ports


def list_serial_ports():
    ports = serial.tools.list_ports.comports()
    result = []
    for port in ports:
        result.append({
            "device": port.device,
            "description": port.description,
            "hwid": port.hwid
        })
    return result


def print_ports():
    ports = list_serial_ports()
    if not ports:
        print("No serial ports found")
        return

    print(f"Found {len(ports)} port(s):\n")
    for p in ports:
        print(f"  {p['device']}")
        print(f"    Description: {p['description']}")
        print(f"    HWID: {p['hwid']}")
        print()


if __name__ == "__main__":
    print_ports()
