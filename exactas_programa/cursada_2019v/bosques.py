#!/usr/bin/python3
import sys
import numpy as npy
import random as rnd

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

def iniciar_bosque( nsize ):
    bosque = []
    for idx in range( 1, nsize+1 ):
        bosque.append( 0 )
    return bosque

#------------------------------------------------------------------------------#

def iniciar_probas( nsize, proba ):
    probas = []
    for idx in range( 1, nsize+1 ):
        probas.append( proba )
    return probas

#------------------------------------------------------------------------------#

def contar_casos( lista, tipo ):
    casos = 0
    for elemento in lista:
        if ( elemento == tipo ):
            casos = casos + 1
    return casos

#------------------------------------------------------------------------------#

def aplicar_brotes( bosque, probas ):

    if ( len(bosque) != len(probas) ):
        print( "Bosque y Probas no son compatibles")
        print( " - len(bosque) = ", len(bosque) )
        print( " - len(probas) = ", len(probas) )
        sys.exit( "Abortando" )

    for idx in range( 0, len(bosque) ):
        if ( bosque[idx] == 0 ):
            bosque[idx] = suceso_aleatorio( probas[idx] )
    
    return contar_casos( bosque, 1 )

#------------------------------------------------------------------------------#

def aplicar_rayos( bosque, proba0 ):

    for idx in range( 0, len(bosque) ):
        if ( bosque[idx] == 1 ):
            bosque[idx] = bosque[idx] - 2 * suceso_aleatorio( proba0 )

    return contar_casos( bosque, -1 )

#------------------------------------------------------------------------------#

def aplicar_propagacion( bosque ):

    for idx in range( 0, len(bosque)-1, 1 ):
        if ( (bosque[idx+1]==1) and (bosque[idx]==-1) ):
            bosque[idx+1] = -1

    for idx in range( len(bosque)-1, 0, -1 ):
        if ( (bosque[idx-1]==1) and (bosque[idx]==-1) ):
            bosque[idx-1] = -1

    return contar_casos( bosque, -1 )

#------------------------------------------------------------------------------#

def aplicar_limpieza( bosque ):

    for idx in range( 0, len(bosque) ):
        if ( bosque[idx] == -1 ):
            bosque[idx] = 0

    return contar_casos( bosque, 1 )

#------------------------------------------------------------------------------#

def actualiza_probas( bosque, probas, step_u, step_d ):

    for idx in range( 0, len(bosque) ):
        if ( bosque[idx] == 1 ):
            probas[idx] = probas[idx] + step_u
        elif ( bosque[idx] == -1 ):
            probas[idx] = probas[idx] - step_d

        if ( probas[idx] < 0.0 ):
            probas[idx] == 0.01

    return contar_casos( bosque, 1 )

#------------------------------------------------------------------------------#

def promedio_en_anios( nsize, nreps, proba_b, proba_r ):

    mibosque = iniciar_bosque( nsize )
    miprobas = iniciar_probas( nsize, proba_b )
    promedio = 0

    for idx in range( 0, nreps ):
        arboles  = aplicar_brotes( mibosque, miprobas )
        fuegos   = aplicar_rayos( mibosque, proba_r )
        fuegos   = aplicar_propagacion( mibosque )
        arboles  = actualiza_probas( mibosque, miprobas, 0.05, 0.05 )
        arboles  = aplicar_limpieza( mibosque )
        promedio = promedio + float(arboles) / float( nreps )

    return promedio

#------------------------------------------------------------------------------#

def optimiza_p( nsize, nreps, ndivs, proba_r ):

    incremento = 1/float(ndivs)
    p_actual   = 0.0
    lista_prom = []

    for step in range(1, ndivs+1):
        p_actual = p_actual + incremento
        promedio = promedio_en_anios( nsize, nreps, p_actual, proba_r )
        lista_prom.append(promedio)

    return lista_prom

################################################################################
# PROCEDIMIENTOS
#------------------------------------------------------------------------------#

promedio = promedio_en_anios( 100, 50, 0.2, 0.02 )
print( promedio )

lista_promedios = optimiza_p( 100, 50, 20, 0.02 )
print( lista_promedios )
print( lista_promedios.index(max(lista_promedios)), max(lista_promedios))

################################################################################
