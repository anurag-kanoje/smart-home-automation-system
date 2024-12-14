class Camera:
    def __init__(self, device_id, name, location):
        self.device_id = device_id
        self.name = name
        self.location = location
        self.recording = False
        self.motion_detection = False

    def start_recording(self):
        self.recording = True
        return f"Recording started on camera {self.name}"

    def stop_recording(self):
        self.recording = False
        return f"Recording stopped on camera {self.name}"

    def toggle_motion_detection(self):
        self.motion_detection = not self.motion_detection
        status = "enabled" if self.motion_detection else "disabled"
        return f"Motion detection {status} on camera {self.name}"

    def get_live_feed(self):
        return f"Streaming live feed from camera {self.name}" 