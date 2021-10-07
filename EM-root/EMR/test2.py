from Paciente import *
from Persona import *
from listaEnlazada import *
from math import sin  # para usar la función seno

from time import time  # importamos la función time para capturar tiempos


lista = ListaEnlazada()

lista.adicionarFinal(Persona("jose","qwer","m",22))
lista.adicionarFinal(Persona("miguel","qwer","m",34))
lista.adicionarFinal(Persona("cami","qwer","m",9))
lista.adicionarFinal(Persona("quin","qwer","m",19))
lista.adicionarFinal(Persona("alma","qwer","m",22))

import time


def decorador_medir_tiempo(f):
    """
    Decorador
    Ejecuta la funcion medir y calcula el tiempo transcurrido
    Imprime el resultado en la salida estandar.
    """

    def medir():

    # obtengo el tiempo inicial
    tiempo_inicial = time.clock()
    # Ejecuto la funcion decorada 'mi_funcion_a_medir'
    f()
    # Obtengo el tiempo transcurrido
    tiempo_transcurrido = time.clock() - tiempo_inicial
    print("Tiempo transcurrido: %0.10f segundos." % tiempo_transcurrido)
    return medir


@decorador_medir_tiempo
def mi_funcion_a_medir():
    for i in range(10000):
        "Hola mundo!".replace("Hola", "Adiós")


# Ejecuto mi funcion a medir
mi_funcion_a_medir()


