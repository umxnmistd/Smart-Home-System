from Assignment import Appliance
from Assignment1 import WashingMachine, AirConditioner, Microwave, SmartTV
from devices import find_device


def create_device(device_list):
    print("\nEnter any device type you want (example: SmartTV, Fan, Heater).")
    type_choice = input("Enter device type: ").strip()
    if not type_choice:
        print("Device type cannot be empty.")
        return

    classes = {
        "washingmachine": WashingMachine,
        "airconditioner": AirConditioner,
        "microwave": Microwave,
        "smarttv": SmartTV,
        "appliance": Appliance,
    }

    normalized_type = type_choice.replace(" ", "").lower()
    selected_class = classes.get(normalized_type, Appliance)

    name = input("Enter device name: ").strip()
    if not name:
        print("Device name cannot be empty.")
        return

    if find_device(device_list, name):
        print(f"{name} already exists!")
        return

    power_input = input("Enter power (watts): ").strip()
    if not power_input.isdigit():
        print("Power must be a whole number.")
        return

    power = int(power_input)
    try:
        new_device = selected_class(name, power)
    except ValueError as error:
        print(error)
        return

    new_device.device_type = type_choice
    device_list.append(new_device)
    print(f"{name} added successfully!")
