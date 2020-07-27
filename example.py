#                             _____
#      /\                    |  __ \
#     /  \   _ __  _ __   ___| |__) |   _
#    / /\ \ | '_ \| '_ \ / _ \  ___/ | | |
#   / ____ \| | | | | | |  __/ |   | |_| |
#  /_/    \_\_| |_|_| |_|\___|_|    \__, |
#                                    __/ |
#                                   |___/
# Gilberto Charles - 2020
from Annepy import Keeb
import time
b = Keeb() ## Detect and instance your anne pro2 keeb, as easy as that

b.set_multi([[255,0,0],[50,100,0]]) ## will turn on ESC and 1 with diferent colors

time.sleep(2.0) ## durr

b.set_all(100,100,100) ## will turn all leds with only one color
