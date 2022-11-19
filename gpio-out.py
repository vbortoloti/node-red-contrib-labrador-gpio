
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

# if(begin_with_init_state == "true"):
#     if(init_state == 1):
#         print("Led High")
#         labrador.led_out.high()

print("running")

if mode == "out":
    getGpio(labrador,pin)
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
                sys.exit(0)
                break

            print("saida: "+str(data))

elif mode == "pwm":
    getGpioPwm(labrador,pin)
    labrador.pwm_out.pwm.stop()
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
                labrador.pwm_out.pwm.start()
                time.sleep(0.25)
            elif(data ==0):
                print("Led Low")
                labrador.pwm_out.pwm.stop()
                time.sleep(0.25)

            else:
                print('invalid input')
                sys.exit(0)
                break

            print("saida: "+str(data))