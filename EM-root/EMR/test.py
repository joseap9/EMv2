import pandas as pd
from listaEnlazada import *
from Persona import *


datos =  pd.read_csv('listadepacientes.csv')




listaPersonas = ListaEnlazada()

listaPersonas.adicionarFinal(1)
listaPersonas.adicionarFinal(22)
listaPersonas.adicionarFinal(9)
listaPersonas.adicionarFinal(44)
listaPersonas.adicionarFinal(44)
listaPersonas.adicionarFinal(46)

listaPersonas.adicionarFinal(35)

listaPersonas.ordenamientoMergeSort()

listaPersonas.imprimirLista()




