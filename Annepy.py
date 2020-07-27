#                             _____
#      /\                    |  __ \
#     /  \   _ __  _ __   ___| |__) |   _
#    / /\ \ | '_ \| '_ \ / _ \  ___/ | | |
#   / ____ \| | | | | | |  __/ |   | |_| |
#  /_/    \_\_| |_|_| |_|\___|_|    \__, |
#                                    __/ |
#                                   |___/
# Gilberto Charles - 2020
from easyhid import Enumeration
import math
from time import sleep
import itertools
from utils import ANNE_LAYOUT


class Keeb(object):
    def __init__(self):
        self._MCU_ADRESS = 65
        self._SERVICE_DATA = [0, 123, 16, self._MCU_ADRESS]
        self._STATIC_MESSAGE = [0, 0, 125]
        self._COMMAND_INFO = [32, 3, 255]
        self._PIDS = [0x8008, 0x8009, 0xa292, 0xa293]
        self._VID = 0x04d9
        self._en = Enumeration()
        self._keeb = None
        _d = self._detect()
        if _d[0] == 1:
            print(_d[1])
            exit()
        else:
            print(_d[1])

    def _detect(self):
        for pid in self._PIDS:
            try:
                devices = self._en.find(vid=self._VID, pid=pid, interface=1)
                self._keeb = devices[0]

                info = (
                    f'\nDevice manufacturer: {self._keeb.manufacturer_string}'
                    f'\n\nProduct: {self._keeb.product_string}\n'
                    f'\nSerial Number: {self._keeb.serial_number}\n'
                )

                return [0, info]
            except:
                pass
        return [1, "\nNo AnnePro2 keeb found\n"]

    def set_all(self, r: int, g: int, b: int):
        """
        Sets all keys to one same color.

        It expects 3 positional arguments to a RGB color.

        Example : set_all(255,255,255)
        """
        try:
            rgb = [r, g, b]
            message = self._SERVICE_DATA + \
                [16] + [7] + self._STATIC_MESSAGE + \
                self._COMMAND_INFO + [1] + rgb
            self._keeb.open()
            self._keeb.write(message)
            self._keeb.close()
        except:
            print(self._warning("ERROR: Verify your RGB format\n"))

    def _generate_multi_color(self,arrayOfRgbValues: list):
        hid_command = []
        real_command_info_length = len(self._COMMAND_INFO) + 1
        maxMessageLength = 55 - real_command_info_length
        messagesToSendAmount = math.ceil(
            len(arrayOfRgbValues) / maxMessageLength)
        val_1 = len(arrayOfRgbValues) % maxMessageLength
        val_2 = maxMessageLength if val_1 == 0 else val_1
        arrayOfRgbValuesCopy = arrayOfRgbValues.copy()
        for i in range(0, messagesToSendAmount):
            rgb = arrayOfRgbValuesCopy[:maxMessageLength]
            arrayOfRgbValuesCopy = arrayOfRgbValuesCopy[maxMessageLength:]
            e = (messagesToSendAmount << 4) + i
            a = (val_2 + real_command_info_length) if messagesToSendAmount - \
                1 == i else (maxMessageLength + real_command_info_length)
            message = self._SERVICE_DATA + \
                [e] + [a] + self._STATIC_MESSAGE + self._COMMAND_INFO + \
                [2] + rgb
            hid_command.append(message)
        return hid_command
    
    def set_multi(self, rgb: list):
        """
        Receives a bi-dimensional array of sequencial RGB values
        corresponding to keys left to right.

        Example: set_multi([  [255,0,0], [0,100,0], ... [100,100,100] ])
        The fisrt item being ESC key, second being 1 key, last being right control key.
        """

        black = [0,0,0]
        rgb_matrix = []
        for key in ANNE_LAYOUT:
            if ANNE_LAYOUT.get(key) is None:
                rgb_matrix += black
            else:
                try:
                    rgb_matrix += rgb[ANNE_LAYOUT.get(key)]
                except :
                    rgb_matrix += black

        hid_command = self._generate_multi_color(rgb_matrix)
        self._keeb.open()
        for command in hid_command:
            self._keeb.write(command)
            sleep(0.05)
        self._keeb.close()


    def _warning(self, str):
        return '\033[91m' + str + '\033[0m'
