#!/usr/bin/env python
""" class allowing to use the joystick version 1 and 2 pmod from digilent.

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.
This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
"""

__author__ = "Tristan Mangeard"
__contact__ = "tmangear@insa-toulouse.fr"
__copyright__ = "Copyright 2023, ICA"
__credits__ = ["Tristan Mangeard"]
__date__ = "2023/07/10"
__deprecated__ = False
__email__ = "tmangear@insa-toulouse.fr"
__license__ = "GPLv3"
__maintainer__ = "developer"
__status__ = "Production"
__version__ = "0.0.1"


import spidev
import time


class PmodJstk2:
    """Class for use the Pmod Joystick 2

    Attributes
    ----------
    x : int
        coordinate x joystick
    y : int
        coordinate y joystick
    trigger_joy_select : bool
        value click button on joystick
    trigger_select : bool
        value click button under joystick
    spi_cs : bool, optional
        specified port Gpio select
    spi_max_speed_hz : float, optional
        value max speed communication protocol spi
    spi : object
        objectspi for library spidev
    spi_standard : bool
        select version frame communication


    Methods
    -------
    spi_open
        Open port spi
    spi_close
        Close port spi
    send
        Send command Joystick
    read_data
        Read data Joystick
    show_data
        Show all data
    """

    def __init__(self, spi_cs=0, spi_max_speed_hz=115200):
        """Constructor

        Parameters
        ----------
        spi_cs : int, optional
            specified port Gpio select, by default 0
        spi_max_speed_hz : int, optional
            value max speed communication protocol spi, by default 115200
        """

        self.x = 0
        self.y = 0
        self.trigger_joy_select = False
        self.trigger_select = False
        self.spi_cs = spi_cs
        self.spi_max_speed_hz = spi_max_speed_hz
        self.spi = spidev.SpiDev()
        self.spi_standard = True

    def spi_open(self):
        """Open port spi"""
        self.spi.open(0, self.spi_cs)
        self.spi.mode = 0b00
        self.spi.max_speed_hz = self.spi_max_speed_hz

    def spi_close(self):
        """Close port spi"""
        self.spi.close()

    def send(
        self,
        command=[0x00],
        param1=[0x00],
        param2=[0x00],
        param3=[0x00],
        param4=[0x00],
        param5=[0x00],
    ):
        """Send command Joystick"""
        try:
            time.sleep(0.25)
            if self.spi_standard:
                list_of_bytes = self.spi.xfer2(
                    command + [0x00] * 4, 10, self.spi_max_speed_hz
                )
            else:
                list_of_bytes = self.spi.xfer2(
                    command + param1 + param2 + param3 + param4 + param5,
                    10,
                    self.spi_max_speed_hz,
                )

            return list_of_bytes
        except:
            print("Error of read")

    def read_data(self):
        """Read data Joystick"""
        recieved_message = [0] * 5  # initialize format
        recieved_message = self.send()
        self.x = recieved_message[0] + (recieved_message[1] << 8)
        self.y = recieved_message[2] + (recieved_message[3] << 8)
        match recieved_message[4]:
            case 0:
                self.trigger_joy_select = False
                self.trigger_select = False
            case 1:
                self.trigger_joy_select = True
                self.trigger_select = False
            case 2:
                self.trigger_joy_select = False
                self.trigger_select = True
            case 3:
                self.trigger_joy_select = True
                self.trigger_select = True

    def show_data(self):
        """Show all data"""
        if self.spi_standard:
            print(
                "X="
                + str(self.x)
                + " Y="
                + str(self.y)
                + " trigger joy="
                + str(self.trigger_joy_select)
                + " trigger="
                + str(self.trigger_select)
            )


if __name__ == "__main__":
    joy = PmodJstk2()
    joy.spi_open()
    try:
        while True:
            joy.read_data()
            joy.show_data()
    finally:
        joy.spi_close()
