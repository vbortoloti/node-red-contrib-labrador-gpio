
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

def getGpioPwm(labrador, pin_to_enable):
    pin_to_enable = f"pin{pin_to_enable}"
    if hasattr(labrador, pin_to_enable):
        pin = getattr(labrador, pin_to_enable)
        pin.enable_pwm(alias="pwm_out", freq=frequency, duty_cycle=duty/100)

pin = int(sys.argv[1])
mode = str(sys.argv[2])
frequency = int(sys.argv[3])
duty = int(sys.argv[4])

# init_state = int(sys.argv[4])
# begin_with_init_state = str(sys.argv[5])

print("led "+str(pin)+" high")
print("led "+str(pin)+" high")

labrador = k9.Labrador()   

print("running")

if mode == "pwm":
    getGpioPwm(labrador,pin)
    running = False
    data = False
    while True:
            time.sleep(0.25)
            data = not data
            if(data == 1):
                if not running:
                    running = True
                    labrador.pwm_out.pwm.start()
            elif(data ==0):
                if running:
                    running = False
                    labrador.pwm_out.pwm.stop()
            else:
                print('invalid input')
                labrador.pwm_out.pwm.stop()
                running = False
                sys.exit(0)
                break
            print("saida: "+str(data))