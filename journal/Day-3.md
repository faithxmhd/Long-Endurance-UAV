# Control Systems – Day 3

Short day today. Made some utility scripts for when I eventually get the hardware.

Made two things:
- list_ports.py - shows all serial ports on the system with their descriptions
- serial_test.py - quick test to see if a port is working and receiving data

The list ports thing uses pyserial's built in tool which is nice. Shows the device name, description and hardware ID. Should be helpful when I have multiple USB things plugged in.

Serial test is basically just "open port, wait 2 seconds, did we get any bytes?" Simple but should save time later.

Ran list_ports on my pc and it found some ports but obviously nothing useful yet. Just bluetooth stuff and whatever.

Still waiting on that FlySky + USB-UART adapter. Shipping is taking forever smh.
