# Control Systems – Day 4

Started working on the virtual flight controller today. This part I can actually test without hardware which is nice.

The idea is to take channel inputs (roll, pitch, throttle, yaw) and calculate what motor values would be. No actual motors involved obv, just the math.

Did a quad-x mixer which is the standard + layout but rotated 45 degrees. Each motor gets a different combo of the inputs:
- Front left: +pitch +roll -yaw
- Front right: +pitch -roll +yaw
- Back left: -pitch +roll +yaw
- Back right: -pitch -roll -yaw

Also added an arming system. Motors stay at minimum until you arm it. Safety first or whatever lol.

The normalize function converts channel values (1000-2000) to -1 to +1 range which makes the mixing math cleaner.

Ran some tests with fake inputs and the outputs look right. Roll right makes left motors spin faster, pitch forward makes back motors spin faster, etc. Physics checks out.

This is the one thing I could actually verify without the receiver. Small win.
