from devices import find_device


def delete_device(device_list):
    name = input("\nEnter the name of the device to delete: ").strip()
    device = find_device(device_list, name)

    if not device:
        print("Device not found.")
        return

    if device.is_on:
        device.turn_off()

    device_list.remove(device)
    print(f"{device.name} deleted successfully.")
