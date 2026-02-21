def total_power_usage(device_list):
    total = 0
    for device in device_list:
        if device.is_on:
            total += device.power
    return total


def find_device(device_list, name):
    for device in device_list:
        if device.name.lower() == name.lower():
            return device
    return None


def get_device_type(device):
    return getattr(device, "device_type", device.__class__.__name__)
