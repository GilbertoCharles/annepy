# AnnePy

AnnePy is a reverse engineered python module to help you create scritps to remote control the lights on your OBINS Anne Pro 2 Keeb.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies

```bash
pip install -r requirements.txt
```

## Usage

```python
from Annepy import Keeb
import time
b = Keeb() ## Detect and instance your anne pro2 keeb, as easy as that

b.set_multi([[255,0,0],[50,100,0]]) ## will turn on ESC and 1 with diferent colors

time.sleep(2.0) ## durr

b.set_all(100,100,100) ## will turn all leds with only one color
```

## TODO
Create a method to set single or multi keys by name.



## License
[GNU-GPL3](https://choosealicense.com/licenses/gpl-3.0/)