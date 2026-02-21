from Assignment import Appliance
from Assignment1 import WashingMachine, AirConditioner, Microwave, SmartTV

def total_power_usage(devices):
    total = 0
    for device in devices:
        if device.is_on:
            total += device.power
    return total

devices = [
    WashingMachine("LG Washer", 200),
    AirConditioner("Daikin AC", 300),
    Microwave("Panasonic Microwave", 400),
    SmartTV("Samsung TV", 5500),
]

for device in devices:
    device.turn_on()
    device.operate()
    print()

print("Total Power Usage:", total_power_usage(devices), "Watts")

print("Appliances currently ON:", Appliance.appliances_on)
