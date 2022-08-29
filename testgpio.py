
# Import library functions we need
#import RPi.GPIO as GPIO
import sys
from time import sleep

#PEGA ENTRADA
try:
    raw_input          # Python 2
except NameError:
    raw_input = input  # Python 3

bounce = 25

if len(sys.argv) > 2:
    cmd = sys.argv[1].lower()
    pin = int(sys.argv[2])
    #GPIO.setmode(GPIO.BCM)
    #GPIO.setwarnings(False)

    if cmd == "pwm":
        print("Initialised pin "+str(pin)+" to PWM")
        try:
            freq = int(sys.argv[3])
        except:
            freq = 100

        #GPIO.setup(pin,GPIO.OUT)
        #p = GPIO.PWM(pin, freq)
        #p.start(0)

        """ while True:
            try:
                data = raw_input()
                if 'close' in data:
                    sys.exit(0)
                #p.ChangeDutyCycle(float(data))
            except (EOFError, SystemExit):        # hopefully always caused by us sigint'ing the program
                #GPIO.cleanup(pin)
                sys.exit(0)
            except Exception as ex:
                print("bad data: "+data) """

    elif cmd == "out":
        print("Initialised pin "+str(pin)+" to OUT")
        #GPIO.setup(pin,GPIO.OUT)
        if len(sys.argv) == 4:
            print("Print top")
            #GPIO.output(pin,int(sys.argv[3]))

        """ while True:
            try:
                data = raw_input()
                if 'close' in data:
                    sys.exit(0)
                data = int(data)
            except (EOFError, SystemExit):        # hopefully always caused by us sigint'ing the program
                #GPIO.cleanup(pin)
                sys.exit(0)
            except:
                if len(sys.argv) == 4:
                   data = int(sys.argv[3])
                else:
                   data = 0
            if data != 0:
                data = 1
            #GPIO.output(pin,data) """
else:
    print("Bad parameters - in|out|pwm|buzz|byte|borg|mouse|kbd|ver|info {pin} {value|up|down}")