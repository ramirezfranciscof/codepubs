#!/usr/bin/python3
import numpy as npy

################################################################################
# FUNCIONES
#------------------------------------------------------------------------------#

def generar_mazo( n_replicas ):

    list_replicas = range( 1, n_replicas+1 )
    list_palos = [ "C", "D", "T", "P" ]
    list_numeros = range( 1, 13+1 )

    mazo = []

    for i_baraja in list_replicas:
        for i_palo in list_palos:
            for i_numero in list_numeros:
                mazo.append( i_numero )

    npy.random.shuffle( mazo )

    return mazo

#------------------------------------------------------------------------------#

def jugar( mazo_io ):

    total = 0

    while (total < 21):
        carta = mazo_io.pop(0)
        total = total + carta

    return total

#------------------------------------------------------------------------------#

def jugar_varios( n_jugadores, mazo_io ):

    resultados = []

    for i_jugador in range( 1, n_jugadores+1 ):
        jugada = jugar( mazo_io )
        resultados.append( jugada )

    return resultados

#------------------------------------------------------------------------------#

def ver_quien_gano( lista_resultados ):

    lista_ganadores = []

    for resultado in lista_resultados:
        if ( resultado == 21 ):
            lista_ganadores.append(1)
        else:
            lista_ganadores.append(0)

    return lista_ganadores

#------------------------------------------------------------------------------#

def experimentar( n_reps, n_jugs ):

    resultados_totales = []

    for i_jug in range( 1, n_jugs+1 ):
        resultados_totales.append(0)

    for i_rep in range( 1, n_reps+1 ):

        cantidad = round( n_jugs / 5 )
        mazo_actual = generar_mazo( cantidad )

        totales_parcial = jugar_varios( n_jugs, mazo_actual )
        resultado_parcial = ver_quien_gano( totales_parcial )

        for i_jug in range( 0, n_jugs ):
            valor_sumar = resultado_parcial[i_jug]
            valor_viejo = resultados_totales[i_jug]
            resultados_totales[i_jug] = valor_viejo + valor_sumar

    return resultados_totales

################################################################################
# PROCEDIMIENTOS
#------------------------------------------------------------------------------#

mi_mazo = generar_mazo(3)
print( mi_mazo )

mis_jugadas = jugar_varios( 10, mi_mazo )
print( mis_jugadas )

mis_ganadores = ver_quien_gano( mis_jugadas )
print( mis_ganadores )

experimento = experimentar( 100, 4 )
print( experimento )

################################################################################
