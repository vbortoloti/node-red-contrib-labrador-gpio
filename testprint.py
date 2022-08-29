from labrador_sdk.gpio import GPIO
from labrador_sdk.main import Labrador
import time


labrador = Labrador("64", kernel_version=">=4.19.98")
labrador.gpio3.enable_io(GPIO.Direction.OUTPUT, alias="led_status")
print("running")
while True:
    labrador.led_status.high()
    time.sleep(0.5)
    labrador.led_status.low()
    time.sleep(0.5)
