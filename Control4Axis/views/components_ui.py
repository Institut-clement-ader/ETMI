# -*- coding: utf-8 -*-
from PySide6.QtWidgets import (
    QLabel,
    QFrame,
)


class Led:
    """Class Led"""

    def __init__(self, frame):
        self.enabled = False
        self.led = frame
        self.led.setStyleSheet("")
        self.update()

    def update(self):
        if self.enabled:
            self.led.setProperty("class", "led_enabled")
        else:
            self.led.setProperty("class", "led_disabled")

        self.led.style().unpolish(self.led)
        self.led.style().polish(self.led)
        self.led.update()


class Label:
    """Class Label"""

    def __init__(self, frame):
        self.label = frame
        self.label.setStyleSheet("")
        self.label.setProperty("class", "label")
        self.update()

    def update(self):
        self.label.style().unpolish(self.label)
        self.label.style().polish(self.label)
        self.label.update()


class Text(QLabel):
    """Class Text"""

    def __init__(self, frame):
        self.text = frame
        self.text.setStyleSheet("")
        self.text.setProperty("class", "text")
        self.update()

    def update(self):
        self.text.style().unpolish(self.text)
        self.text.style().polish(self.text)
        self.text.update()
