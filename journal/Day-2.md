# Control Systems – Day 2

Worked on failsafe detection today. Still no hardware but I can at least write the logic.

The detector checks for three things:
1. No packets coming in at all (signal lost)
2. All channels suddenly go to default values (1500 or 1000)
3. Channels freeze and stop changing (this ones sneaky)

The frozen channel detection was tricky to think through. Added a counter so it doesnt freak out over small pauses. It waits for like 10 frozen frames before calling it a failsafe.

States are just simple strings: "OK", "SIGNAL LOST", "FAILSAFE". Kept it basic on purpose cause I dont need anything complicated rn.

Cant actually test any of this until the receiver shows up but the logic makes sense to me. Hopefully it works first try lol (it wont).

Really hoping my package comes soon cause coding without testing feels weird.
