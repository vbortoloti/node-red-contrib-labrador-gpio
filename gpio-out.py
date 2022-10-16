
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
        pin.enable_gpio(k9.Pin.Direction.OUTPUT, alias="led_out")

pin = int(sys.argv[1])
print("led "+str(pin)+" high")

labrador = k9.Labrador()   
getGpio(labrador,pin)
print("running")

while True:
        try:
            data = raw_input()
            if 'close' in data:
                sys.exit(0)
            data = int(data)
        except (EOFError, SystemExit):        # hopefully always caused by us sigint'ing the program
            print("erro")
            sys.exit(0)

        if(data == 1):
            print("Led High")
            labrador.led_out.high()
        elif(data ==0):
            print("Led Low")
            labrador.led_out.low()
        else:
            print('invalid input')
            break

        print("saida: "+str(data))
