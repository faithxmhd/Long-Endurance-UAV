This diagram below shows the full control oversight of the project.

STATUS: SYSTEM ARMED
MODE: MANUAL CONTROL (ACRO)

      ╔══════════════════════════════╗
      ║   THE PILOT (HUMAN INPUT)    ║
      ║      [ 🧠 + 🎮 ]             ║
      ╚══════════════╦═══════════════╝
                     ║
      (STICK INPUT)  ║ ▶▶▶ CONTROL SIGNALS
                     ║
      ╔══════════════▼═══════════════╗
      ║    TRANSMITTER (TX RADIO)    ║
      ║    [ 📡 SIGNAL ENCODER ]     ║
      ╚══════════════╦═══════════════╝
                     ║
                     ║ ⚡ 2.4GHz RF LINK ⚡
                     ║ (WIRELESS CONTROL)
                     ║
      ╔══════════════▼═══════════════╗
      ║     RECEIVER (RX UNIT)       ║
      ║    [ 📥 SIGNAL DECODE ]      ║
      ╚══════════════╦═══════════════╝
                     ║
   (DIGITAL DATA)    ║ ▶▶▶ iBUS / SBUS
   0101101011...     ║
                     ║
╔════════════════════▼════════════════════╗
║    FLIGHT CONTROLLER (CONTROL CORE)     ║
║   [ ⚙️ MCU + GYRO + LOGIC ]              ║
╚════════╦═══════════════════════╦════════╝
         ║                       ║
         ║ (MOTOR COMMANDS)      ║ (ON-SCREEN DATA)
         ║ ▼▼▼▼                  ║ ▶▶▶▶
         ║                       ║
╔════════▼═════════╗    ╔════════▼═════════╗
║   4-IN-1 ESC     ║    ║   OSD / VIDEO    ║
║ [ POWER CONTROL ]║    ║ [ FLIGHT DATA ]  ║
╚════════╦═════════╝    ╚════════╦═════════╝
         ║                       ║
  (CONTROLLED POWER)              ║ (TO VTX / DISPLAY)
  ⚡⚡⚡⚡⚡⚡⚡                   📡 ▶▶ 🥽
         ║
╔════════▼═════════╗
║    BRUSHLESS     ║
║     MOTORS       ║
║  [ THRUST OUT ]  ║
╚══════════════════╝


Above is a TX-RX Communications diagram for basic understanding.