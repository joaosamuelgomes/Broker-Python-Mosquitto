# encoding: utf-8

import paho.mqtt.client as mqtt
import os
import time

from random import randint
from time import sleep
 
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
 
def main():
    cls()
     
    print("     MQTT - Broker Mosquitto - Python    ")
    print('')
    print('Simulador Sensor de temperatura (Publish)')
    print('')
    print('')
    ip = input('Informe o ip do Broker: ')
    print('')
    lugar = input('Informe em qual lugar na cidade o sensor se encontra: ')
    print('')
 
    topico = "cidade/%s/temperatura" %(lugar)
 
    client = mqtt.Client("C" + str(time.time()))
    client.connect(ip, 1883)
 
    for x in range(0, 25):
        temp = randint(0, 50)
        client.publish(topico, temp)
 
        print(topico + " " + str(temp))
         
        sleep(2)

    client.disconnect()
     
main()
