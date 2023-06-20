import RPi.GPIO as GPIO

CS_PIN = 17
RST_PIN = 18
CLOCK = 27

# Configuration de la broche SYNC
GPIO.setmode(GPIO.BCM)

GPIO.setup(CLOCK, GPIO.OUT)
GPIO.setup(CS_PIN, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(RST_PIN, GPIO.OUT, initial=GPIO.LOW)

GPIO.output(CLOCK, GPIO.LOW)
GPIO.output(CS_PIN, GPIO.LOW)
GPIO.output(RST_PIN, GPIO.LOW)
GPIO.cleanup()

print('fin')
