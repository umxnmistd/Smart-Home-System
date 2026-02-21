from Assignment import Appliance
from devices import total_power_usage, get_device_type


def print_devices(device_list):
    if not device_list:
        print("\nNo devices found.")
        return

    print("\nCurrent Devices:")
    for index, device in enumerate(device_list, start=1):
        status = "ON" if device.is_on else "OFF"
        print(
            f"{index}. {device.name} | Type: {get_device_type(device)} | "
            f"Power: {device.power}W | Status: {status}"
        )

    print(f"Total Power Usage: {total_power_usage(device_list)} Watts")
    print(f"Appliances currently ON: {Appliance.appliances_on}")
