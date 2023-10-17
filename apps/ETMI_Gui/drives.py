import RPi.GPIO as gpio
import json
from pathlib import Path

DRIVE_ENABLED = gpio.HIGH
DRIVE_DISABLED = gpio.LOW
CLOCKWISE = gpio.HIGH
DIR_POSITIF = gpio.HIGH
DIR_NEGATIF = gpio.LOW

DUTY_CYCLE = 50

path_config = Path("./config_drives.json")
drives_infos = [
    {"pin_clk": "12", "pin_dir": "5", "pin_en": "6", "freq": "10"},
    {"pin_clk": "19", "pin_dir": "20", "pin_en": "21", "freq": "10"},
    {"pin_clk": "18", "pin_dir": "22", "pin_en": "23", "freq": "10"},
    {"pin_clk": "13", "pin_dir": "24", "pin_en": "25", "freq": "10"},
]


class Drive:
    """Class Drive"""

    def __init__(self, pin_clk, pin_dir, pin_en, frequency):
        self.pin_dir = int(pin_dir)
        self.pin_en = int(pin_en)
        self.pin_clk = int(pin_clk)
        gpio.setup(self.pin_dir, gpio.OUT, initial=gpio.HIGH)
        gpio.setup(self.pin_en, gpio.OUT, initial=DRIVE_DISABLED)
        gpio.setup(self.pin_clk, gpio.OUT, initial=gpio.LOW)
        self.enabled = DRIVE_DISABLED
        self.frequency = int(frequency)
        self.counter_pulse = 0
        self.pulse = gpio.PWM(self.pin_clk, self.frequency)

    def start(self, dir):
        self.set_dir(dir)
        self.enabled = DRIVE_ENABLED
        self.set_frequency(self.frequency)
        self.pulse.start(DUTY_CYCLE)
        gpio.output(self.pin_en, DRIVE_ENABLED)

    def stop(self):
        self.enabled = DRIVE_DISABLED
        gpio.output(self.pin_en, DRIVE_DISABLED)
        self.pulse.stop()

    def set_dir(self, dir):
        gpio.output(self.pin_dir, dir)

    def set_frequency(self, freq):
        self.freqeuncy = freq
        self.pulse.ChangeFrequency(freq)


class ManageDrives:
    """Class Manager Drives"""

    def __init__(self):
        self.clk_common = False
        self.drives = []
        # GPIO init
        gpio.setmode(gpio.BCM)
        # initialize parameters drive
        for drive in drives_infos:
            self.drives.append(
                Drive(
                    drive["pin_clk"], drive["pin_dir"], drive["pin_en"], drive["freq"]
                )
            )

    def start_clock(self):
        if self.clk_common:
            self.drives[0].pulse.start(DUTY_CYCLE)
        else:
            for drive in self.drives:
                drive.pulse.start(DUTY_CYCLE)

    def stop_clock(self):
        if self.clk_common:
            self.drives[0].pulse.stop(DUTY_CYCLE)
        else:
            for drive in self.drives:
                drive.pulse.stop(DUTY_CYCLE)

    def update_clock(self):
        self.stop_clock()
        for drive in self.drives:
            drive.clk = self.freq
        self.start_clock()

    def start_drives(self):
        for drive in self.drives:
            drive.start()

    def stop_drives(self):
        for drive in self.drives:
            drive.stop()

    def gpio_clean(self):
        self.stop_drives()
        gpio.cleanup()


def config():
    global drives_infos
    if path_config.is_file():
        with open(path_config, "r") as jsonfile:
            drives_infos = json.load(jsonfile)
    else:
        with open(path_config, "w") as jsonfile:
            json.dump(drives_infos, jsonfile)
