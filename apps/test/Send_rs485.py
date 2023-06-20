import RPi.GPIO as GPIO
import spidev
import serial
import time


CS_PIN = 17
RST_PIN = 18
CLOCK = 27

# Configuration de la communication SPI
# spi = spidev.SpiDev()
# spi.open(0, 0)
# spi.max_speed_hz = 1000

# Configuration de la broche SYNC
GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)
GPIO.setup(CLOCK, GPIO.OUT)
GPIO.setup(CS_PIN, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(RST_PIN, GPIO.OUT, initial=GPIO.LOW)

# Génération du signal SYNC
# GPIO.output(27, GPIO.LOW)
# time.sleep(0.0001)
# GPIO.output(27, GPIO.HIGH)
# time.sleep(0.0001)

pwm = GPIO.PWM(27, 1000)  # Fréquence de 1 kHz
pwm.start(50)
cpt = 0

while True:
    # Activation de la ligne de sélection du capteur SSI
    GPIO.output(CS_PIN, GPIO.HIGH)
    GPIO.output(RST_PIN, GPIO.LOW)  # Activation du mode lecture

    # Envoi d'une commande de lecture SSI
    # command = [0x00, 0x00, 0x00, 0x00]
    # response = spi.xfer2(command)

    # Traitement de la réponse SSI
    # Ouverture du port série
    ser = serial.Serial("/dev/serial0", 9600)
    # Envoi des données

    data = "Hello"

    # Affichage des données lues
    cpt += 1
    ser.write(data.encode("Ascii"))

    # Fermeture de la communication SPI
    # spi.close()
    # Fermeture de la communication Serie
    ser.close()

    # Désactivation de la broche SYNC
    # Désactivation de la ligne de sélection du capteur SSI
    GPIO.output(CS_PIN, GPIO.LOW)

    # Attente pour atteindre la fréquence de lecture désirée (1000 Hz)
    # time.sleep(1)


GPIO.output(CLOCK, GPIO.LOW)
GPIO.output(CS_PIN, GPIO.LOW)
GPIO.output(RST_PIN, GPIO.LOW)
GPIO.cleanup()
print("fin")
