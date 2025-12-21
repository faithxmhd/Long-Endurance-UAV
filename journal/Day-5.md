# Control Systems – Day 5

Spent today cleaning up code and making everything more modular. Refactored the ibus reader into a proper class so other scripts can import it easily.

The IBusReader class now has:
- connect/disconnect methods
- read_packet for getting channel data
- sync method for finding packet boundaries (this was annoying to figure out)

Current folder structure:
```
code/
├── ibus-reader/   (packet reading + logging)
├── failsafe/      (signal loss detection)
├── utils/         (port listing + testing)
└── virtual-fc/    (mixer + motor output)
```

Tested what I could with fake data. The virtual FC mixer works great, utility scripts run fine. The ibus reader and failsafe stuff will have to wait until I get actual hardware.

Honestly getting impatient at this point. All this code sitting here ready to go and nothing to test it on lmao. Gonna check the tracking number again brb.

Next I wanna look into PID control but thats a whole rabbit hole. For now the foundation is there, just need that FlySky to actually validate everything works.
