class Led:
    """Class Led"""

    def __init__(self, frame):
        self.enabled = False
        self.led = frame
        self.update()

    def update(self):
        if self.enabled:
            self.led.setProperty("class", "led_enabled")
        else:
            self.led.setProperty("class", "led_disabled")

        self.led.style().unpolish(self.led)
        self.led.style().polish(self.led)
        self.led.update()
