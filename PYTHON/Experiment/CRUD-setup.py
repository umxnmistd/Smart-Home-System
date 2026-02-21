from Assignment2 import devices
from create_device import create_device
from read_device import print_devices
from update_device import update_device
from delete_device import delete_device

for device in devices:
    if not hasattr(device, "device_type"):
        device.device_type = device.__class__.__name__


while True:
    print("\nDevice Manager")
    print("1. Create device")
    print("2. Read devices")
    print("3. Update device")
    print("4. Delete device")
    print("5. Exit")

    choice = input("Select an option (1-5): ").strip()

    if choice == "1":
        create_device(devices)
    elif choice == "2":
        print_devices(devices)
    elif choice == "3":
        update_device(devices)
    elif choice == "4":
        delete_device(devices)
    elif choice == "5":
        print("Goodbye.")
        break
    else:
        print("Invalid option. Please choose 1-5.")
