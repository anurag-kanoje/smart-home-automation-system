class Light:
    def __init__(self, device_id, name, location):
        self.device_id = device_id
        self.name = name
        self.location = location
        self.state = False
        self.brightness = 0
        self.color = "white"

    def turn_on(self):
        self.state = True
        return f"Light {self.name} turned on"

    def turn_off(self):
        self.state = False
        return f"Light {self.name} turned off"

    def set_brightness(self, level):
        if 0 <= level <= 100:
            self.brightness = level
            return f"Brightness set to {level}%"
        return "Invalid brightness level"

    def set_color(self, color):
        self.color = color
        return f"Color changed to {color}" 