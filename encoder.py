import caninos_sdk as k9
import time

labrador = k9.Labrador()

labrador.pin3.enable_gpio(k9.Pin.Direction.OUTPUT, alias="inA")
labrador.pin5.enable_gpio(k9.Pin.Direction.OUTPUT, alias="inB")
labrador.pin7.enable_gpio(k9.Pin.Direction.INPUT, alias="encoder")

lastRead= 0
read = 0
count = 0

labrador.inA.high()
labrador.inB.low()

while True:
    read  = labrador.encoder.read()
    if read != lastRead:
        lastRead = read
        print(read)
        count += 1
        print(count)
        if count == 120:
            labrador.inA.low()
            time.sleep(0.5)
            count =0
            labrador.inA.high()


