#!/usr/bin/python3
################################################################################
import numpy as npy
import random as rnd
import csv
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

def poblar_coords( tablero, coords, tipo ):
    for coord in coords:
        tablero[ coord ] = tipo
    return True

#------------------------------------------------------------------------------#

def poblar_random( tablero, num_a, num_l ):
    dimx = tablero.shape[0] - 2
    dimy = tablero.shape[1] - 2

    coordlist = []
    for ix in range( 1, dimx+1):
        for iy in range( 1, dimy+1):
            coordlist.append( (ix,iy) )

    rnd.shuffle( coordlist )

    for idx in range(num_a):
        coord = coordlist.pop(0)
        poblar_coords( tablero, [coord], "A" )

    for idx in range(num_l):
        coord = coordlist.pop(0)
        poblar_coords( tablero, [coord], "L" )

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

def contar_tipo( tablero, tipo ):
    dimx = tablero.shape[0] - 2
    dimy = tablero.shape[1] - 2

    contador = 0
    for ix in range( 1, dimx+1):
        for iy in range( 1, dimy+1):
            if ( tablero[ (ix,iy) ] == tipo):
                contador = contador + 1

    return contador

#------------------------------------------------------------------------------#

def cuantos_de_cada( tablero ):
    num_a = contar_tipo( tablero, "A" )
    num_l = contar_tipo( tablero, "L" )
    return [ num_a , num_l ]

#------------------------------------------------------------------------------#

def fase_mover( tablero ):
    dimx = tablero.shape[0] - 2
    dimy = tablero.shape[1] - 2

    for ix in range( 1, dimx+1):
        for iy in range( 1, dimy+1):
            disponible = buscar_adyacente( tablero, (ix,iy), ' ' )
            if ( disponible != [] ):
                if ( tablero[ (ix,iy) ] == "L"):
                    tablero[ (ix,iy) ]       = " "
                    tablero[ disponible[0] ] = "L"
                if ( tablero[ (ix,iy) ] == "A"):
                    tablero[ (ix,iy) ]       = " "
                    tablero[ disponible[0] ] = "A"

    return True

#------------------------------------------------------------------------------#

def fase_alimentacion( tablero ):
    dimx = tablero.shape[0] - 2
    dimy = tablero.shape[1] - 2

    for ix in range( 1, dimx+1):
        for iy in range( 1, dimy+1):
            crd_anti = buscar_adyacente( tablero, (ix,iy), 'A' )
            if ( crd_anti != [] ):
                if ( tablero[ (ix,iy) ] == "L"):
                    tablero[ (ix,iy) ]     = " "
                    tablero[ crd_anti[0] ] = "L"

    return True


#------------------------------------------------------------------------------#

def fase_reproduccion( tablero ):
    dimx = tablero.shape[0] - 2
    dimy = tablero.shape[1] - 2

    for ix in range( 1, dimx+1):
        for iy in range( 1, dimy+1):
            myid = tablero[ (ix,iy) ]
            crd_igual = buscar_adyacente( tablero, (ix,iy), myid )
            crd_libre = buscar_adyacente( tablero, (ix,iy), ' ' )
            if ( (crd_igual != []) and (crd_libre != []) ):
                tablero[ crd_libre[0] ] = myid

    return True

#------------------------------------------------------------------------------#

def evolucionar_en_el_tiempo( tablero, pasos ):

    all_results = []
    for paso in range(pasos):
        fase_alimentacion( tablero )
        fase_reproduccion( tablero )
        fase_mover( tablero )
        un_result = cuantos_de_cada( tablero )
        all_results.append( un_result )

    return all_results

#------------------------------------------------------------------------------#

def registrar_evolucion( tablero, pasos ):

    registro = evolucionar_en_el_tiempo( tablero, pasos )

    with open("predpres.csv", "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow( [ "antilopes", "leones" ] )
        csv_writer.writerows( registro )

    return registro

#------------------------------------------------------------------------------#

def generar_tablero_azar( filas, columnas, numb_a, numb_l ):
    un_tablero = iniciar_tablero( filas, columnas )
    poblar_random( un_tablero, numb_a, numb_l )
    return un_tablero


################################################################################
# PROCEDIMIENTOS
#------------------------------------------------------------------------------#

mi_tablero = 0
mi_tablero = iniciar_tablero( 5, 7 )
print( mi_tablero )
print( "--------" )
mi_lista = [ (1,3), (2,1), (3,1), (3,3) ]
poblar_coords( mi_tablero, mi_lista, "A" )
poblar_coords( mi_tablero, [ (1,2) ], "L" )
print( mi_tablero )
print( buscar_adyacente( mi_tablero, (1,1), "L" ) )
print( buscar_adyacente( mi_tablero, (1,1), "A" ) )
print( buscar_adyacente( mi_tablero, (1,1), " " ) )
print( buscar_adyacente( mi_tablero, (2,2), "A" ) )
print( buscar_adyacente( mi_tablero, (3,3), "L" ) )


mi_tablero = iniciar_tablero( 4, 6 )
mi_lista = [ (2,2), (3,3), (4,3) ]
poblar_coords( mi_tablero, mi_lista, "A" )
mi_lista = [ (4,5), (2,5) ]
poblar_coords( mi_tablero, mi_lista, "L" )
mis_results = evolucionar_en_el_tiempo( mi_tablero, 8 )
print( contar_tipo( mi_tablero, "A" ) )


mi_tablero = iniciar_tablero( 10, 10 )
print( mi_tablero )
poblar_random( mi_tablero, 10, 5 )
print( mi_tablero )
print( evolucionar_en_el_tiempo( mi_tablero, 10 ) )

################################################################################
