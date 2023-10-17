""" class allowing to use modbusTcP for display INL35SSI and encoder baumer G0M2H-112A102.

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
__date__ = "2023/10/12"
__deprecated__ = False
__email__ = "tmangear@insa-toulouse.fr"
__license__ = "GPLv3"
__maintainer__ = "developer"
__status__ = "Production"
__version__ = "0.0.1"

from pymodbus.client import ModbusTcpClient  # Pour le client Modbus TCP
from pymodbus.exceptions import ConnectionException
import struct


class Encoder:

    """class for use modbusTCp with encoder display

    Attributes
    ----------

    ip : string
    port : int
    state : int
    display_value : float
    display_value_lsb : int
    display_value_msb : int
    out_value : float
    out_value_lsb : int
    out_value_msb : int
    raw_value : int
    raw_value_lsb : int
    raw_value_msb : int

    Methods
    -------
    close
        close the communicaztion modbuTCP
    read
        read the data of the encoder display

    """

    def __init__(self, ip) -> None:
        self.ip = ip
        self.port = 502
        self.state = 0
        self.display_value = 0.0
        self.display_value_lsb = 0
        self.display_value_msb = 0
        self.out_value = 0.0
        self.out_value_lsb = 0
        self.out_value_msb = 0
        self.raw_value = 0
        self.raw_value_lsb = 0
        self.raw_value_msb = 0
        try:
            self.client = ModbusTcpClient(self.ip)
            self.client.connect()
        except ConnectionException as e:
            print("Erreur de connexion : ", str(e))

    def close(self):
        """close the communication modbusTCP"""
        self.client.close()

    def read(self):
        """Read the data of encoder diplay
        Send read code 0x03
        """
        response = self.client.read_input_registers(
            0, 8
        )  # Lire 8 registres d'entrée à partir de l'adresse 0
        if response.isError():
            print("Erreur de lecture des registres d'entrée : ", response)
        else:
            self.etat = response.registers[0]
            self.display_value_msb = response.registers[1]
            self.display_value_lsb = response.registers[2]
            self.display_value = self._convert_2word_to_32float(
                self.display_value_lsb, self.display_value_msb
            )
            self.out_value_msb = response.registers[3]
            self.out_value_lsb = response.registers[4]
            self.out_value = self._convert_2word_to_32float(
                self.out_value_lsb, self.out_value_msb
            )
            self.raw_value_msb = response.registers[6]
            self.raw_value_lsb = response.registers[7]
            self.raw_value = self._convert_2word_to_32int(
                encoder.raw_value_lsb, encoder.raw_value_msb
            )

    def _convert_2word_to_32float(self, lsb, msb):
        """convert 2 word IEEE 754 to float

        Parameters
        ----------
        lsb : int
            low weight
        msb : int
            high weight

        Returns
        -------
        float
            value convert
        """
        value = (msb << 16) + lsb
        f = int(str(bin(value)[2:]), 2)
        value_convert = struct.unpack("f", struct.pack("I", f))[0]
        return value_convert

    def _convert_2word_to_32int(self, lsb, msb):
        """convert 2 word to int 32 bits unsigned

        Parameters
        ----------
        lsb : int
            low weight
        msb : int
            high weight

        Returns
        -------
        int
            value convert
        """
        value = (msb << 16) + lsb

        return value


if __name__ == "__main__":
    ip = input("insert IP:")
    encoder = Encoder(ip)
    encoder.read()
    print(encoder.__dict__)
