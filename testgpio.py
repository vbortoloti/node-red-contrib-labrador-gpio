from labrador_sdk.gpio import GPIO
from labrador_sdk.main import Labrador
from cgi import test
import time
import sys

try:
    raw_input          # Python 2
except NameError:
    raw_input = input  # Python 3

# def getGpio(pin):
#     if(pin == 3):
#         labrador.gpio3.enable_io(GPIO.Direction.OUTPUT, alias="led_out")
#     elif(pin == 7):
#         labrador.gpio7.enable_io(GPIO.Direction.OUTPUT, alias="led_out")
#     else:
#         labrador.gpio11.enable_io(GPIO.Direction.OUTPUT, alias="led_out") 
    

pin = int(sys.argv[1])
print("led "+str(pin)+" high")
labrador = Labrador()  
labrador.gpio3.enable_io(GPIO.Direction.OUTPUT, alias="led_out")
# getGpio(pin)
print("runnin")

while True:
        print("Led High")
        labrador.led_out.high()
        time.sleep(2)
        labrador.led_out.low()
        print("Led Low")
        time.sleep(2)

