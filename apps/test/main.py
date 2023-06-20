import RPi.GPIO as gpio
import time
from signal import signal, SIGINT
from sys import exit
DRIVE_ENABLED = 21
DRIVE_DIR = 22
DRIVE_PULS = 23
 
def handler(signal_received, frame):
    # on gère un cleanup propre
    print('')
    print('SIGINT or CTRL-C detected. Exiting gracefully')
    gpio.cleanup()
    exit(0)
 
def main():
    # GPIO init
    gpio.setmode(gpio.BCM)
    gpio.setup(DRIVE_ENABLED, gpio.OUT)
    gpio.setup(DRIVE_DIR, gpio.OUT)
    gpio.setup(DRIVE_PULS, gpio.OUT)
    
    freq = 200
    drive_enabled = gpio.output(DRIVE_ENABLED, gpio.HIGH)
    drive_dir = gpio.output(DRIVE_DIR, gpio.HIGH)
    drive_puls = gpio.PWM(DRIVE_PULS, freq)
    print(drive_enabled)
    print(drive_dir)
    print(drive_puls)
 
    # cycle = 50%
    drive_puls.start(50)
 
    while 1:
        # Le niveau haut donne l'information au variateur d'arrêter le moteur
        if gpio.input(DRIVE_ENABLED) == 1:
            drive_etat = 'arrêté'
        else :
            drive_etat = 'en marche'
        # sens horaire en niveau haut    
        if gpio.input(DRIVE_DIR) == 1:
            drive_sens = 'sens ->'
        else:
            drive_sens = 'sens <-'
        
        print('Moteur '+ drive_etat +' dans le '+drive_sens + ' à la fréquence : ' + str(freq) + 'Hz')
        print('Moteur 0 (arrêté) 1 (en marche)')
        print('Direction 10 (<-) 11 (->)')
        order = input('Entrez la commande :')
        if order == '0':
            gpio.output(DRIVE_ENABLED, gpio.HIGH)
        elif order == '1':
            gpio.output(DRIVE_ENABLED, gpio.LOW)       
        elif order == '10':
            gpio.output(DRIVE_DIR, gpio.LOW)
        elif order == '11':
            gpio.output(DRIVE_DIR, gpio.HIGH)
        else: 
            print('Commande incorrecte')
        
        print('\n')

 
if __name__ == '__main__':
    # On prévient Python d'utiliser la method handler quand un signal SIGINT est reçu
    signal(SIGINT, handler)
    main()