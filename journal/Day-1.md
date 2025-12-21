# Control Systems – Day 1

Started writing the ibus reader script today even tho I dont have the receiver yet lol. Figured I'd get the code ready so when the FlySky arrives I can just plug it in and go.

Had to look up how the iBUS packet structure works - its 32 bytes with a header (0x20 0x40) and a checksum at the end. The checksum math is weird but I think I got it right. Wont know for sure until I test with real hardware tho.

The script reads packets from serial, validates them, and spits out the channel values as a list. Nothing fancy, no GUI or anything. Just raw numbers.

Also made a logger version that dumps everything to CSV so I can analyze it later. Might be useful for spotting patterns or whatever.

Stuff I learned today:
- iBUS packets are 32 bytes
- First 2 bytes are always 0x20 0x40
- 14 channels, each is 2 bytes (little endian)
- Checksum is 0xFFFF minus sum of first 30 bytes

Gotta get my hands on that FlySky soon. Kinda hard to test serial code without actual serial data lmao.
