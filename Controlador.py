import pyfirmata2 as pyfirmata

puerto='COM4'

cod_arduino=pyfirmata.Arduino(puerto)


led_1=cod_arduino.get_pin('d:8:o')
led_2=cod_arduino.get_pin('d:9:o')
led_3=cod_arduino.get_pin('d:10:o')
led_4=cod_arduino.get_pin('d:11:o')
led_5=cod_arduino.get_pin('d:12:o')

def led(dedosArriba):
    if dedosArriba==[0,0,0,0,0]:
        led_1.write(0)
        led_2.write(0)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)

    elif dedosArriba==[1,0,0,0,0]:
        led_1.write(1)
        led_2.write(0)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)
    elif dedosArriba==[1,1,0,0,0]:
        led_1.write(1)
        led_2.write(1)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)    
    elif dedosArriba==[1,1,1,0,0]:
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(0)
        led_5.write(0)
    elif dedosArriba==[1,1,1,1,0]:
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(1)
        led_5.write(0)
    elif dedosArriba==[1,1,1,1,1]:
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(1)
        led_5.write(1)