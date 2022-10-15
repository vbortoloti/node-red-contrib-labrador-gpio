import caninos_sdk as k9

# instancia o objeto labrador
labrador = k9.Labrador()

# habilita o pino 15 como saída, e dá a ele o apelido "led_status"
labrador.pin3.enable_gpio(k9.Pin.Direction.OUTPUT, alias="led_status")

# liga o "led_status"
labrador.led_status.high()
# desliga o "led_status"
labrador.led_status.low()
# liga o mesmo led de novo, porém agora se referindo a ele pelo número do pino
labrador.pin3.high()