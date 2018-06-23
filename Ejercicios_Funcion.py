#! /usr/bin/python
# -*- coding: iso-8859-15 -*-
import os, sys

def funcion(x):
    y = 2*x**2+1
    return y
def cuadrado(L):
    Area = L**2
    return Area
def area_triangulo(a,b,c):
    perimetro = a+b+c
    return perimetro
def rectangulo(A,H):
    Area = A*H
    return Area
print''
print'F U N C I O N '
for i in range(3):
    y = funcion(i)
    print(i,y)
print''
print'A R E A'
b=10
c=15
for i in range(5):
    y = area_triangulo(i,b,c)
    print(i,y)
print''
print'C U A D R A D O '
for i in range(3):
    y = cuadrado(i)
    print(i,y)
print''
print'R E C T A N G U L O'
H=4
for i in range(5):
    y = rectangulo(i,H)
    print(i,y)

