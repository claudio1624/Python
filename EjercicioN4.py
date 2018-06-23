#! /usr/bin/python
# -*- coding: iso-8859-15 -*-
import os, sys
llamada = int(input('Duracion de llamada :'))
corta = 100
larga = 100 + (100*0.05)
if llamada < 10:
    print'LA LLAMADA SE CONSIDERA CORTA'
    print'EL VALOR ES DE:   ', corta
else:
    print'LA LLAMADA ES LARGA'
    print'TIENE UN CARGO ADICIONAL DE 5% ES DE :  ',larga
