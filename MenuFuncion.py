#! /usr/bin/python
# -*- coding: iso-8859-15 -*-
from random import *

def menu():
    print('1. Primera opcion')
    print('2. Segunda opcion')
    print('3. Tercera opcion')
    print('4. cuarta opcion')
while True:
    menu()
    opcionMenu = input('Inserte opcion')
    if opcionMenu == 1:
       print" "
       print("Has pulsado la opcion 1. Pulsa una tecla para continuar")  
       print" "
       menu()
    elif opcionMenu == 2:
        print" "
        
    elif opcionMenu == 3:
        print" "
    else:
        print""
        print("LA OPCION INGRESADA NO ES VALIDA")
        print""