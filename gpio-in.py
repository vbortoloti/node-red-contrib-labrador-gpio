
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
        pin.enable_gpio(k9.Pin.Direction.INPUT, alias="led_in")

pin = int(sys.argv[1])

print("led "+str(pin)+" high")

labrador = k9.Labrador()
getGpio(labrador,pin)
print("running")

lastRead  = labrador.encoder.read()
while True:
    read  = labrador.encoder.read()
     if read != lastRead:
        lastRead = read
        print(read)
        count += 1
        print(count)
    sleep(0.01)



