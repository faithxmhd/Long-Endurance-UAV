CH_ROLL = 0
CH_PITCH = 1
CH_THROTTLE = 2
CH_YAW = 3

MIN_CHANNEL = 1000
MAX_CHANNEL = 2000
CENTER = 1500

MIN_MOTOR = 1000
MAX_MOTOR = 2000


def normalize(value, min_val=MIN_CHANNEL, max_val=MAX_CHANNEL):
    return (value - min_val) / (max_val - min_val) * 2 - 1


def clamp(value, min_val=MIN_MOTOR, max_val=MAX_MOTOR):
    return max(min_val, min(max_val, int(value)))


def mix_quad_x(channels):
    throttle = channels[CH_THROTTLE]
    roll = normalize(channels[CH_ROLL])
    pitch = normalize(channels[CH_PITCH])
    yaw = normalize(channels[CH_YAW])

    base = throttle - MIN_CHANNEL

    motor_fl = base + pitch + roll - yaw
    motor_fr = base + pitch - roll + yaw
    motor_bl = base - pitch + roll + yaw
    motor_br = base - pitch - roll - yaw

    scale = (MAX_MOTOR - MIN_MOTOR) / (MAX_CHANNEL - MIN_CHANNEL)

    return [
        clamp(MIN_MOTOR + motor_fl * scale),
        clamp(MIN_MOTOR + motor_fr * scale),
        clamp(MIN_MOTOR + motor_bl * scale),
        clamp(MIN_MOTOR + motor_br * scale)
    ]


class VirtualFC:
    def __init__(self, mixer_func=mix_quad_x):
        self.mixer = mixer_func
        self.armed = False
        self.motor_outputs = [MIN_MOTOR] * 4

    def set_armed(self, armed):
        self.armed = armed
        if not armed:
            self.motor_outputs = [MIN_MOTOR] * 4

    def update(self, channels):
        if not self.armed:
            self.motor_outputs = [MIN_MOTOR] * 4
            return self.motor_outputs

        if channels[CH_THROTTLE] < MIN_CHANNEL + 50:
            self.motor_outputs = [MIN_MOTOR] * 4
            return self.motor_outputs

        self.motor_outputs = self.mixer(channels)
        return self.motor_outputs

    def get_outputs(self):
        return self.motor_outputs


if __name__ == "__main__":
    fc = VirtualFC()
    fc.set_armed(True)

    test_inputs = [
        [1500, 1500, 1000, 1500],
        [1500, 1500, 1500, 1500],
        [1600, 1500, 1500, 1500],
        [1500, 1600, 1500, 1500],
        [1500, 1500, 1500, 1600],
        [1500, 1500, 2000, 1500],
    ]

    labels = [
        "Throttle low (idle)",
        "Center all, mid throttle",
        "Roll right",
        "Pitch forward",
        "Yaw right",
        "Full throttle",
    ]

    print("Virtual FC Mixer Test (Quad-X)")
    print("Motors: [FL, FR, BL, BR]\n")

    for channels, label in zip(test_inputs, labels):
        motors = fc.update(channels)
        print(f"{label}")
        print(f"  Input:  {channels}")
        print(f"  Output: {motors}\n")
