#! /usr/bin/python
# -*- coding: iso-8859-15 -*-
import os, sys
n1 = float(input('Ingrese primer numero :'))
n2 = float(input('Ingrese segundo numero : '))
print""
suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
divi = n1 / n2
print'La suma es:  ',suma  
if suma < 20:
    print'AZUL'
    print""
elif suma < 40:
    print'ROJO'
    print""
elif suma < 60:
    print'NEGRO'
    print""
print'La resta es:   ',resta
print'La multiplicacion es:   ',multi
print'La division es:  ',divi
