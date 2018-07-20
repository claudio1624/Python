#! /usr/bin/python
# -*- coding: iso-8859-15 -*-

from random import *

n = int(input('Ingrese cantidad de notas a sacar promedio: '))
sum = 0
for i in range(n):
    x = float(input('ingrese nota : '))
    sum = x + sum
    p = sum / n
print('EL PROMEDIO ES.   :' ,p)




