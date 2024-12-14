class Thermostat:
    def __init__(self, device_id, name, location):
        self.device_id = device_id
        self.name = name
        self.location = location
        self.temperature = 20
        self.mode = "OFF"  # OFF, HEAT, COOL
        self.schedule = {}

    def set_temperature(self, temp):
        if 10 <= temp <= 30:
            self.temperature = temp
            return f"Temperature set to {temp}°C"
        return "Invalid temperature range"

    def set_mode(self, mode):
        valid_modes = ["OFF", "HEAT", "COOL"]
        if mode.upper() in valid_modes:
            self.mode = mode.upper()
            return f"Mode set to {mode}"
        return "Invalid mode"

    def set_schedule(self, time, temperature):
        self.schedule[time] = temperature
        return f"Schedule updated for {time}" 