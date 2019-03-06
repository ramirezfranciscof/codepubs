#!/usr/bin/python3
import sys
import numpy as npy
import random as rnd
import matplotlib.pyplot as plt

################################################################################
# FUNCIONES
#------------------------------------------------------------------------------#

def suceso_aleatorio( proba ):
    tirada = rnd.random()
    if ( tirada < proba ):
        resultado = 1
    else:
        resultado = 0
    return resultado

#------------------------------------------------------------------------------#

def proxima_posicion( pos_ahora, pos_antes, fuerza, masa, dt ):
    pos_next = 2 * pos_ahora - pos_antes + (fuerza / masa) * dt * dt
    return pos_next

#------------------------------------------------------------------------------#

def lanzamiento_vertical( y0, y1, dt, pasos_total):

    g0 = 9.8
    tiempos = [ 0.0, dt ]
    alturas = [ y0, y1 ]

    for step in range(1, pasos_total):
        tiempo_antes = tiempos[step-1]
        altura_antes = alturas[step-1]

        tiempo_ahora = tiempos[step]
        altura_ahora = alturas[step]

        tiempo_nuevo = tiempo_ahora + dt
        altura_nueva = proxima_posicion( altura_ahora, altura_antes, -g0, 1.0, dt )

        tiempos.append( tiempo_nuevo )
        alturas.append( altura_nueva )


    plt.title("Posicion del objeto")
    plt.plot(tiempos, alturas, 'r')
    plt.xlabel('tiempo (s)')
    plt.ylabel('altura (m)')
    plt.show()

    return True

################################################################################
# PROCEDIMIENTOS
#------------------------------------------------------------------------------#

lanzamiento_vertical( 0.0, 3.0   ,  0.01 , 10000 )
lanzamiento_vertical( 0.0, 30.0  ,  0.1  , 1000 )
lanzamiento_vertical( 0.0, 300.0 ,  1.0  , 100 )
lanzamiento_vertical( 0.0, 3000.0, 10.0  , 10 )
lanzamiento_vertical( 0.0, 6000.0, 20.0  , 5 )

################################################################################
