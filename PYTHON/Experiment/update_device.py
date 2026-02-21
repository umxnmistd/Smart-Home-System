from devices import find_device, get_device_type


def update_device(device_list):
    name = input("\nEnter the name of the device to update: ").strip()
    device = find_device(device_list, name)

    if not device:
        print("Device not found.")
        return

    new_name = input(f"Enter new name (press Enter to keep '{device.name}'): ").strip()
    if new_name and new_name.lower() != device.name.lower() and find_device(device_list, new_name):
        print("A device with that name already exists.")
        return
    if new_name:
        device.name = new_name

    new_type = input(
        f"Enter new device type (press Enter to keep '{get_device_type(device)}'): "
    ).strip()
    if new_type:
        device.device_type = new_type

    new_power = input(f"Enter new power in watts (press Enter to keep {device.power}): ").strip()
    if new_power:
        if not new_power.isdigit():
            print("Power must be a whole number.")
            return
        try:
            device.power = int(new_power)
        except ValueError as error:
            print(error)
            return

    print("Power state options: on / off / keep")
    state_choice = input("Set power state: ").strip().lower()
    if state_choice == "on":
        device.turn_on()
    elif state_choice == "off":
        device.turn_off()
    elif state_choice != "keep":
        print("Invalid power state option. Keeping current state.")

    print("Device updated successfully.")
