class Appliance:
    appliances_on = 0

    def __init__(self, name, power, is_on=False):
        self.name = name
        self._power = power
        self._is_on = is_on

    @property
    def power(self):
        return self._power

    @power.setter
    def power(self, value):
        if value < 0:
            raise ValueError("Power cannot be negative.")
        self._power = value

    @property
    def is_on(self):
        return self._is_on

    def turn_on(self):
        if self.power > 2000:
            print(f"{self.name} cannot be turned on. Power exceeds 2000W.")
            return

        if not self._is_on:
            self._is_on = True
            Appliance.appliances_on += 1
            print(f"{self.name} is now ON.")

    def turn_off(self):
        if self._is_on:
            self._is_on = False
            Appliance.appliances_on -= 1
            print(f"{self.name} is now OFF.")

    def operate(self):
        if not self._is_on:
            print(f"{self.name} is off. Please turn it on first.")
        else:
            print(f"{self.name} is operating.")