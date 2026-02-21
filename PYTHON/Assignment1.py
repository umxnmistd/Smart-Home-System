from Assignment import Appliance

class WashingMachine(Appliance):
    def operate(self):
        if not self.is_on:
            print("Device is off. Please turn it on first.")
        else:
            print(f"{self.name} is washing clothes.")


class AirConditioner(Appliance):
    def operate(self):
        if not self.is_on:
            print("Device is off. Please turn it on first.")
        else:
            print(f"{self.name} is cooling the room.")


class Microwave(Appliance):
    def operate(self):
        if not self.is_on:
            print("Device is off. Please turn it on first.")
        else:
            print(f"{self.name} is heating food.")

class SmartTV(Appliance):
    def operate(self):
        if not self.is_on:
            print("Device is off. Please turn it on first.")
        else:
            print(f"{self.name} is streaming your favorite show.")