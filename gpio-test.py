
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

if mode == "out":
    getGpio(labrador,pin)
    data = False
    while True:
            time.sleep(0.2)
            data = not data
            if(data == 1):
                print("Led High")
                labrador.led_out.high()
            elif(data ==0):
                print("Led Low")
                labrador.led_out.low()
            else:
                print('invalid input')
                sys.exit(0)
                break

            print("saida: "+str(data))

elif mode == "pwm":
    getGpioPwm(labrador,pin)
    labrador.pwm_out.pwm.stop()
    running = False
    data = False
    while True:
            time.sleep(0.2)
            data = not data
            if(data == 1):
                print("Led High")
                if not running:
                    labrador.pwm_out.pwm.start()
                    running = True
            elif(data ==0):
                print("Led Low")
                if running:
                    labrador.pwm_out.pwm.stop()
                    running = False
            else:
                print('invalid input')
                labrador.pwm_out.pwm.stop()
                running = False
                sys.exit(0)
                break

            print("saida: "+str(data))