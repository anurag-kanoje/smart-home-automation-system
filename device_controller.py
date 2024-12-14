from ..devices.light import Light
from ..devices.thermostat import Thermostat
from ..devices.camera import Camera

class DeviceController:
    def __init__(self):
        self.devices = {}

    def add_device(self, device_type, device_id, name, location):
        if device_type.lower() == "light":
            device = Light(device_id, name, location)
        elif device_type.lower() == "thermostat":
            device = Thermostat(device_id, name, location)
        elif device_type.lower() == "camera":
            device = Camera(device_id, name, location)
        else:
            return "Invalid device type"

        self.devices[device_id] = device
        return f"{device_type} added successfully"

    def get_device(self, device_id):
        return self.devices.get(device_id)

    def list_devices(self):
        return [
            f"{device_id}: {device.__class__.__name__} - {device.name}"
            for device_id, device in self.devices.items()
        ] 