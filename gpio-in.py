
import caninos_sdk as k9
from cgi import test
import time
import sys

try:
    raw_input          # Python 2
except NameError:
    raw_input = input  # Python 3

def getGpio(labrador, pin_to_enable):
    pin_to_enable = f"pin{pin_to_enable}"
    if hasattr(labrador, pin_to_enable):
        pin = getattr(labrador, pin_to_enable)
        pin.enable_gpio(k9.Pin.Direction.INPUT, alias="input")

pin = int(sys.argv[1])


labrador = k9.Labrador()
getGpio(labrador,pin)

lastRead  = labrador.input.read()
print(lastRead)

while True:
    read  = labrador.input.read()
    if read != lastRead:
        lastRead = read
        print(read)
        
    time.sleep(0.01)



