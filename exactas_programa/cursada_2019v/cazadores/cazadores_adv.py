#!/usr/bin/python3
################################################################################
import numpy as npy
import random as rnd
#import matplotlib.pyplot as plt

################################################################################
# FUNCIONES
#------------------------------------------------------------------------------#

def iniciar_tablero( dimx, dimy ):
    tablero0 = npy.repeat(" ", (dimx+2) * (dimy+2) ).reshape(dimx+2 ,dimy+2)

    for idx in range( dimx+2 ):
        tablero0[ (idx, 0) ]      = "M"
        tablero0[ (idx, dimy+1) ] = "M"

    for idx in range( dimy+2 ):
        tablero0[ (0, idx) ]      = "M"
        tablero0[ (dimx+1, idx) ] = "M"

    return tablero0


#------------------------------------------------------------------------------#

def contar_espacios( tablero, tipo ):

    dimx = tablero.shape[0] - 2
    dimy = tablero.shape[1] - 2
    cont = 0

    for ix in range( 1, dimx):
        for iy in range( 1, dimy):
            if (tablero[ (ix,iy) ] == tipo):
                cont = cont + 1

    return cont


#------------------------------------------------------------------------------#

def poblar_coords( tablero, coords, tipo ):
    for coord in coords:
        tablero[ coord ] = tipo
    return True

#------------------------------------------------------------------------------#

def poblar_random( tablero, n_deers, n_lions ):
    
    dimx = tablero.shape[0] - 2
    dimy = tablero.shape[1] - 2

    for ii in range(n_deers):
        item_libre = True
        while (item_libre):
            posx = rnd.randint( 1, dimx )
            posy = rnd.randint( 1, dimy )
            if ( tablero[ (posx, posy) ] == " " ):
                tablero[ (posx, posy) ] = "A"
                item_libre = False

    for ii in range(n_lions):
        item_libre = True
        while (item_libre):
            posx = rnd.randint( 1, dimx )
            posy = rnd.randint( 1, dimy )
            if ( tablero[ (posx,posy) ] == " " ):
                tablero[ (posx, posy) ] = "L"
                item_libre = False

    return True


#------------------------------------------------------------------------------#

def coord_vecinas( tablero, coord ):
#   (x-1,y-1)  (x-1,y+0)  (x-1,y+1)
#   (x+0,y-1)  (x+0,y+0)  (x+0,y+1)
#   (x+1,y-1)  (x+1,y+0)  (x+1,y+1)
    posx = coord[0]
    posy = coord[1]
    lista_vecinos = []
    lista_vecinos.append( ( posx-1 , posy-1 ) )
    lista_vecinos.append( ( posx-1 , posy+0 ) )
    lista_vecinos.append( ( posx-1 , posy+1 ) )
    lista_vecinos.append( ( posx+0 , posy+1 ) )
    lista_vecinos.append( ( posx+1 , posy+1 ) )
    lista_vecinos.append( ( posx+1 , posy+0 ) )
    lista_vecinos.append( ( posx+1 , posy-1 ) )
    lista_vecinos.append( ( posx+0 , posy-1 ) )
    return lista_vecinos


#------------------------------------------------------------------------------#

def buscar_adyacente( tablero, coord, tipo ):
    posx = coord[0]
    posy = coord[1]
    coord_out = []

    mis_vecinos = coord_vecinas( tablero, coord )
    for crd_vecino in mis_vecinos:
        if ( tablero[ crd_vecino ] == tipo ):
            return [ crd_vecino ]
    return []


#------------------------------------------------------------------------------#

def fase_mover( tablero ):



################################################################################
# PROCEDIMIENTOS
#------------------------------------------------------------------------------#

mi_tablero = 0
mi_tablero = iniciar_tablero( 7, 9 )
print( mi_tablero )
print( "--------" )
mi_lista = [ (1,3), (2,1), (3,1), (3,3) ]
poblar_coords( mi_tablero, mi_lista, "A" )
poblar_coords( mi_tablero, [ (1,2) ], "L" )
#poblar_random( mi_tablero, 4, 1 )
print( mi_tablero )
print( buscar_adyacente( mi_tablero, (1,1), "L" ) )
print( buscar_adyacente( mi_tablero, (1,1), "A" ) )
print( buscar_adyacente( mi_tablero, (1,1), " " ) )
print( buscar_adyacente( mi_tablero, (2,2), "A" ) )
print( buscar_adyacente( mi_tablero, (3,3), "L" ) )


################################################################################
