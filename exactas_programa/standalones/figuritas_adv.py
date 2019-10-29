#!/usr/bin/python3
import sys
import numpy as npy
import random as rnd

################################################################################
# FUNCIONES
#------------------------------------------------------------------------------#

def generar_paquete_conrep( pack_size, lista_figs ):

    paquete_out = []
    numeros_posibles = len(lista_figs) - 1

    for i_rep in range( 1, pack_size+1 ):
        numero_sorteado = rnd.randint( 0, numeros_posibles )
        esta_figu = lista_figs[numero_sorteado]
        paquete_out.append( esta_figu )

    return paquete_out

#------------------------------------------------------------------------------#

def generar_paquete_sinrep( pack_size, lista_figs ):

    numeros_posibles = len(lista_figs) - 1

    if ( pack_size > numeros_posibles + 1 ):
        print( "Queres más figus de las que hay!")
        print( " - numeros_posibles = ", numeros_posibles )
        print( " -        pack_size = ", pack_size )
        sys.exit( "Abortando" )

    paquete_out = []
    numeros_sorteados = list( range( 0, numeros_posibles+1 ) )
    rnd.shuffle( numeros_sorteados )

    for i_rep in range( 1, pack_size+1 ):
        este_numb = numeros_sorteados[i_rep-1]
        esta_figu = lista_figs[ este_numb ]
        paquete_out.append( esta_figu )

    return paquete_out

#------------------------------------------------------------------------------#

def generar_album( lista_figs ):

    album_out = []
    numero_figs = len(lista_figs)

    for i_pos in range( 1, numero_figs+1):
        album_out.append( 0 )

    return album_out

#------------------------------------------------------------------------------#

def llenar_album( pack_in, album_io, lista_figs ):

    numero_de_figus = len(lista_figs)

    if ( numero_de_figus != len(album_io) ):
        print( "Numero de figus y album no compatibles...")
        print( " - len(lista_figs) = ", len(lista_figs) )
        print( " - len(album_io)   = ", len(album_io) )
        sys.exit( "Abortando" )


    for pack_item in pack_in:
        for this_figid in range( 0, numero_de_figus ):
            if ( pack_item == lista_figs[this_figid] ):
                album_io[this_figid] = album_io[this_figid] + 1

    esta_lleno = 1
    for this_figid in range( 0, numero_de_figus ):
        if ( album_io[this_figid] == 0 ):
            esta_lleno = 0

    return esta_lleno

#------------------------------------------------------------------------------#

def cuantos_packs( pack_size, lista_figs ):

    mialbum = generar_album( lista_figs )
    esta_completo = 0
    packs_comprados = 0

    while ( esta_completo == 0 ):
        packs_comprados = packs_comprados + 1
        mipack = generar_paquete_conrep( pack_size, lista_figs )
        esta_completo = llenar_album( mipack, mialbum, figus_todas )

    return packs_comprados

#------------------------------------------------------------------------------#

def cuantos_packs_promedio( sample_size, pack_size, lista_figs ):

    resultados = []

    for caso in range( 1, sample_size+1 ):
        resultados.append( cuantos_packs( pack_size, lista_figs ) )

    promedio_packs = npy.mean( resultados )
    return promedio_packs

#------------------------------------------------------------------------------#

def pudo_llenar( num_packs, pack_size, lista_figs ):

    mialbum = generar_album( lista_figs )
    esta_completo = 0

    for un_pack in range( 1, num_packs+1 ):
        mipack = generar_paquete_conrep( pack_size, lista_figs )
        esta_completo = llenar_album( mipack, mialbum, figus_todas )

    return esta_completo

#------------------------------------------------------------------------------#

def proba_llenar( num_intentos, num_packs, pack_size, lista_figs ):

    exitos = 0

    for intento in range( 1, num_intentos+1 ):
        exitos = exitos + pudo_llenar( num_packs, pack_size, lista_figs )

    proba = float(exitos) / float(num_intentos)

    return proba


################################################################################
# PROCEDIMIENTOS
#------------------------------------------------------------------------------#

# simple x6
figus_todas = [ "charly", "gonza", "fede", "laia", "yami", "mauro" ]
print( cuantos_packs_promedio( 1000, 1, figus_todas ) )

# intermedio
figus_todas = list( range( 1, 669+1 ) )
figus_todas = list( range( 1, 69+1 ) )
print( cuantos_packs_promedio( 100, 1, figus_todas ) )

# con paquetes
figus_todas = list( range( 1, 669+1 ) )
figus_todas = list( range( 1, 69+1 ) )
print( cuantos_packs_promedio( 100, 5, figus_todas ) )

# opcionales
figus_todas = list( range( 1, 669+1 ) )
figus_todas = list( range( 1, 69+1 ) )
print( proba_llenar( 1000, 100, 5, figus_todas ) )

################################################################################
