#                             _____       
#      /\                    |  __ \      
#     /  \   _ __  _ __   ___| |__) |   _ 
#    / /\ \ | '_ \| '_ \ / _ \  ___/ | | |
#   / ____ \| | | | | | |  __/ |   | |_| |
#  /_/    \_\_| |_|_| |_|\___|_|    \__, |
#                                    __/ |
#                                   |___/ 
# Gilberto Charles - 2020
import sys
from src.detect import detect

def annepy(argv):
    options = ["detect"]
    default = """
    Welcome to annepy, a Python module to controll your AnnePro2 keeb
    Commands: 
        detect: detect a connected AnnePro2 keeb
    """
    if len(argv) > 1 or len(argv) == 0:
        print(default)
    elif argv[0] not in options:
        print(default)
    else:
        keeb = detect()
        print(keeb[0])


if __name__ == "__main__":
    annepy(sys.argv[1:])




