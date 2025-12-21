import time

STATE_OK = "OK"
STATE_SIGNAL_LOST = "SIGNAL LOST"
STATE_FAILSAFE = "FAILSAFE"

DEFAULT_CENTER = 1500
DEFAULT_LOW = 1000
FREEZE_THRESHOLD = 50
PACKET_TIMEOUT = 0.5


class FailsafeDetector:
    def __init__(self, freeze_count=10, timeout=PACKET_TIMEOUT):
        self.freeze_count = freeze_count
        self.timeout = timeout
        self.last_channels = None
        self.last_packet_time = None
        self.frozen_counter = 0
        self.state = STATE_OK

    def update(self, channels):
        now = time.time()

        if channels is None:
            if self.last_packet_time and (now - self.last_packet_time) > self.timeout:
                self.state = STATE_SIGNAL_LOST
            return self.state

        self.last_packet_time = now

        if self._is_failsafe_values(channels):
            self.state = STATE_FAILSAFE
            return self.state

        if self._is_frozen(channels):
            self.frozen_counter += 1
            if self.frozen_counter >= self.freeze_count:
                self.state = STATE_FAILSAFE
        else:
            self.frozen_counter = 0
            self.state = STATE_OK

        self.last_channels = channels
        return self.state

    def _is_failsafe_values(self, channels):
        all_default = all(
            ch == DEFAULT_CENTER or ch == DEFAULT_LOW or ch == 0
            for ch in channels[:4]
        )
        return all_default

    def _is_frozen(self, channels):
        if self.last_channels is None:
            return False
        for i in range(min(4, len(channels))):
            if abs(channels[i] - self.last_channels[i]) > FREEZE_THRESHOLD:
                return False
        return True

    def check_timeout(self):
        if self.last_packet_time is None:
            return self.state
        if (time.time() - self.last_packet_time) > self.timeout:
            self.state = STATE_SIGNAL_LOST
        return self.state


if __name__ == "__main__":
    import sys
    sys.path.insert(0, "..")
    from ibus_reader.ibus_reader import IBusReader

    port = sys.argv[1] if len(sys.argv) > 1 else "COM3"

    reader = IBusReader(port)
    detector = FailsafeDetector()

    try:
        reader.connect()
        print(f"Monitoring {port}...")
        reader.sync()

        while True:
            channels = reader.read_packet()
            state = detector.update(channels)
            print(f"{state} | {channels[:4] if channels else 'No data'}")

    except KeyboardInterrupt:
        pass
    finally:
        reader.disconnect()
