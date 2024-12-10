#!/usr/bin/env python
""" class allowing to use the joystick version 1 and 2 pmod from digilent with spi protocol.

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
from constants import *


class PmodJstk2:
    """Class for use the Pmod Joystick 2

    Attributes
    ----------
    x : int
        coordinate x joystick
    x_min : int
        coordinate minimum x joystick
    x_max : int
        coordinate maximum x joystick
    x_cen_min : int
        coordinate minimum center x joystick
    x_cen_max : int
        coordinate maximum center x joystick
    y : int
        coordinate y joystick
    y_min : int
        coordinate minimum y joystick
    y_max : int
        coordinate maximum y joystick
    y_cen_min : int
        coordinate minimum center y joystick
    y_cen_max : int
        coordinate maximum center y joystick
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
        Send cmd Joystick
    read_data
        Read data Joystick
    show_data
        Show all data
    initialize
        Send cmd and read the coordinate values
    _extract_values
        Extract the bytes from the data
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
        self.x_min = 0
        self.x_max = 0
        self.y_min = 0
        self.y_max = 0
        self.trigger_joy_select = False
        self.trigger_select = False
        self.spi_cs = spi_cs
        self.spi_max_speed_hz = spi_max_speed_hz
        self.spi = spidev.SpiDev()
        self.spi_standard = True

    def __repr__(self):
        """Show all data"""
        if self.spi_standard:
            return print(self.__dict__)

    def spi_open(self):
        """Open port spi"""
        self.spi.open(0, self.spi_cs)
        self.spi.mode = 0b00
        self.spi.max_speed_hz = self.spi_max_speed_hz

    def spi_close(self):
        """Close port spi"""
        self.spi.close()

    def send_cmd(
        self,
        cmd=CMD_DEFAULT,
        param1=CMD_DEFAULT,
        param2=CMD_DEFAULT,
        param3=CMD_DEFAULT,
        param4=CMD_DEFAULT,
        param5=CMD_DEFAULT,
        param6=CMD_DEFAULT,
    ):
        """Send cmd Joystick

        Parameters
        ----------
        cmd : hex
            cmd to send in hexadecimal, by default CMD_DEFAULT
        param1 : hex, optional
            parameters to be entered if necessary, read the manufacturer's documentation, by default CMD_DEFAULT
        param2 : hex, optional
            parameters to be entered if necessary, read the manufacturer's documentation, by default CMD_DEFAULT
        param3 : hex, optional
            parameters to be entered if necessary, read the manufacturer's documentation, by default CMD_DEFAULT
        param4 : hex, optional
            parameters to be entered if necessary, read the manufacturer's documentation, by default CMD_DEFAULT
        param5 : hex, optional
            parameters to be entered if necessary, read the manufacturer's documentation, by default CMD_DEFAULT

        Returns
        -------
        list
            a list of bytes, 5 for standard and 6 for extender

        """
        try:
            time.sleep(0.25)
            if self.spi_standard:
                list_of_bytes = self.spi.xfer2(
                    cmd + CMD_DEFAULT * 4, 10, self.spi_max_speed_hz
                )
            else:
                list_of_bytes = self.spi.xfer2(
                    cmd + param1 + param2 + param3 + param4 + param5 + param6,
                    10,
                    self.spi_max_speed_hz,
                )

            return list_of_bytes
        except:
            print("Error of read")

    def read_data(self):
        """Read data Joystick

        Returns
        -------
        bool
            Return False if  there was an error

        """
        try:
            recieved_cmd = [0] * 5  # initialize format
            recieved_cmd = self.send_cmd()
            self.x = recieved_cmd[0] + (recieved_cmd[1] << 8)
            self.y = recieved_cmd[2] + (recieved_cmd[3] << 8)
            match recieved_cmd[4]:
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
            return True
        except TypeError as err:
            print("communication with the peripheral is no longer active.", err)
            return False

    def initialize(self):
        """Send cmd and read the coordinate values use only with protocol 2"""
        # try:
        standard_save = self.spi_standard
        self.spi_standard = False
        self.x_min = self._extract_value(self.send_cmd(CMD_GET_CAL_X_MIN), 2)
        self.x_max = self._extract_value(self.send_cmd(CMD_GET_CAL_X_MAX), 2)
        self.x_cen_min = self._extract_value(self.send_cmd(CMD_GET_CAL_X_CEN_MIN), 2)
        self.x_cen_max = self._extract_value(self.send_cmd(CMD_GET_CAL_X_CEN_MAX), 2)
        self.y_min = self._extract_value(self.send_cmd(CMD_GET_CAL_Y_MIN), 2)
        self.y_max = self._extract_value(self.send_cmd(CMD_GET_CAL_Y_MAX), 2)
        self.y_cen_min = self._extract_value(self.send_cmd(CMD_GET_CAL_Y_CEN_MIN), 2)
        self.y_cen_max = self._extract_value(self.send_cmd(CMD_GET_CAL_Y_CEN_MAX), 2)
        self.spi_standard = standard_save

    #     return True
    # except TypeError as err:
    #     print("communication with the peripheral is no longer active.", err)
    #     return False

    def _extract_value(self, data, byte_amount):
        """Extract the bytes from the data

        Pamareters
        ----------
        data : array of byte
            contains the data received by the cmd sent
        byte_amount : int
            number of bytes to extract

        Returns
        -------
        int
            return the value concatenated by the number of bytes put in parameter
        """
        try:
            match byte_amount:
                case 1:
                    return data[5]
                case 2:
                    return data[5] + (data[6] << 8)
                case _:
                    return [0]
        except TypeError as err:
            print("communication with the peripheral is no longer active.", err)


if __name__ == "__main__":
    joy = PmodJstk2()
    joy.spi_open()
    joy.initialize()
    try:
        while joy.read_data():
            print(joy.__dict__)

    finally:
        joy.spi_close()
