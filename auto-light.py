import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

led = 26
GPIO.setup(led, GPIO.OUT)

led_li = 6
GPIO.setup(led_li, GPIO.IN)

while True:
    GPIO.output(led, not GPIO.input(led_li))
    