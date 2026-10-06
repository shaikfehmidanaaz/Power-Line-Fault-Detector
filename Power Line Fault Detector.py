class PowerLineFaultDetector:
    def __init__(self, max_current, min_voltage, max_voltage, max_earth_leakage):
        self.max_current = max_current
        self.min_voltage = min_voltage
        self.max_voltage = max_voltage
        self.max_earth_leakage = max_earth_leakage

        self.current = 0
        self.voltage = 0
        self.earth_leakage = 0

    def measure_values(self, voltage, current, earth_leakage):
        self.voltage = voltage
        self.current = current
        self.earth_leakage = earth_leakage

    def detect_fault(self):
        faults = []

        print("\n----- POWER LINE MONITORING -----")
        print(f"Voltage        : {self.voltage:.2f} V")
        print(f"Current        : {self.current:.2f} A")
        print(f"Earth Leakage  : {self.earth_leakage:.3f} A")

        # Overcurrent check
        if self.current > self.max_current:
            faults.append("OVERCURRENT")

        # Undervoltage check
        if self.voltage < self.min_voltage:
            faults.append("UNDERVOLTAGE")

        # Overvoltage check
        if self.voltage > self.max_voltage:
            faults.append("OVERVOLTAGE")

        # Earth leakage check
        if self.earth_leakage > self.max_earth_leakage:
            faults.append("EARTH FAULT")

        print("\n----- FAULT ANALYSIS -----")

        if len(faults) == 0:
            print("Status : NORMAL")
            print("No power-line fault detected.")
        else:
            print("Status : FAULT DETECTED")

            for fault in faults:
                print(f"Fault  : {fault}")

            print("\nProtection System : TRIP")
            print("Load               : DISCONNECTED")

    def display_limits(self):
        print("\n----- PROTECTION LIMITS -----")
        print(f"Maximum Current       : {self.max_current} A")
        print(f"Minimum Voltage       : {self.min_voltage} V")
        print(f"Maximum Voltage       : {self.max_voltage} V")
        print(f"Maximum Earth Leakage : {self.max_earth_leakage} A")


def main():

    print("======================================")
    print("       POWER LINE FAULT DETECTOR")
    print("======================================")

    try:
        # Protection limits
        max_current = float(
            input("\nEnter maximum current limit (A): ")
        )

        min_voltage = float(
            input("Enter minimum voltage limit (V): ")
        )

        max_voltage = float(
            input("Enter maximum voltage limit (V): ")
        )

        max_earth_leakage = float(
            input("Enter maximum earth leakage limit (A): ")
        )

        # Measured values
        voltage = float(
            input("\nEnter measured voltage (V): ")
        )

        current = float(
            input("Enter measured current (A): ")
        )

        earth_leakage = float(
            input("Enter measured earth leakage (A): ")
        )

        detector = PowerLineFaultDetector(
            max_current,
            min_voltage,
            max_voltage,
            max_earth_leakage
        )

        detector.display_limits()

        detector.measure_values(
            voltage,
            current,
            earth_leakage
        )

        detector.detect_fault()

    except ValueError:
        print("\nInvalid input! Please enter numerical values.")


if __name__ == "__main__":
    main()
