from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import numpy as np
from numpy.lib.twodim_base import diag
import pylab as pl
import pandas as pd
from PIL import Image, ImageTk
from time import time
from Medico import *
from Paciente import *
from Persona import *
from Especialidad import *
from functions import display_logo
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter.messagebox import showinfo

medico = Medico("", "", "", "", "", "")
paciente = Paciente("", "-", "-", "", "", "", "", False, "", "", "", "", "", "")

# lista completa de pacientes
listaEnlazada = ListaEnlazada()
# lista de pacientes de alta Medica
listaPacientesAM = ListaEnlazada()




# lista de pacientes por es
listaTrauma = ListaTrauma()
listaNeuro = ListaNeuro()
listaCardio = ListaCardio()


# lista de ordenamiento por edad
listaOrdenamiento = ListaEnlazada()
# lista de orden por diagnostico
listaDiagnostico = ListaEnlazada()
# lista de orden Por Estado
listaEstado = ListaEnlazada()

listaOrdenadaPorEdad = []
listaOrdenadaPorEstado = []
listaOrdenadaPorDiagnostico = []

listadoPacientesCsv = pd.read_csv('listadepacientes.csv')

for x in range(48):
    listaEnlazada.adicionarFinal(
        Paciente(listadoPacientesCsv['nombre'].loc[x], str(listadoPacientesCsv['rut'].loc[x]),
                 listadoPacientesCsv['sexo'].loc[x]
                 , listadoPacientesCsv['edad'].loc[x], listadoPacientesCsv['diagnosticoI'].loc[x],
                 listadoPacientesCsv['estado'].loc[x]
                 , listadoPacientesCsv['despacho'].loc[x], listadoPacientesCsv['altaMedica'].loc[x]
                 , listadoPacientesCsv['nombreMedico'].loc[x], listadoPacientesCsv['rutMedico'].loc[x],
                 listadoPacientesCsv['diagnostico'].loc[x], listadoPacientesCsv['tratamiento'].loc[x]
                 , listadoPacientesCsv['idEspecialista'].loc[x], listadoPacientesCsv['nombreEspecialidad'].loc[x]))

for j in range(0, listaEnlazada.contador()):
    listaOrdenamiento.adicionarFinal(listaEnlazada[j].getEdad())

for i in range(listaEnlazada.contador()):
    listaOrdenadaPorEdad.append(Paciente(listaEnlazada[i].getNombre(), listaEnlazada[i].getRut()
                                         , listaEnlazada[i].getSexo(), listaEnlazada[i].getEdad()
                                         , listaEnlazada[i].getDiagnosticoI(), listaEnlazada[i].getEstado()
                                         , listaEnlazada[i].getDespacho(), listaEnlazada[i].getaltaMedica(),
                                         listaEnlazada[i].getNombreM(), listaEnlazada[i].getRutM()
                                         , listaEnlazada[i].getDiagnostico(), listaEnlazada[i].getTratamiento()
                                         , listaEnlazada[i].getIdEspecialista(),
                                         listaEnlazada[i].getNombreEspecialidad()))

for i in range(listaEnlazada.contador()):
            if listaEnlazada[i].getEstado() == "Reanimacion":
                listaEstado.adicionarFinal(1)
                listaOrdenadaPorEstado.append(Paciente(listaEnlazada[i].getNombre(), listaEnlazada[i].getRut()
                                                     , listaEnlazada[i].getSexo(), listaEnlazada[i].getEdad()
                                                     , listaEnlazada[i].getDiagnosticoI(), listaEnlazada[i].getEstado()
                                                     , listaEnlazada[i].getDespacho(), listaEnlazada[i].getaltaMedica(),
                                                     int(1), listaEnlazada[i].getRutM()
                                                     , listaEnlazada[i].getDiagnostico(),
                                                     listaEnlazada[i].getTratamiento()
                                                     , listaEnlazada[i].getIdEspecialista(),
                                                     listaEnlazada[i].getNombreEspecialidad()))

            elif listaEnlazada[i].getEstado() == "Emergencia":
                listaEstado.adicionarFinal(2)
                listaOrdenadaPorEstado.append(Paciente(listaEnlazada[i].getNombre(), listaEnlazada[i].getRut()
                                                       , listaEnlazada[i].getSexo(), listaEnlazada[i].getEdad()
                                                       , listaEnlazada[i].getDiagnosticoI(),
                                                       listaEnlazada[i].getEstado()
                                                       , listaEnlazada[i].getDespacho(),
                                                       listaEnlazada[i].getaltaMedica(),
                                                       int(2), listaEnlazada[i].getRutM()
                                                       , listaEnlazada[i].getDiagnostico(),
                                                       listaEnlazada[i].getTratamiento()
                                                       , listaEnlazada[i].getIdEspecialista(),
                                                       listaEnlazada[i].getNombreEspecialidad()))
            elif listaEnlazada[i].getEstado() == "Urgencia":
                listaEstado.adicionarFinal(3)
                listaOrdenadaPorEstado.append(Paciente(listaEnlazada[i].getNombre(), listaEnlazada[i].getRut()
                                                       , listaEnlazada[i].getSexo(), listaEnlazada[i].getEdad()
                                                       , listaEnlazada[i].getDiagnosticoI(),
                                                       listaEnlazada[i].getEstado()
                                                       , listaEnlazada[i].getDespacho(),
                                                       listaEnlazada[i].getaltaMedica(),
                                                       int(3), listaEnlazada[i].getRutM()
                                                       , listaEnlazada[i].getDiagnostico(),
                                                       listaEnlazada[i].getTratamiento()
                                                       , listaEnlazada[i].getIdEspecialista(),
                                                       listaEnlazada[i].getNombreEspecialidad()))
            elif listaEnlazada[i].getEstado() == "Prioritario":
                listaEstado.adicionarFinal(4)
                listaOrdenadaPorEstado.append(Paciente(listaEnlazada[i].getNombre(), listaEnlazada[i].getRut()
                                                       , listaEnlazada[i].getSexo(), listaEnlazada[i].getEdad()
                                                       , listaEnlazada[i].getDiagnosticoI(),
                                                       listaEnlazada[i].getEstado()
                                                       , listaEnlazada[i].getDespacho(),
                                                       listaEnlazada[i].getaltaMedica(),
                                                       int(4), listaEnlazada[i].getRutM()
                                                       , listaEnlazada[i].getDiagnostico(),
                                                       listaEnlazada[i].getTratamiento()
                                                       , listaEnlazada[i].getIdEspecialista(),
                                                       listaEnlazada[i].getNombreEspecialidad()))
            else:
                listaEstado.adicionarFinal(5)
                listaOrdenadaPorEstado.append(Paciente(listaEnlazada[i].getNombre(), listaEnlazada[i].getRut()
                                                       , listaEnlazada[i].getSexo(), listaEnlazada[i].getEdad()
                                                       , listaEnlazada[i].getDiagnosticoI(),
                                                       listaEnlazada[i].getEstado()
                                                       , listaEnlazada[i].getDespacho(),
                                                       listaEnlazada[i].getaltaMedica(),
                                                       int(5), listaEnlazada[i].getRutM()
                                                       , listaEnlazada[i].getDiagnostico(),
                                                       listaEnlazada[i].getTratamiento()
                                                       , listaEnlazada[i].getIdEspecialista(),
                                                       listaEnlazada[i].getNombreEspecialidad()))

for i in range(listaEnlazada.contador()):
            if listaEnlazada[i].getDiagnosticoI() == "1-Hemorragia Traumatica":
                listaDiagnostico.adicionarFinal(1)
                listaOrdenadaPorDiagnostico.append(Paciente(listaEnlazada[i].getNombre(), listaEnlazada[i].getRut()
                                                     , listaEnlazada[i].getSexo(), listaEnlazada[i].getEdad()
                                                     , listaEnlazada[i].getDiagnosticoI(), listaEnlazada[i].getEstado()
                                                     , listaEnlazada[i].getDespacho(), listaEnlazada[i].getaltaMedica(),
                                                     int(1), int(1)
                                                     , listaEnlazada[i].getDiagnostico(),
                                                     listaEnlazada[i].getTratamiento()
                                                     , listaEnlazada[i].getIdEspecialista(),
                                                     listaEnlazada[i].getNombreEspecialidad()))

            elif listaEnlazada[i].getDiagnosticoI() == "2-Impacto de Bala":
                listaDiagnostico.adicionarFinal(2)
                listaOrdenadaPorDiagnostico.append(Paciente(listaEnlazada[i].getNombre(), listaEnlazada[i].getRut()
                                                       , listaEnlazada[i].getSexo(), listaEnlazada[i].getEdad()
                                                       , listaEnlazada[i].getDiagnosticoI(),
                                                       listaEnlazada[i].getEstado()
                                                       , listaEnlazada[i].getDespacho(),
                                                       listaEnlazada[i].getaltaMedica(),
                                                       int(2), int(2)
                                                       , listaEnlazada[i].getDiagnostico(),
                                                       listaEnlazada[i].getTratamiento()
                                                       , listaEnlazada[i].getIdEspecialista(),
                                                       listaEnlazada[i].getNombreEspecialidad()))
            elif listaEnlazada[i].getDiagnosticoI() == "3-Fractura Osea":
                listaDiagnostico.adicionarFinal(3)
                listaOrdenadaPorDiagnostico.append(Paciente(listaEnlazada[i].getNombre(), listaEnlazada[i].getRut()
                                                            , listaEnlazada[i].getSexo(), listaEnlazada[i].getEdad()
                                                            , listaEnlazada[i].getDiagnosticoI(),
                                                            listaEnlazada[i].getEstado()
                                                            , listaEnlazada[i].getDespacho(),
                                                            listaEnlazada[i].getaltaMedica(),
                                                            int(3), int(3)
                                                            , listaEnlazada[i].getDiagnostico(),
                                                            listaEnlazada[i].getTratamiento()
                                                            , listaEnlazada[i].getIdEspecialista(),
                                                            listaEnlazada[i].getNombreEspecialidad()))

            elif listaEnlazada[i].getDiagnosticoI() == "4-Infeccion Bacteriana":
                listaDiagnostico.adicionarFinal(4)
                listaOrdenadaPorDiagnostico.append(Paciente(listaEnlazada[i].getNombre(), listaEnlazada[i].getRut()
                                                            , listaEnlazada[i].getSexo(), listaEnlazada[i].getEdad()
                                                            , listaEnlazada[i].getDiagnosticoI(),
                                                            listaEnlazada[i].getEstado()
                                                            , listaEnlazada[i].getDespacho(),
                                                            listaEnlazada[i].getaltaMedica(),
                                                            int(4), int(4)
                                                            , listaEnlazada[i].getDiagnostico(),
                                                            listaEnlazada[i].getTratamiento()
                                                            , listaEnlazada[i].getIdEspecialista(),
                                                            listaEnlazada[i].getNombreEspecialidad()))
            else:
                listaDiagnostico.adicionarFinal(5)
                listaOrdenadaPorDiagnostico.append(Paciente(listaEnlazada[i].getNombre(), listaEnlazada[i].getRut()
                                                       , listaEnlazada[i].getSexo(), listaEnlazada[i].getEdad()
                                                       , listaEnlazada[i].getDiagnosticoI(),
                                                       listaEnlazada[i].getEstado()
                                                       , listaEnlazada[i].getDespacho(),
                                                       listaEnlazada[i].getaltaMedica(),
                                                       int(5), int(5)
                                                       , listaEnlazada[i].getDiagnostico(),
                                                       listaEnlazada[i].getTratamiento()
                                                       , listaEnlazada[i].getIdEspecialista(),
                                                       listaEnlazada[i].getNombreEspecialidad()))


def addList():
    listaTrauma.adicionarFinal(
        Paciente("Silvia Gonzalez", "27039327-6", "M", 55, "1-Hemorragia Traumática", "normal", "traumatologia",
                 False, "jose Perdomo", "", "", "", "", ""))
    listaTrauma.adicionarFinal(
        Paciente("Silvia Gonzalez", "27039327-6", "M", 37, "1-Hemorragia Traumática", "normal", "traumatologia",
                 False, "jose Perdomo", "", "", "", "", ""))
    listaTrauma.adicionarFinal(
        Paciente("Silvia Gonzalez", "27039327-6", "M", "portugal 272", "1-Hemorragia Traumática", "normal",
                 "traumatologia",
                 False, "jose Perdomo", "", "", "", "", ""))
    listaTrauma.adicionarFinal(
        Paciente("Silvia Gonzalez", "27039327-6", "M", "portugal 272", "1-Hemorragia Traumática", "normal",
                 "traumatologia",
                 False, "jose Perdomo", "", "", "", "", ""))
    listaTrauma.adicionarFinal(
        Paciente("Silvia Gonzalez", "27039327-6", "M", "portugal 272", "1-Hemorragia Traumática", "normal",
                 "traumatologia",
                 False, "jose Perdomo", "", "", "", "", ""))
    listaTrauma.adicionarFinal(
        Paciente("Silvia Gonzalez", "27039327-6", "M", "portugal 272", "1-Hemorragia Traumática", "normal",
                 "traumatologia",
                 False, "jose Perdomo", "", "", "", "", ""))
    listaTrauma.adicionarFinal(
        Paciente("Silvia Gonzalez", "27039327-6", "M", "portugal 272", "1-Hemorragia Traumática", "normal",
                 "traumatologia",
                 False, "jose Perdomo", "", "", "", "", ""))

    listaNeuro.adicionarFinal(
        Paciente("Silvia Gonzalez", "27039327-6", "M", "portugal 272", "---", "normal", "traumatologia", False,
                 "jose Perdomo", "", "", "", "", ""))
    listaNeuro.adicionarFinal(
        Paciente("Silvia Gonzalez", "27039327-6", "M", "portugal 272", "---", "normal", "traumatologia", False,
                 "jose Perdomo", "", "", "", "", ""))
    listaNeuro.adicionarFinal(
        Paciente("Silvia Gonzalez", "27039327-6", "M", "portugal 272", "---", "normal", "traumatologia", False,
                 "jose Perdomo", "", "", "", "", ""))
    listaNeuro.adicionarFinal(
        Paciente("Silvia Gonzalez", "27039327-6", "M", "portugal 272", "---", "normal", "traumatologia", False,
                 "jose Perdomo", "", "", "", "", ""))
    listaNeuro.adicionarFinal(
        Paciente("Silvia Gonzalez", "27039327-6", "M", "portugal 272", "---", "normal", "traumatologia", False,
                 "jose Perdomo", "", "", "", "", ""))
    listaNeuro.adicionarFinal(
        Paciente("Silvia Gonzalez", "27039327-6", "M", "portugal 272", "1-Hemorragia Traumática", "normal",
                 "neurologia",
                 False, "jose Perdomo", "", "", "", "", ""))

    listaCardio.adicionarFinal(
        Paciente("Silvia Gonzalez", "27039327-6", "M", "portugal 272", "---", "normal", "traumatologia", False,
                 "jose Perdomo", "", "", "", "", ""))
    listaCardio.adicionarFinal(
        Paciente("Silvia Gonzalez", "27039327-6", "M", "portugal 272", "---", "normal", "traumatologia", False,
                 "jose Perdomo", "", "", "", "", ""))
    listaCardio.adicionarFinal(
        Paciente("Silvia Gonzalez", "27039327-6", "M", "portugal 272", "---", "normal", "traumatologia", False,
                 "jose Perdomo", "", "", "", "", ""))
    listaCardio.adicionarFinal(
        Paciente("Silvia Gonzalez", "27039327-6", "M", "portugal 272", "---", "normal", "traumatologia", False,
                 "jose Perdomo", "", "", "", "", ""))
    listaCardio.adicionarFinal(
        Paciente("Silvia Gonzalez", "27039327-6", "M", "portugal 272", "---", "normal", "traumatologia", False,
                 "jose Perdomo", "", "", "", "", ""))


# Lista de medicos
medico = ["Dr. Alberto Rojas", "26970671-6", "No disponible", "No Disponible", "543", "Traumatologia"]


def ordenamiento():


    def graficos():
        # ==================GRAFICOS==================================

        # grafico de edades tipo pie

        popup = Toplevel()
        popup.geometry("1180x430")

        popup.wm_title("Ordenamiento de Pacientes")
        popup.configure(bg="#C0EAF8")
        menores = 0
        adultos = 0
        terceraEdad = 0

        for x in range(listaOrdenamiento.contador()):
            if listaOrdenamiento[x] >= 0 and listaOrdenamiento[x] <= 18:
                menores += 1
            elif listaOrdenamiento[x] >= 19 and listaOrdenamiento[x] <= 49:
                adultos += 1
            else:
                terceraEdad += 1

        fig = plt.Figure(figsize=(3.5, 3.9))
        a = fig.add_subplot(111)
        a.pie([menores, adultos, terceraEdad], autopct='%1.1f%%')  # an example data
        a.legend(["Edades: [1 - 18] -> TOTAL: " + str(menores)
                     , "Edades: [19 - 49] -> TOTAL: " + str(adultos)
                     , "Edades: [50+] -> TOTAL: " + str(terceraEdad)], prop={'size': 8}, bbox_to_anchor=(1.1, 0.01))
        a.set_title("Pacientes Ingresados Por Rango de Edad")
        canvas = FigureCanvasTkAgg(fig, master=popup)
        canvas.get_tk_widget().place(x=30, y=10)
        canvas.draw()

        # grafico de estados tipo pie
        reanimacion = 0
        emergencia = 0
        urgencia = 0
        prioritario = 0
        noUrgencia = 0

        for i in range(listaEstado.contador()):
            if listaEstado[i] == 1:
                reanimacion += 1
            elif listaEstado[i] == 2:
                emergencia += 1
            elif listaEstado[i] == 3:
                urgencia += 1
            elif listaEstado[i] == 4:
                prioritario += 1
            else:
                noUrgencia += 1


        fig = plt.Figure(figsize=(3.5, 3.9))
        B = fig.add_subplot(111)
        B.pie([reanimacion, emergencia, urgencia,prioritario,noUrgencia], autopct='%1.1f%%')  # an example data
        B.legend(["Reanimacion: " + str(reanimacion)
                     , "Emergencia: " + str(emergencia)
                     , "Urgencia " + str(urgencia)
                  ,"Prioritario: " + str(prioritario)
                  ,"No Urgencia: "+ str(noUrgencia)], prop={'size': 8}, bbox_to_anchor=(1.1, 0.12))
        B.set_title("Pacientes Ingresados Por Estado")
        canvasE = FigureCanvasTkAgg(fig, master=popup)
        canvasE.get_tk_widget().place(x=405, y=10)
        canvasE.draw()

        # grafico de Diagnostico tipo pie
        hemorragia = 0
        impacto = 0
        fractura = 0
        infeccion = 0
        otro = 0

        for i in range(listaDiagnostico.contador()):
            if listaDiagnostico[i] == 1:
                hemorragia += 1
            elif listaDiagnostico[i] == 2:
                impacto += 1
            elif listaDiagnostico[i] == 3:
                fractura += 1
            elif listaDiagnostico[i] == 4:
                infeccion += 1
            else:
                otro += 1


        fig3 = plt.Figure(figsize=(3.5, 3.9))
        C = fig3.add_subplot(111)
        C.pie([hemorragia, impacto, fractura,infeccion,otro], autopct='%1.1f%%')  # an example data
        C.legend(["Hemorragia: " + str(hemorragia)
                     , "Impacto de Bala: " + str(impacto)
                     , "Fractura Osea " + str(fractura)
                  ,"Infeccion Bacteriana: " + str(infeccion)
                  ,"Otro: "+ str(otro)], prop={'size': 8}, bbox_to_anchor=(1.1, 0.12))
        C.set_title("Pacientes Ingresados Por Diagnostico I.")
        canvasE = FigureCanvasTkAgg(fig3, master=popup)
        canvasE.get_tk_widget().place(x=785, y=10)
        canvasE.draw()



        popup.mainloop()

    def ordenPorDiagnostico():

        listaDiagnostico.ordenamientoBurbuja()
        listaOrdenadaPorDiagnostico.sort(key=lambda x: x.getRutM())

    def ordenPorEstado():

        listaEstado.ordenamientoBurbuja()
        listaOrdenadaPorEstado.sort(key=lambda x: x.getNombreM())



    def ordenPorEdad():

        tiempo_inicial = time()

        listaOrdenamiento.ordenamientoBurbuja()
        listaOrdenadaPorEdad.sort(key=lambda x: x.edad)

        tiempo_final = time()
        tiempo_ejecucion = tiempo_final - tiempo_inicial

        print("Tiempo transcurrido: %0.15f segundos." % tiempo_ejecucion)
        listaOrdenadaPorEdad.sort(key=lambda x: x.edad)




    ordenPorDiagnostico()
    ordenPorEstado()
    ordenPorEdad()
    popup = Toplevel()

    popup.geometry("1000x530")

    popup.wm_title("Ordenamiento de Pacientes")
    popup.configure(bg="#C0EAF8")

    # marco
    marcoTrauma = LabelFrame(popup, text="Orden Por Edad", bd=4, width=290, height=420, bg="#EDF0F2")
    marcoTrauma.place(x=30, y=25)
    # estilo
    style = ttk.Style()
    style.configure('Treeview', background="#C0EAF8", foreground="black", fieldBackground="#C0EAF8")
    style.theme_use("default")
    style.map('Treeview', background=[('selected', '#DCA44C')])
    # creacion de tabla
    tablaT = ttk.Treeview(popup, columns=(0, 1, 2), show='headings', height=18)
    tablaT.place(x=50, y=50)
    tablaT.tag_configure('oddrow', background="#26C1F4")
    tablaT.tag_configure('evenrow', background="#C0EAF8")
    tablaT.heading(0, text="n°")
    tablaT.heading(1, text="Nombre")
    tablaT.heading(2, text="Edad")
    tablaT.column(0, width=10, minwidth=25)
    tablaT.column(1, width=120)
    tablaT.column(2, width=120)
    # scrollBar
    yscrollbar = ttk.Scrollbar(popup, orient="vertical", command=tablaT.yview)
    yscrollbar.place(x=300, y=50)

    ##======================================================================================
    # marco
    marcoEstado = LabelFrame(popup, text="Orden Por Estado", bd=4, width=290, height=420, bg="#EDF0F2")
    marcoEstado.place(x=330, y=25)
    # estilo
    style = ttk.Style()
    style.configure('Treeview', background="#C0EAF8", foreground="black", fieldBackground="#C0EAF8")
    style.theme_use("default")
    style.map('Treeview', background=[('selected', '#DCA44C')])
    # creacion de tabla
    tablaE = ttk.Treeview(popup, columns=(0, 1, 2), show='headings', height=18)
    tablaE.place(x=350, y=50)
    tablaE.tag_configure('oddrow', background="#26C1F4")
    tablaE.tag_configure('evenrow', background="#C0EAF8")
    tablaE.heading(0, text="n°")
    tablaE.heading(1, text="Nombre")
    tablaE.heading(2, text="Estado")
    tablaE.column(0, width=10, minwidth=25)
    tablaE.column(1, width=120)
    tablaE.column(2, width=120)
    # scrollBar
    yscrollbar = ttk.Scrollbar(popup, orient="vertical", command=tablaE.yview)
    yscrollbar.place(x=600, y=50)

    ##======================================================================================
    # marco DIAG
    marcoD = LabelFrame(popup, text="Orden Por Diagnostico Inicial", bd=4, width=335, height=420, bg="#EDF0F2")
    marcoD.place(x=630, y=25)
    # estilo
    style = ttk.Style()
    style.configure('Treeview', background="#C0EAF8", foreground="black", fieldBackground="#C0EAF8")
    style.theme_use("default")
    style.map('Treeview', background=[('selected', '#DCA44C')])
    # creacion de tabla
    tablaD = ttk.Treeview(popup, columns=(0, 1, 2), show='headings', height=18)
    tablaD.place(x=650, y=50)
    tablaD.tag_configure('oddrow', background="#26C1F4")
    tablaD.tag_configure('evenrow', background="#C0EAF8")
    tablaD.heading(0, text="n°")
    tablaD.heading(1, text="Nombre")
    tablaD.heading(2, text="Diag. I")
    tablaD.column(0, width=10, minwidth=25)
    tablaD.column(1, width=120)
    tablaD.column(2, width=165)
    # scrollBar
    yscrollbar = ttk.Scrollbar(popup, orient="vertical", command=tablaD.yview)
    yscrollbar.place(x=945, y=50)

    index = 1
    indexE = 1
    indexD = 1
    t = 0
    E = 0
    D = 0
    for i in range(len(listaOrdenadaPorEdad)):
        if t % 2 == 0:
            tablaT.insert(parent='', index=i, iid=i,
                          values=(index, listaOrdenadaPorEdad[i].getNombre(), listaOrdenadaPorEdad[i].getEdad()),
                          tags=('evenrow'))

        else:
            tablaT.insert(parent='', index=i, iid=i,
                          values=(index, listaOrdenadaPorEdad[i].getNombre(), listaOrdenadaPorEdad[i].getEdad()),
                          tags=('oddrow'))

        index += 1
        t += 1

    for i in range(len(listaOrdenadaPorEstado)):
        if E % 2 == 0:
            tablaE.insert(parent='', index=i, iid=i,
                          values=(indexE, listaOrdenadaPorEstado[i].getNombre(), listaOrdenadaPorEstado[i].getEstado()),
                          tags=('evenrow'))

        else:
            tablaE.insert(parent='', index=i, iid=i,
                          values=(indexE, listaOrdenadaPorEstado[i].getNombre(), listaOrdenadaPorEstado[i].getEstado()),
                          tags=('oddrow'))

        indexE += 1
        E += 1

    for i in range(len(listaOrdenadaPorDiagnostico)):
        if D % 2 == 0:
            tablaD.insert(parent='', index=i, iid=i,
                          values=(indexD, listaOrdenadaPorDiagnostico[i].getNombre(), listaOrdenadaPorDiagnostico[i].getDiagnosticoI()),
                          tags=('evenrow'))

        else:
            tablaD.insert(parent='', index=i, iid=i,
                          values=(indexD, listaOrdenadaPorDiagnostico[i].getNombre(), listaOrdenadaPorDiagnostico[i].getDiagnosticoI()),
                          tags=('oddrow'))

        indexD += 1
        D += 1

    imgAgregar = Image.open('images/agregarPrin.png')
    imgAgregar = ImageTk.PhotoImage(imgAgregar)
    agregar = Button(popup, image=imgAgregar, borderwidth=0, bg="#0026fe", command=lambda: [graficos()])
    agregar.place(x=895, y=460)

    popup.mainloop()



def treeInit():
    opcionPacientesIngresados = 'Pacientes Ingresados'
    opcionGrafico = 'Grafico de Pacientes'

    def infoTree():

        def selectPacient():

            def close_window(root):
                root.destroy()

            def guardaT():

                diagnosticoAct = ""
                tratamientoAct = ""
                listaEnlazada[index].setDiagnostico(diagnostico.get())
                listaEnlazada[index].setTratamiento(tratamiento.get("1.0", "end"))

                if len(listaEnlazada[index].getDiagnostico()) == 0:
                    diagnosticoAct = "No Disponible"
                else:
                    diagnosticoAct = listaEnlazada[index].getDiagnostico()

                cDiagnostico.set(diagnosticoAct)

                if len(listaEnlazada[index].getTratamiento()) == 0:
                    tratamientoAct = "No Disponible"
                else:
                    tratamientoAct = listaEnlazada[index].getTratamiento()

                cTratamiento.set(tratamientoAct)

            top = Toplevel()
            top.geometry("350x270")
            top.title("Diagnostico")
            header = Frame(top, width=500, height=120)
            header.pack()
            body = Frame(top, width=500, height=380, bg="#00B8FF")
            body.pack()

            selected = tree.selection()
            values = tree.item(selected, 'values')
            text = tree.item(selected, 'text')
            index = int(values[0])

            tk.Label(top, text="Diagnostico:").place(x=125, y=10)
            diagnostico = tk.Entry(top, width=40)
            diagnostico.place(x=50, y=30)

            tk.Label(top, text="Tratamiento:").place(x=125, y=50)
            tratamiento = tk.Text(top, height=5, width=25, padx=15, pady=15)
            tratamiento.place(x=50, y=70)

            imgAgrega = Image.open('images/solAtenAgregar.png')
            imgAgrega = ImageTk.PhotoImage(imgAgrega)
            agrega = Button(top, image=imgAgrega, borderwidth=0, bg="#00B8FF",
                            command=lambda: [guardaT(), close_window(top)])
            agrega.place(x=210, y=200)

            imgBac = Image.open('images/solAtenAtras.png')
            imgBac = ImageTk.PhotoImage(imgBac)
            bac = Button(top, image=imgBac, borderwidth=0, bg="#00B8FF", command=lambda: close_window(top))
            bac.place(x=280, y=200)

            top.mainloop()

        def altaMedica():

            def showInfo():
                resp = messagebox.showinfo("Info", "Alta Medica Completa\n\n", parent=info)
                if resp == "ok":
                    ActualizaTabla()
                    close_window(info)

            selected = tree.focus()
            values = tree.item(selected, 'values')
            index = int(values[0])
            listaEnlazada[index].setaltaMedica()

            listaPacientesAM.adicionarFinal(Paciente(listaEnlazada[index].getNombre(), listaEnlazada[index].getRut(),
                                                     listaEnlazada[index].getSexo(),
                                                     listaEnlazada[index].getEdad(),
                                                     listaEnlazada[index].getDiagnosticoI(),
                                                     listaEnlazada[index].getEstado(),
                                                     listaEnlazada[index].getDespacho(), True,
                                                     listaEnlazada[index].getNombreM(), listaEnlazada[index].getRutM(),
                                                     listaEnlazada[index].getDiagnostico(),
                                                     listaEnlazada[index].getTratamiento(),
                                                     listaEnlazada[index].getIdEspecialista(),
                                                     listaEnlazada[index].getNombreEspecialidad()))

            rutActual = listaEnlazada[index].getRut()
            listaEnlazada.borrarPorRut(rutActual)
            showInfo()

        def close_window(root):
            root.destroy()

        cNom = StringVar()
        cRut = StringVar()
        cEstado = StringVar()
        cDiagI = StringVar()
        cSexo = StringVar()
        cEdad = StringVar()
        cDiagnostico = StringVar()
        cTratamiento = StringVar()

        selected = tree.selection()
        values = tree.item(selected, 'values')
        text = tree.item(selected, 'text')
        index = int(values[0])

        cNom.set(listaEnlazada[index].getNombre())
        cRut.set(listaEnlazada[index].getRut())
        cEstado.set(listaEnlazada[index].getEstado())
        cDiagI.set(listaEnlazada[index].getDiagnosticoI())
        cSexo.set(listaEnlazada[index].getSexo())
        cEdad.set(listaEnlazada[index].getEdad())

        diagnostico = ""
        if len(listaEnlazada[index].getDiagnostico()) == 0:
            diagnostico = "No Disponible"
        else:
            diagnostico = listaEnlazada[index].getDiagnostico()

        cDiagnostico.set(diagnostico)

        tratamiento = ""
        if len(listaEnlazada[index].getTratamiento()) == 0:
            tratamiento = "No Disponible"
        else:
            tratamiento = listaEnlazada[index].getTratamiento()

        cTratamiento.set(tratamiento)

        info = Toplevel()
        info.title("Paciente " + listaEnlazada[index].getNombre())
        info.geometry("420x360")
        header = Frame(info, width=550, height=167)
        header.pack()
        body = Frame(info, width=550, height=500, bg="#00B8FF")
        body.pack()

        Label(info, text="Nombre:").place(x=40, y=30)
        nombre = Entry(info, width=30, state="readonly", textvariable=cNom)
        nombre.focus()
        nombre.place(x=170, y=30)

        Label(info, text="Rut:").place(x=40, y=60)
        rut = Entry(info, width=30, state="readonly", textvariable=cRut)
        rut.place(x=170, y=60)

        Label(info, text="Edad:").place(x=40, y=90)
        Edad = Entry(info, width=30, state="readonly", textvariable=cEdad)
        Edad.place(x=170, y=90)

        Label(info, text="Diagnostico Inicial:").place(x=40, y=120)
        diagI = Entry(info, width=30, state="readonly", textvariable=cDiagI)
        diagI.place(x=170, y=120)

        Label(info, text=f"Estado de {listaEnlazada[index].getNombre()}", bg="#00B8FF",
              font=("Aharoni", 10, 'bold')).place(x=100, y=170)

        Label(info, text="Estado:", bg="#00B8FF").place(x=40, y=200)
        estado = Entry(info, width=30, state="readonly", textvariable=cEstado)
        estado.place(x=170, y=200)

        Label(info, text="Diagnostico:", bg="#00B8FF").place(x=40, y=230)
        estado = Entry(info, width=30, state="readonly", textvariable=cDiagnostico)
        estado.place(x=170, y=230)

        Label(info, text="Tratamiento:", bg="#00B8FF").place(x=40, y=260)
        datosBoxT = Entry(info, width=30, state="readonly", textvariable=cTratamiento)
        datosBoxT.place(x=170, y=260)

        imgamC = Image.open('images/btnAM.png')
        imgamC = ImageTk.PhotoImage(imgamC)
        btnAMC = Button(info, image=imgamC, borderwidth=0, bg="#EDF0F2",
                        command=lambda: [altaMedica(), close_window(info)])
        btnAMC.place(x=260, y=300)

        imgdC = Image.open('images/btnD.png')
        imgdC = ImageTk.PhotoImage(imgdC)
        btnDC = Button(info, image=imgdC, borderwidth=0, bg="#EDF0F2", command=lambda: selectPacient())
        btnDC.place(x=310, y=300)

        info.mainloop()

    def item_selected(e):

        for selected_item in tree.selection():
            # dictionary
            item = tree.item(selected_item)
            # list
            valor = item['values']

            nombreOpcion = item['text']
            imagen = item['image']
            abierto = item['open']

            if nombreOpcion == "Solicitar Atencion":
                ventanaAtencion()
            elif nombreOpcion == "Dashboard":
                dashboard()
            elif nombreOpcion == opcionGrafico:
                graficarDatos()
            elif nombreOpcion == "Analitica De Pacientes":
                analitica()
            elif nombreOpcion == "Altas Medicas":
                tablaAM()
            elif nombreOpcion == opcionPacientesIngresados:
                tratarPacientes()
            elif nombreOpcion == "Ordenamiento de Pacientes":
                ordenamiento()
            else:
                infoTree()

    # otra opcion para selecionar item del treeview
    def sele(e):
        selected = tree.selection()
        values = tree.item(selected, 'values')
        text = tree.item(selected, 'text')
        indexx = int(values[0])
        if text == listaEnlazada[indexx].getNombre():
            showinfo(title="Paciente " + listaEnlazada[indexx].getNombre(),
                     message="Tomado un hijo " + listaEnlazada[indexx].getNombre())

    inde = 0
    # crear el treeview
    tree = ttk.Treeview(root, height=20)
    # ubica el arbol en la raiz 
    tree.place(x=10, y=130)
    tree.heading('#0', text='Emergencias Medicas', anchor='w')

    _imgS = tk.PhotoImage(file="images/solTree.png")
    _imgG = tk.PhotoImage(file="images/grafTREE.png")
    _imgD = tk.PhotoImage(file="images/diagTREE.png")
    _imgA = tk.PhotoImage(file="images/altaTREE.png")
    tree.insert('', 'end', text='Solicitar Atencion', image=_imgS, iid=0, open=False)

    tree.insert('', tk.END, text=opcionPacientesIngresados, image=_imgD, iid=1000, open=False)
    tree.insert('', tk.END, text='Traumatologia', iid=2000, open=False)
    tree.insert('', tk.END, text='Neurologia', iid=3000, open=False)
    tree.insert('', tk.END, text='Cardiologia', iid=4000, open=False)

    tree.insert('', tk.END, text='Dashboard', image=_imgG, iid=5000, open=False)
    tree.insert('', tk.END, text=opcionGrafico, iid=5001, open=False)
    tree.insert('', tk.END, text='Analitica De Pacientes', iid=5002, open=False)
    tree.insert('', tk.END, text='Altas Medicas', image=_imgA, iid=5003, open=False)
    tree.insert('', tk.END, text='Ordenamiento de Pacientes', iid=5004, open=False)


    tree.move(2000, 1000, 0)
    tree.move(3000, 1000, 1)
    tree.move(4000, 1000, 2)

    tree.move(5001, 5000, 0)
    tree.move(5002, 5000, 1)
    tree.move(5004, 5000, 2)


    for i in range(0, listaEnlazada.contador()):
        if listaEnlazada[i].getDespacho() == "traumatologia":

            tree.insert('', tk.END, iid=i + 1, text=listaEnlazada[i].getNombre(), values=inde, open=False)
            tree.move(i + 1, 2000, i + 1)
        elif listaEnlazada[i].getDespacho() == "neurologia":

            tree.insert('', tk.END, iid=i + 1, text=listaEnlazada[i].getNombre(), values=inde, open=False)
            tree.move(i + 1, 3000, i + 1)
        elif listaEnlazada[i].getDespacho() == "cardiologia":

            tree.insert('', tk.END, iid=i + 1, text=listaEnlazada[i].getNombre(), values=inde, open=False)
            tree.move(i + 1, 4000, i + 1)

        inde = inde + 1

    # control de la opcion escogida
    tree.bind('<Double-1>', item_selected)
    root.mainloop()


def tratarPacientes():
    def actualizaColas():
        # marco
        marcoTrauma = LabelFrame(roott, text="Traumatologia", bd=4, width=290, height=330, bg="#EDF0F2")
        marcoTrauma.place(x=30, y=25)
        # estilo
        style = ttk.Style()
        style.configure('Treeview', background="#C0EAF8", foreground="black", fieldBackground="#C0EAF8")
        style.theme_use("default")
        style.map('Treeview', background=[('selected', '#DCA44C')])
        # creacion de tabla
        tablaT = ttk.Treeview(roott, columns=(0, 1, 2), show='headings', height=12)
        tablaT.place(x=50, y=50)
        tablaT.tag_configure('oddrow', background="#26C1F4")
        tablaT.tag_configure('evenrow', background="#C0EAF8")
        tablaT.heading(0, text="N°")
        tablaT.heading(1, text="Nombre")
        tablaT.heading(2, text="Rut")
        tablaT.column(0, width=10, minwidth=25)
        tablaT.column(1, width=120)
        tablaT.column(2, width=120)
        # scrollBar
        yscrollbar = ttk.Scrollbar(roott, orient="vertical", command=tablaT.yview)
        yscrollbar.place(x=300, y=50)
        # yscrollbar.place(x = 300, y =50, fill = Y)

        # =00=========================================================================================================================================
        # marco
        marcoNeuro = LabelFrame(roott, text="Neurologia", bd=4, width=290, height=330, bg="#EDF0F2")
        marcoNeuro.place(x=380, y=25)
        # estilo
        style = ttk.Style()
        style.configure('Treeview', background="#C0EAF8", foreground="black", fieldBackground="#C0EAF8")
        style.theme_use("default")
        style.map('Treeview', background=[('selected', '#DCA44C')])
        # creacion de tabla
        tablaN = ttk.Treeview(roott, columns=(0, 1, 2), show='headings', height=12)
        tablaN.pack(side="left")
        tablaN.place(x=400, y=50)
        tablaN.tag_configure('oddrow', background="#26C1F4")
        tablaN.tag_configure('evenrow', background="#C0EAF8")
        tablaN.heading(0, text="N°")
        tablaN.heading(1, text="Nombre")
        tablaN.heading(2, text="Rut")
        tablaN.column(0, width=10, minwidth=25)
        tablaN.column(1, width=120)
        tablaN.column(2, width=120)

        # scrollBar
        yscrollbar = ttk.Scrollbar(roott, orient="vertical", command=tablaN.yview)
        yscrollbar.place(x=650, y=50)
        # yscrollbar.place(x = 300, y =50, fill = Y)
        tablaN.configure(yscrollcommand=yscrollbar.set)

        # =======================================================================================================================
        # =00=========================================================================================================================================
        # marco
        marcoCardio = LabelFrame(roott, text="Cardiologia", bd=4, width=290, height=330, bg="#EDF0F2")
        marcoCardio.place(x=730, y=25)
        # estilo
        style = ttk.Style()
        style.configure('Treeview', background="#C0EAF8", foreground="black", fieldBackground="#C0EAF8")
        style.theme_use("default")
        style.map('Treeview', background=[('selected', '#DCA44C')])
        # creacion de tabla
        tablaC = ttk.Treeview(roott, columns=(0, 1, 2), show='headings', height=12)
        tablaC.pack(side="left")
        tablaC.place(x=750, y=50)
        tablaC.tag_configure('oddrow', background="#26C1F4")
        tablaC.tag_configure('evenrow', background="#C0EAF8")
        tablaC.heading(0, text="N°")
        tablaC.heading(1, text="Nombre")
        tablaC.heading(2, text="Rut")
        tablaC.column(0, width=10, minwidth=25)
        tablaC.column(1, width=120)
        tablaC.column(2, width=120)

        # scrollBar
        yscrollbar = ttk.Scrollbar(roott, orient="vertical", command=tablaC.yview)
        yscrollbar.place(x=1000, y=50)
        # yscrollbar.place(x = 300, y =50, fill = Y)
        tablaC.configure(yscrollcommand=yscrollbar.set)

        # agregando elementos
        index = 1
        t = 0
        c = 0
        n = 1
        for i in range(0, listaEnlazada.contador()):
            if listaEnlazada[i].getDespacho() == "traumatologia":
                if t % 2 == 0:
                    tablaT.insert(parent='', index=i, iid=i,
                                  values=(index, listaEnlazada[i].getNombre(), listaEnlazada[i].getRut()),
                                  tags=('evenrow'))

                else:
                    tablaT.insert(parent='', index=i, iid=i,
                                  values=(index, listaEnlazada[i].getNombre(), listaEnlazada[i].getRut()),
                                  tags=('oddrow'))

                t += 1
            elif listaEnlazada[i].getDespacho() == "cardiologia":
                if index % 2 == 0:
                    tablaC.insert(parent='', index=i, iid=i,
                                  values=(index, listaEnlazada[i].getNombre(), listaEnlazada[i].getRut()),
                                  tags=('evenrow'))

                else:
                    tablaC.insert(parent='', index=i, iid=i,
                                  values=(index, listaEnlazada[i].getNombre(), listaEnlazada[i].getRut()),
                                  tags=('oddrow'))
                c += 1
            else:
                if index % 2 == 0:
                    tablaN.insert(parent='', index=i, iid=i,
                                  values=(index, listaEnlazada[i].getNombre(), listaEnlazada[i].getRut()),
                                  tags=('evenrow'))

                else:
                    tablaN.insert(parent='', index=i, iid=i,
                                  values=(index, listaEnlazada[i].getNombre(), listaEnlazada[i].getRut()),
                                  tags=('oddrow'))
                n += 1

            index += 1

        # botones Trauma
        imgL = Image.open('images/btnAM.png')
        imgL = ImageTk.PhotoImage(imgL)
        btnAM = Button(roott, image=imgL, borderwidth=0, bg="#EDF0F2", command=lambda: [altaMedica(tablaT), showInfo()])
        btnAM.place(x=265, y=310)

        img = Image.open('images/btnD.png')
        img = ImageTk.PhotoImage(img)
        btnD = Button(roott, image=img, borderwidth=0, bg="#EDF0F2", command=lambda: selectPacient(tablaT))
        btnD.place(x=225, y=310)

        imgC = Image.open('images/btnInfo.png')
        imgC = ImageTk.PhotoImage(imgC)
        btnC = Button(roott, image=imgC, borderwidth=0, bg="#EDF0F2", command=lambda: [info(tablaT)])
        btnC.place(x=185, y=310)

        # botones Neurologia

        imgamN = Image.open('images/btnAM.png')
        imgamN = ImageTk.PhotoImage(imgamN)
        btnAMN = Button(roott, image=imgamN, borderwidth=0, bg="#EDF0F2",
                        command=lambda: [altaMedica(tablaN), showInfo()])
        btnAMN.place(x=620, y=310)

        imgdn = Image.open('images/btnD.png')
        imgdn = ImageTk.PhotoImage(imgdn)
        btnDn = Button(roott, image=imgdn, borderwidth=0, bg="#EDF0F2", command=lambda: selectPacient(tablaN))
        btnDn.place(x=580, y=310)

        imgmn = Image.open('images/btnInfo.png')
        imgmn = ImageTk.PhotoImage(imgmn)
        btnMn = Button(roott, image=imgmn, borderwidth=0, bg="#EDF0F2", command=lambda: [info(tablaN)])
        btnMn.place(x=540, y=310)

        # botones Cradiologia

        imgamC = Image.open('images/btnAM.png')
        imgamC = ImageTk.PhotoImage(imgamC)
        btnAMC = Button(roott, image=imgamC, borderwidth=0, bg="#EDF0F2",
                        command=lambda: [altaMedica(tablaC), showInfo()])
        btnAMC.place(x=970, y=310)

        imgdC = Image.open('images/btnD.png')
        imgdC = ImageTk.PhotoImage(imgdC)
        btnDC = Button(roott, image=imgdC, borderwidth=0, bg="#EDF0F2", command=lambda: selectPacient(tablaC))
        btnDC.place(x=930, y=310)

        imgmC = Image.open('images/btnInfo.png')
        imgmC = ImageTk.PhotoImage(imgmC)
        btnMC = Button(roott, image=imgmC, borderwidth=0, bg="#EDF0F2", command=lambda: [info(tablaC)])
        btnMC.place(x=890, y=310)

        roott.mainloop()

    def selectPacient(tabla):

        def close_window(root):
            root.destroy()

        def guardaT():
            listaEnlazada[index].setDiagnostico(diagnostico.get())
            listaEnlazada[index].setTratamiento(tratamiento.get("1.0", "end"))

        top = Toplevel(roott)
        top.geometry("350x270")
        top.title("Diagnostico")
        header = Frame(top, width=500, height=120)
        header.pack()
        body = Frame(top, width=500, height=380, bg="#00B8FF")
        body.pack()

        selected = tabla.focus()
        values = tabla.item(selected, 'values')
        indexx = int(values[0])
        index = indexx - 1

        tk.Label(top, text="Diagnostico:").place(x=125, y=10)
        diagnostico = tk.Entry(top, width=40)
        diagnostico.place(x=50, y=30)

        tk.Label(top, text="Tratamiento:").place(x=125, y=50)
        tratamiento = tk.Text(top, height=5, width=25, padx=15, pady=15)
        tratamiento.place(x=50, y=70)

        imgAgrega = Image.open('images/solAtenAgregar.png')
        imgAgrega = ImageTk.PhotoImage(imgAgrega)
        agrega = Button(top, image=imgAgrega, borderwidth=0, bg="#00B8FF",
                        command=lambda: [guardaT(), close_window(top)])
        agrega.place(x=210, y=200)

        imgBac = Image.open('images/solAtenAtras.png')
        imgBac = ImageTk.PhotoImage(imgBac)
        bac = Button(top, image=imgBac, borderwidth=0, bg="#00B8FF", command=lambda: close_window(top))
        bac.place(x=280, y=200)
        # guardaB = Button(top, text="Diagnosticar", width=50, bg = "#00B8FF", command=lambda: [print(index), guardaT(), close_window(top)])
        # guardaB.pack(pady = 5)

        top.mainloop()

    def altaMedica(tabla):

        selected = tabla.focus()
        values = tabla.item(selected, 'values')
        indexx = int(values[0])
        index = indexx - 1
        listaEnlazada[index].setaltaMedica()

        listaPacientesAM.adicionarFinal(
            Paciente(listaEnlazada[index].getNombre(), listaEnlazada[index].getRut(), listaEnlazada[index].getSexo(),
                     listaEnlazada[index].getEdad(), listaEnlazada[index].getDiagnosticoI(),
                     listaEnlazada[index].getEstado(), listaEnlazada[index].getDespacho(), True,
                     listaEnlazada[index].getNombreM(), listaEnlazada[index].getRutM(),
                     listaEnlazada[index].getDiagnostico(), listaEnlazada[index].getTratamiento(),
                     listaEnlazada[index].getIdEspecialista(), listaEnlazada[index].getNombreEspecialidad()))

        rutActual = listaEnlazada[index].getRut()
        listaEnlazada.borrarPorRut(rutActual)

    def showInfo():
        resp = messagebox.showinfo("Info", "Alta Medica Completa\n\n", parent=roott)
        if resp == "ok":
            actualizaColas()

    roott = Toplevel()
    roott.title("Tratar Paciente")
    roott.geometry("1100x400")
    header = Frame(roott, width=1200, height=120, bg="white")
    header.pack()
    body = Frame(roott, width=1200, height=380, bg="#00B8FF")
    body.pack()

    # marco
    marcoTrauma = LabelFrame(roott, text="Traumatologia", bd=4, width=290, height=330, bg="#EDF0F2")
    marcoTrauma.place(x=30, y=25)
    # estilo
    style = ttk.Style()
    style.configure('Treeview', background="#C0EAF8", foreground="black", fieldBackground="#C0EAF8")
    style.theme_use("default")
    style.map('Treeview', background=[('selected', '#DCA44C')])
    # creacion de tabla
    tablaT = ttk.Treeview(roott, columns=(0, 1, 2), show='headings', height=12)
    tablaT.place(x=50, y=50)
    tablaT.tag_configure('oddrow', background="#26C1F4")
    tablaT.tag_configure('evenrow', background="#C0EAF8")
    tablaT.heading(0, text="N°")
    tablaT.heading(1, text="Nombre")
    tablaT.heading(2, text="Rut")
    tablaT.column(0, width=10, minwidth=25)
    tablaT.column(1, width=120)
    tablaT.column(2, width=120)
    # scrollBar
    yscrollbar = ttk.Scrollbar(roott, orient="vertical", command=tablaT.yview)
    yscrollbar.place(x=300, y=50)
    # yscrollbar.place(x = 300, y =50, fill = Y)

    # =00=========================================================================================================================================
    # marco
    marcoNeuro = LabelFrame(roott, text="Neurologia", bd=4, width=290, height=330, bg="#EDF0F2")
    marcoNeuro.place(x=380, y=25)
    # estilo
    style = ttk.Style()
    style.configure('Treeview', background="#C0EAF8", foreground="black", fieldBackground="#C0EAF8")
    style.theme_use("default")
    style.map('Treeview', background=[('selected', '#DCA44C')])
    # creacion de tabla
    tablaN = ttk.Treeview(roott, columns=(0, 1, 2), show='headings', height=12)
    tablaN.pack(side="left")
    tablaN.place(x=400, y=50)
    tablaN.tag_configure('oddrow', background="#26C1F4")
    tablaN.tag_configure('evenrow', background="#C0EAF8")
    tablaN.heading(0, text="N°")
    tablaN.heading(1, text="Nombre")
    tablaN.heading(2, text="Rut")
    tablaN.column(0, width=10, minwidth=25)
    tablaN.column(1, width=120)
    tablaN.column(2, width=120)

    # scrollBar
    yscrollbar = ttk.Scrollbar(roott, orient="vertical", command=tablaN.yview)
    yscrollbar.place(x=650, y=50)
    # yscrollbar.place(x = 300, y =50, fill = Y)
    tablaN.configure(yscrollcommand=yscrollbar.set)

    # =======================================================================================================================
    # =00=========================================================================================================================================
    # marco
    marcoCardio = LabelFrame(roott, text="Cardiologia", bd=4, width=290, height=330, bg="#EDF0F2")
    marcoCardio.place(x=730, y=25)
    # estilo
    style = ttk.Style()
    style.configure('Treeview', background="#C0EAF8", foreground="black", fieldBackground="#C0EAF8")
    style.theme_use("default")
    style.map('Treeview', background=[('selected', '#DCA44C')])
    # creacion de tabla
    tablaC = ttk.Treeview(roott, columns=(0, 1, 2), show='headings', height=12)
    tablaC.pack(side="left")
    tablaC.place(x=750, y=50)
    tablaC.tag_configure('oddrow', background="#26C1F4")
    tablaC.tag_configure('evenrow', background="#C0EAF8")
    tablaC.heading(0, text="N°")
    tablaC.heading(1, text="Nombre")
    tablaC.heading(2, text="Rut")
    tablaC.column(0, width=10, minwidth=25)
    tablaC.column(1, width=120)
    tablaC.column(2, width=120)

    # scrollBar
    yscrollbar = ttk.Scrollbar(roott, orient="vertical", command=tablaC.yview)
    yscrollbar.place(x=1000, y=50)
    # yscrollbar.place(x = 300, y =50, fill = Y)
    tablaC.configure(yscrollcommand=yscrollbar.set)

    # agregando elementos
    index = 1
    t = 0
    c = 0
    n = 1
    for i in range(0, listaEnlazada.contador()):
        if listaEnlazada[i].getDespacho() == "traumatologia":
            if t % 2 == 0:
                tablaT.insert(parent='', index=i, iid=i,
                              values=(index, listaEnlazada[i].getNombre(), listaEnlazada[i].getRut()), tags=('evenrow'))

            else:
                tablaT.insert(parent='', index=i, iid=i,
                              values=(index, listaEnlazada[i].getNombre(), listaEnlazada[i].getRut()), tags=('oddrow'))

            t += 1
        elif listaEnlazada[i].getDespacho() == "cardiologia":
            if index % 2 == 0:
                tablaC.insert(parent='', index=i, iid=i,
                              values=(index, listaEnlazada[i].getNombre(), listaEnlazada[i].getRut()), tags=('evenrow'))

            else:
                tablaC.insert(parent='', index=i, iid=i,
                              values=(index, listaEnlazada[i].getNombre(), listaEnlazada[i].getRut()), tags=('oddrow'))
            c += 1
        else:
            if index % 2 == 0:
                tablaN.insert(parent='', index=i, iid=i,
                              values=(index, listaEnlazada[i].getNombre(), listaEnlazada[i].getRut()), tags=('evenrow'))

            else:
                tablaN.insert(parent='', index=i, iid=i,
                              values=(index, listaEnlazada[i].getNombre(), listaEnlazada[i].getRut()), tags=('oddrow'))
            n += 1

        index += 1

    # botones Trauma
    imgL = Image.open('images/btnAM.png')
    imgL = ImageTk.PhotoImage(imgL)
    btnAM = Button(roott, image=imgL, borderwidth=0, bg="#EDF0F2", command=lambda: [altaMedica(tablaT), showInfo()])
    btnAM.place(x=265, y=310)

    img = Image.open('images/btnD.png')
    img = ImageTk.PhotoImage(img)
    btnD = Button(roott, image=img, borderwidth=0, bg="#EDF0F2", command=lambda: selectPacient(tablaT))
    btnD.place(x=225, y=310)

    imgC = Image.open('images/btnInfo.png')
    imgC = ImageTk.PhotoImage(imgC)
    btnC = Button(roott, image=imgC, borderwidth=0, bg="#EDF0F2", command=lambda: [info(tablaT)])
    btnC.place(x=185, y=310)

    # botones Neurologia

    imgamN = Image.open('images/btnAM.png')
    imgamN = ImageTk.PhotoImage(imgamN)
    btnAMN = Button(roott, image=imgamN, borderwidth=0, bg="#EDF0F2", command=lambda: [altaMedica(tablaN), showInfo()])
    btnAMN.place(x=620, y=310)

    imgdn = Image.open('images/btnD.png')
    imgdn = ImageTk.PhotoImage(imgdn)
    btnDn = Button(roott, image=imgdn, borderwidth=0, bg="#EDF0F2", command=lambda: selectPacient(tablaN))
    btnDn.place(x=580, y=310)

    imgmn = Image.open('images/btnInfo.png')
    imgmn = ImageTk.PhotoImage(imgmn)
    btnMn = Button(roott, image=imgmn, borderwidth=0, bg="#EDF0F2", command=lambda: [info(tablaN)])
    btnMn.place(x=540, y=310)

    # botones Cradiologia

    imgamC = Image.open('images/btnAM.png')
    imgamC = ImageTk.PhotoImage(imgamC)
    btnAMC = Button(roott, image=imgamC, borderwidth=0, bg="#EDF0F2", command=lambda: [altaMedica(tablaC), showInfo()])
    btnAMC.place(x=970, y=310)

    imgdC = Image.open('images/btnD.png')
    imgdC = ImageTk.PhotoImage(imgdC)
    btnDC = Button(roott, image=imgdC, borderwidth=0, bg="#EDF0F2", command=lambda: selectPacient(tablaC))
    btnDC.place(x=930, y=310)

    imgmC = Image.open('images/btnInfo.png')
    imgmC = ImageTk.PhotoImage(imgmC)
    btnMC = Button(roott, image=imgmC, borderwidth=0, bg="#EDF0F2", command=lambda: [info(tablaC)])
    btnMC.place(x=890, y=310)

    roott.mainloop()


def ventanaAtencion():
    def close_window(root):
        root.destroy()

    def distribuirListas(nombre, rut, sexo, Edad, diagI, estado, despacho):

        if len(nombre) == 0 or len(rut) == 0 or len(Edad) == 0:
            messagebox.showerror("Error", "Todos Los Campos Son Obligatorios", parent=root)
        else:

            listaEnlazada.adicionarFinal(
                Paciente(nombre, rut, sexo, Edad, diagI, estado, despacho, False, medico[0], medico[1], medico[2],
                         medico[3], medico[4], medico[5]))

            # listaCompleta.agregar(Paciente(nombre,rut,sexo,Edad,diagI,estado,despacho,False    ,medico[0],medico[1],medico[2],medico[3],medico[4],medico[5]))

            if despacho == "traumatologia":
                listaTrauma.adicionarFinal(
                    Paciente(nombre, rut, sexo, Edad, diagI, estado, despacho, False, "", "", "", "", "", ""))
            elif despacho == "neurologia":
                listaNeuro.adicionarFinal(
                    Paciente(nombre, rut, sexo, Edad, diagI, estado, despacho, False, "", "", "", "", "", ""))
            elif despacho == "cardiologia":
                listaCardio.adicionarFinal(
                    Paciente(nombre, rut, sexo, Edad, diagI, estado, despacho, False, "", "", "", "", "", ""))

            res = messagebox.showinfo("Info", "Paciente Registrado", parent=root)
            if res == "ok":
                close_window(root)

    root = Toplevel()
    root.title("Solicitar Atencion")
    root.geometry("450x350")

    header = Frame(root, width=450, height=117)
    header.pack()

    # cuerpo
    body = Frame(root, width=450, height=233, bg="#00B8FF")
    body.pack()

    sexos = ["masculino", "femenino", "otro"]
    estados = ["reanimacion", "emergencia", "urgencia", "prioritario", "no urgencia"]
    dIniciales = ["1-Hemorragia Traumática", "2-Impacto de bala", "3-Fractura ósea", "4-Infección bacteriana", "5-otro"]

    # labels

    Label(root, text="Nombre:").place(x=40, y=30)
    nombre = Entry(root, width=40)
    nombre.focus()
    nombre.place(x=170, y=30)

    Label(root, text="Rut:").place(x=40, y=60)
    rut = Entry(root, width=40)
    rut.place(x=170, y=60)

    Label(root, text="Sexo:").place(x=40, y=90)
    sexo = Spinbox(root, values=sexos)
    sexo.place(x=170, y=90)

    Label(root, text="Edad:", bg="#00B8FF").place(x=40, y=120)
    Edad = Entry(root, width=40)
    Edad.place(x=170, y=120)

    Label(root, text="Diagnostico Inicial:", bg="#00B8FF").place(x=40, y=150)
    diagI = Spinbox(root, values=dIniciales, width=30)
    diagI.place(x=170, y=150)

    Label(root, text="Estado:", bg="#00B8FF").place(x=40, y=180)
    estado = Spinbox(root, values=estados)
    estado.place(x=170, y=180)

    Label(root, text="Despacho:", bg="#00B8FF").place(x=40, y=210)

    despacho = StringVar()
    trauma = Radiobutton(root, text="Traumatologia", variable=despacho, value="traumatologia", bg="#00B8FF")
    trauma.place(x=170, y=210)
    trauma.select()

    neuro = Radiobutton(root, text="Neurologia", variable=despacho, value="neurologia", bg="#00B8FF")
    neuro.place(x=170, y=230)

    cardio = Radiobutton(root, text="Cardiologia", variable=despacho, value="cardiologia", bg="#00B8FF")
    cardio.place(x=170, y=250)

    imgAgregar = Image.open('images/solAtenAgregar.png')
    imgAgregar = ImageTk.PhotoImage(imgAgregar)
    agregar = Button(root, image=imgAgregar, borderwidth=0, bg="#00B8FF", command=lambda: [
        distribuirListas(nombre.get(), rut.get(), sexo.get(), Edad.get(), diagI.get(), estado.get(),
                         despacho.get()), ActualizaTabla()])
    agregar.place(x=350, y=280)

    imgBack = Image.open('images/solAtenAtras.png')
    imgBack = ImageTk.PhotoImage(imgBack)
    back = Button(root, image=imgBack, borderwidth=0, bg="#00B8FF", command=lambda: [close_window(root)])
    back.place(x=280, y=280)

    root.mainloop()


def info(tabla):
    def close_window(root):
        root.destroy()

    def showInfo():
        messagebox.showerror("Error", "Todos los campos son obligatorios", parent=info)

    def setInfo(nombre, rut, sexo, diagI, Edad, estado):
        if len(nombre) == 0 or len(rut) == 0 or len(Edad) == 0:
            showInfo()
        else:

            listaEnlazada[index].setNombre(nombre)
            listaEnlazada[index].setRut(rut)
            listaEnlazada[index].setSexo(sexo)
            listaEnlazada[index].setDiagnosticoI(diagI)
            listaEnlazada[index].setEdad(Edad)
            listaEnlazada[index].setEstado(estado)

            cNom.set(listaEnlazada[index].getNombre())
            cRut.set(listaEnlazada[index].getRut())
            cEstado.set(listaEnlazada[index].getEstado())
            cDiagI.set(listaEnlazada[index].getDiagnosticoI())
            cSexo.set(listaEnlazada[index].getSexo())
            cEdad.set(listaEnlazada[index].getEdad())
            messagebox.showinfo("Info", "Datos Cambiados Correctamente\n\n Actualice Para Reflejar Cambios En Tabla",
                                parent=info)

    def delete(nombre, rut, Edad):
        nombre.delete(0, 'end')
        rut.delete(0, 'end')
        Edad.delete(0, 'end')

    cNom = StringVar()
    cRut = StringVar()
    cEstado = StringVar()
    cDiagI = StringVar()
    cSexo = StringVar()
    cEdad = StringVar()

    selected = tabla.focus()
    values = tabla.item(selected, 'values')
    indexx = int(values[0])
    index = indexx - 1

    cNom.set(listaEnlazada[index].getNombre())
    cRut.set(listaEnlazada[index].getRut())
    cEstado.set(listaEnlazada[index].getEstado())
    cDiagI.set(listaEnlazada[index].getDiagnosticoI())
    cSexo.set(listaEnlazada[index].getSexo())
    cEdad.set(listaEnlazada[index].getEdad())

    info = Toplevel()
    info.title("Paciente " + listaEnlazada[index].getNombre())
    info.geometry("500x420")
    header = Frame(info, width=550, height=120)
    header.pack()
    body = Frame(info, width=550, height=380, bg="#00B8FF")
    body.pack()

    Label(info, text="Nombre:").place(x=40, y=30)
    nombre = Entry(info, width=30, state="readonly", textvariable=cNom)
    nombre.focus()
    nombre.place(x=170, y=30)

    Label(info, text="Rut:").place(x=40, y=60)
    rut = Entry(info, width=30, state="readonly", textvariable=cRut)
    rut.place(x=170, y=60)

    Label(info, text="Sexo:").place(x=40, y=90)
    sexo = Entry(info, width=30, state="readonly", textvariable=cSexo)
    sexo.place(x=170, y=90)

    Label(info, text="Edad:", bg="#00B8FF").place(x=40, y=120)
    Edad = Entry(info, width=30, state="readonly", textvariable=cEdad)
    Edad.place(x=170, y=120)

    Label(info, text="Diagnostico Inicial:", bg="#00B8FF").place(x=40, y=150)
    diagI = Entry(info, width=30, state="readonly", textvariable=cDiagI)
    diagI.place(x=170, y=150)

    Label(info, text="Estado:", bg="#00B8FF").place(x=40, y=180)
    estado = Entry(info, width=30, state="readonly", textvariable=cEstado)
    estado.place(x=170, y=180)

    marco = LabelFrame(info, text="Modificar", bd=4, width=480, height=150, bg="#EDF0F2")
    marco.place(x=10, y=220)

    sexos = ["masculino", "femenino", "otro"]
    estados = ["reanimacion", "emergencia", "urgencia", "prioritario", "no urgencia"]
    dIniciales = ["1-Hemorragia Traumática", "2-Impacto de bala", "3-Fractura ósea", "4-Infección bacteriana", "5-otro"]

    # labels

    Label(info, text="Nombre:").place(x=20, y=240)
    nombre = Entry(info, width=15)
    nombre.focus()
    nombre.place(x=80, y=240)

    Label(info, text="Rut:").place(x=180, y=240)
    rut = Entry(info, width=15)
    rut.place(x=210, y=240)

    Label(info, text="Sexo:").place(x=310, y=240)
    sexo = Spinbox(info, values=sexos, width=10)
    sexo.place(x=350, y=240)

    Label(info, text="Edad:").place(x=20, y=280)
    Edad = Entry(info, width=15)
    Edad.place(x=80, y=280)

    Label(info, text="Estado:").place(x=180, y=280)
    estado = Spinbox(info, values=estados, width=15)
    estado.place(x=230, y=280)

    Label(info, text="Diag. Inicial:").place(x=20, y=320)
    diagI = Spinbox(info, values=dIniciales, width=37)
    diagI.place(x=100, y=320)

    imgAgrega = Image.open('images/btnAM.png')
    imgAgrega = ImageTk.PhotoImage(imgAgrega)
    agrega = Button(info, image=imgAgrega, borderwidth=0, command=lambda: [
        setInfo(nombre.get(), rut.get(), sexo.get(), diagI.get(), Edad.get(), estado.get()),
        delete(nombre, rut, Edad)])
    agrega.place(x=400, y=310)

    imgBac = Image.open('images/solAtenAtras.png')
    imgBac = ImageTk.PhotoImage(imgBac)
    bac = Button(info, image=imgBac, borderwidth=0, bg="#00B8FF", command=lambda: close_window(info))
    bac.place(x=410, y=370)

    info.mainloop()


def ActualizaTabla():
    # =================================================================
    treeInit()


def dashboard():
    def mayor():
        if listaTrauma.contador() > listaNeuro.contador() and listaTrauma.contador() > listaCardio.contador():
            return "(Traumatologia)"
        elif listaNeuro.contador() > listaCardio.contador() and listaNeuro.contador() > listaTrauma.contador():
            return "(Neurologia)"
        elif listaCardio.contador() > listaNeuro.contador() and listaCardio.contador() > listaTrauma.contador():
            return "(Cardiologia)"
        else:
            return ""

    def menor():
        if listaTrauma.contador() < listaNeuro.contador() and listaTrauma.contador() < listaCardio.contador():
            return "(Traumatologia)"
        elif listaNeuro.contador() < listaCardio.contador() and listaNeuro.contador() < listaTrauma.contador():
            return "(Neurologia)"
        elif listaCardio.contador() < listaNeuro.contador() and listaCardio.contador() < listaTrauma.contador():
            return "(Cardiologia)"
        else:
            return ""

        cont = 0
        for x in range(0, listaEnlazada.contador()):
            if listaEnlazada[x].getDiagnosticoI() == "1-Hemorragia Traumática":
                cont = cont + 1
        return cont

    def contDiagnostico():
        tipo1 = 0
        tipo2 = 0
        tipo3 = 0
        tipo4 = 0
        tipo5 = 0
        for x in range(0, listaEnlazada.contador()):
            if listaEnlazada[x].getDiagnosticoI() == "1-Hemorragia Traumática":
                tipo1 = tipo1 + 1
            elif listaEnlazada[x].getDiagnosticoI() == "2-Impacto de bala":
                tipo2 = tipo2 + 1
            elif listaEnlazada[x].getDiagnosticoI() == "3-Fractura ósea":
                tipo3 = tipo3 + 1
            elif listaEnlazada[x].getDiagnosticoI() == "4-Infección bacteriana":
                tipo4 = tipo4 + 1
            elif listaEnlazada[x].getDiagnosticoI() == "5-otro":
                tipo5 = tipo5 + 1

        result = "Hemorragia Traumatica: " + str(tipo1)
        re = "\nImpacto de bala: " + str(tipo2) + "\nFractura Osea: " + str(tipo3) + "\nInfeccion bacteriana: " + str(
            tipo4) + "\nOtro: " + str(tipo5)
        return result + re

    trauma = np.array(listaTrauma.contador()).astype(int)

    neuro = np.array(listaNeuro.contador()).astype(int)

    cardio = np.array(listaCardio.contador()).astype(int)

    totalPacientes = [listaTrauma.contador(), listaNeuro.contador(), listaCardio.contador()]

    # -------- ESTADISTICAS TODOS LOS Pacientes

    mayorTodos = np.max(totalPacientes)  # Valor máximo de los elementos del array

    menorTodos = np.min(totalPacientes)  # Valor mínimo de los elementos del array

    mediaTodos = np.mean(totalPacientes)  # Valor medio de los elementos del array

    stdTodos = np.std(totalPacientes)  # Desviación típica de los elementos del array

    sumaTodos = np.sum(totalPacientes)  # Suma de todos los elementos del array

    # -------- ESTADISTICAS CADA TIPO

    mediaTrauma = trauma.mean()

    mediaNeuro = neuro.mean()

    mediaCardio = cardio.mean()

    Txt_1 = StringVar()

    Txt_2 = StringVar()

    Txt_3 = StringVar()

    Txt_4 = StringVar()

    Txt_5 = StringVar()

    Txt_7 = StringVar()

    Txt_8 = StringVar()

    Txt_9 = StringVar()

    Txt_0 = StringVar()

    txtHT = StringVar()

    popup = Toplevel()

    popup.geometry("1150x450")

    popup.wm_title("Análitica de Pacientes")
    popup.configure(bg="#C0EAF8")

    Txt_0.set("Análitica De Pacientes \nPor Especialidad")

    Txt_1.set("Mayor: " + str(mayorTodos) + "  " + str(mayor()))

    Txt_2.set("Menor: " + str(menorTodos) + "  " + str(menor()))

    Txt_3.set("Media: " + str(mediaTodos))

    Txt_4.set("Std: " + str(stdTodos))

    Txt_5.set("Total: " + str(sumaTodos))

    Txt_7.set("Promedio Traumatologia: " + str(mediaTrauma))

    Txt_8.set("Promedio Neurologia: " + str(mediaNeuro))

    Txt_9.set("Promedio Cardiologia: " + str(mediaCardio))

    txtHT.set(contDiagnostico())

    mayorE = Frame(popup, width=320, height=340, bg="#00B8FF")
    mayorE.place(x=20, y=20)

    Frame(popup, width=320, height=60, bg="light grey").place(x=20, y=20)

    Label(popup, textvariable=Txt_0, bg="light grey", fg="black", font=("Cascadia Code PL SemiBold", 12)).place(x=30,
                                                                                                                y=30)

    Label(popup, textvariable=Txt_1, bg="#00B8FF", fg="black", height=1, font=("Cascadia Code PL SemiBold", 10)).place(
        x=30, y=90)
    Label(popup, textvariable=Txt_2, bg="#00B8FF", fg="black", height=1, font=("Cascadia Code PL SemiBold", 10)).place(
        x=30, y=110)
    Label(popup, textvariable=Txt_5, bg="#00B8FF", fg="black", height=1, font=("Cascadia Code PL SemiBold", 10)).place(
        x=30, y=130)
    Label(popup, textvariable=Txt_3, bg="#00B8FF", fg="black", height=1, font=("Cascadia Code PL SemiBold", 10)).place(
        x=30, y=150)
    Label(popup, textvariable=Txt_4, bg="#00B8FF", fg="black", height=1, font=("Cascadia Code PL SemiBold", 10)).place(
        x=30, y=170)
    Label(popup, textvariable=Txt_7, bg="#00B8FF", fg="black", height=1, font=("Cascadia Code PL SemiBold", 10)).place(
        x=30, y=190)
    Label(popup, textvariable=Txt_8, bg="#00B8FF", fg="black", height=1, font=("Cascadia Code PL SemiBold", 10)).place(
        x=30, y=210)
    Label(popup, textvariable=Txt_9, bg="#00B8FF", fg="black", height=1, font=("Cascadia Code PL SemiBold", 10)).place(
        x=30, y=230)
    # Label(popup, text =  "Pacientes Por Diag. Inicial",bg = "#00B8FF", fg="red",height = 1,font=("Cascadia Code PL SemiBold",11) ).place(x=30,y=180)
    # Label(popup, text = "Hemorragia Traumática: ",bg = "#00B8FF", fg="black",font=("Cascadia Code PL SemiBold",10) ).place(x=30,y=210)
    Label(popup, textvariable=txtHT, bg="#00B8FF", fg="black", font=("Cascadia Code PL SemiBold", 10)).place(x=30,
                                                                                                             y=250)

    # imgI = Image.open('images/grafico.png')
    # imgI = ImageTk.PhotoImage(imgI)
    # listaE = Button(popup, image=imgI, bg="#C0EAF8",borderwidth=0,command=lambda: [graficarDatos()] )
    # listaE.place(x=470,y=373)

    # =======================

    marcoTodos = LabelFrame(popup, text="Pacientes Con Alta Medica", bd=4, width=290, height=318, bg="#EDF0F2")
    marcoTodos.place(x=370, y=30)
    # estilo
    style = ttk.Style()
    style.configure('Treeview', background="#C0EAF8", foreground="black", fieldBackground="#C0EAF8")
    style.theme_use("default")
    style.map('Treeview', background=[('selected', '#DCA44C')])
    # creacion de tabla
    tablaTodos = ttk.Treeview(popup, columns=(0, 1, 2), show='headings', height=12)
    tablaTodos.place(x=385, y=55)
    tablaTodos.tag_configure('oddrow', background="#26C1F4")
    tablaTodos.tag_configure('evenrow', background="#C0EAF8")
    tablaTodos.heading(0, text="N°")
    tablaTodos.heading(1, text="Nombre")
    tablaTodos.heading(2, text="Rut")
    tablaTodos.column(0, width=10, minwidth=25)
    tablaTodos.column(1, width=120)
    tablaTodos.column(2, width=120)

    # agregando elementos
    index = 1
    for i in range(0, listaPacientesAM.contador()):

        if index % 2 == 0:
            tablaTodos.insert(parent='', index=i, iid=i,
                              values=(index, listaPacientesAM[i].getNombre(), listaPacientesAM[i].getRut()),
                              tags=('evenrow'))

        else:
            tablaTodos.insert(parent='', index=i, iid=i,
                              values=(index, listaPacientesAM[i].getNombre(), listaPacientesAM[i].getRut()),
                              tags=('oddrow'))

        index += 1

    fig = plt.Figure(figsize=(4, 4))
    a = fig.add_subplot(111)
    a.pie([listaTrauma.contador(), listaNeuro.contador(), listaCardio.contador()])  # an example data
    a.legend(["TRAUMATOLOGIA", "NEUROLOGIA", "CARDIOLOGIA"], prop={'size': 9}, bbox_to_anchor=(1.1, 0.1))
    a.set_title("Pacientes Ingresados")
    canvas = FigureCanvasTkAgg(fig, master=popup)
    canvas.get_tk_widget().place(x=700, y=30)
    canvas.draw()

    popup.mainloop()


def graficarDatos():
    tT = []

    tT.append(listaCardio.contador())

    tT.append(listaTrauma.contador())

    tT.append(listaNeuro.contador())

    pl.pie(tT, labels=["Cardiologia", "Traumalogia", "Neurologia"])

    pl.title("PACIENTES INGRESADOS")

    pl.show()


def analitica():
    def mayor():
        if listaTrauma.contador() > listaNeuro.contador() and listaTrauma.contador() > listaCardio.contador():
            return "(Traumatologia)"
        elif listaNeuro.contador() > listaCardio.contador() and listaNeuro.contador() > listaTrauma.contador():
            return "(Neurologia)"
        elif listaCardio.contador() > listaNeuro.contador() and listaCardio.contador() > listaTrauma.contador():
            return "(Cardiologia)"
        else:
            return ""

    def menor():
        if listaTrauma.contador() < listaNeuro.contador() and listaTrauma.contador() < listaCardio.contador():
            return "(Traumatologia)"
        elif listaNeuro.contador() < listaCardio.contador() and listaNeuro.contador() < listaTrauma.contador():
            return "(Neurologia)"
        elif listaCardio.contador() < listaNeuro.contador() and listaCardio.contador() < listaTrauma.contador():
            return "(Cardiologia)"
        else:
            return ""

        cont = 0
        for x in range(0, listaEnlazada.contador()):
            if listaEnlazada[x].getDiagnosticoI() == "1-Hemorragia Traumática":
                cont = cont + 1
        return cont

    def contDiagnostico():
        tipo1 = 0
        tipo2 = 0
        tipo3 = 0
        tipo4 = 0
        tipo5 = 0
        for x in range(0, listaEnlazada.contador()):
            if listaEnlazada[x].getDiagnosticoI() == "1-Hemorragia Traumática":
                tipo1 = tipo1 + 1
            elif listaEnlazada[x].getDiagnosticoI() == "2-Impacto de bala":
                tipo2 = tipo2 + 1
            elif listaEnlazada[x].getDiagnosticoI() == "3-Fractura ósea":
                tipo3 = tipo3 + 1
            elif listaEnlazada[x].getDiagnosticoI() == "4-Infección bacteriana":
                tipo4 = tipo4 + 1
            elif listaEnlazada[x].getDiagnosticoI() == "5-otro":
                tipo5 = tipo5 + 1

        result = "Hemorragia Traumatica: " + str(tipo1)
        re = "\nImpacto de bala: " + str(tipo2) + "\nFractura Osea: " + str(tipo3) + "\nInfeccion bacteriana: " + str(
            tipo4) + "\nOtro: " + str(tipo5)
        return result + re

    trauma = np.array(listaTrauma.contador()).astype(int)

    neuro = np.array(listaNeuro.contador()).astype(int)

    cardio = np.array(listaCardio.contador()).astype(int)

    totalPacientes = [listaTrauma.contador(), listaNeuro.contador(), listaCardio.contador()]

    # -------- ESTADISTICAS TODOS LOS Pacientes

    mayorTodos = np.max(totalPacientes)  # Valor máximo de los elementos del array

    menorTodos = np.min(totalPacientes)  # Valor mínimo de los elementos del array

    mediaTodos = np.mean(totalPacientes)  # Valor medio de los elementos del array

    stdTodos = np.std(totalPacientes)  # Desviación típica de los elementos del array

    sumaTodos = np.sum(totalPacientes)  # Suma de todos los elementos del array

    # -------- ESTADISTICAS CADA TIPO

    mediaTrauma = trauma.mean()

    mediaNeuro = neuro.mean()

    mediaCardio = cardio.mean()

    Txt_1 = StringVar()

    Txt_2 = StringVar()

    Txt_3 = StringVar()

    Txt_4 = StringVar()

    Txt_5 = StringVar()

    Txt_7 = StringVar()

    Txt_8 = StringVar()

    Txt_9 = StringVar()

    Txt_0 = StringVar()

    txtHT = StringVar()

    popup = Toplevel()

    popup.geometry("400x450")

    popup.wm_title("Análitica de Pacientes")
    popup.configure(bg="#C0EAF8")

    Txt_0.set("Análitica De Pacientes \nPor Especialidad")

    Txt_1.set("Mayor: " + str(mayorTodos) + "  " + str(mayor()))

    Txt_2.set("Menor: " + str(menorTodos) + "  " + str(menor()))

    Txt_3.set("Media: " + str(mediaTodos))

    Txt_4.set("Std: " + str(stdTodos))

    Txt_5.set("Total: " + str(sumaTodos))

    Txt_7.set("Promedio Traumatologia: " + str(mediaTrauma))

    Txt_8.set("Promedio Neurologia: " + str(mediaNeuro))

    Txt_9.set("Promedio Cardiologia: " + str(mediaCardio))

    txtHT.set(contDiagnostico())

    mayorE = Frame(popup, width=320, height=340, bg="#00B8FF")
    mayorE.place(x=20, y=20)

    Frame(popup, width=320, height=60, bg="light grey").place(x=20, y=20)

    Label(popup, textvariable=Txt_0, bg="light grey", fg="black", font=("Cascadia Code PL SemiBold", 12)).place(x=30,
                                                                                                                y=30)

    Label(popup, textvariable=Txt_1, bg="#00B8FF", fg="black", height=1, font=("Cascadia Code PL SemiBold", 10)).place(
        x=30, y=90)
    Label(popup, textvariable=Txt_2, bg="#00B8FF", fg="black", height=1, font=("Cascadia Code PL SemiBold", 10)).place(
        x=30, y=110)
    Label(popup, textvariable=Txt_5, bg="#00B8FF", fg="black", height=1, font=("Cascadia Code PL SemiBold", 10)).place(
        x=30, y=130)
    Label(popup, textvariable=Txt_3, bg="#00B8FF", fg="black", height=1, font=("Cascadia Code PL SemiBold", 10)).place(
        x=30, y=150)
    Label(popup, textvariable=Txt_4, bg="#00B8FF", fg="black", height=1, font=("Cascadia Code PL SemiBold", 10)).place(
        x=30, y=170)
    Label(popup, textvariable=Txt_7, bg="#00B8FF", fg="black", height=1, font=("Cascadia Code PL SemiBold", 10)).place(
        x=30, y=190)
    Label(popup, textvariable=Txt_8, bg="#00B8FF", fg="black", height=1, font=("Cascadia Code PL SemiBold", 10)).place(
        x=30, y=210)
    Label(popup, textvariable=Txt_9, bg="#00B8FF", fg="black", height=1, font=("Cascadia Code PL SemiBold", 10)).place(
        x=30, y=230)
    # Label(popup, text =  "Pacientes Por Diag. Inicial",bg = "#00B8FF", fg="red",height = 1,font=("Cascadia Code PL SemiBold",11) ).place(x=30,y=180)
    # Label(popup, text = "Hemorragia Traumática: ",bg = "#00B8FF", fg="black",font=("Cascadia Code PL SemiBold",10) ).place(x=30,y=210)
    Label(popup, textvariable=txtHT, bg="#00B8FF", fg="black", font=("Cascadia Code PL SemiBold", 10)).place(x=30,
                                                                                                             y=250)


def tablaAM():
    popup = Tk()
    popup.geometry("400x400")
    popup.title("Pacientes Alta Medica")
    # =======================

    marcoTodos = LabelFrame(popup, text="Pacientes Con Alta Medica", bd=4, width=290, height=318, bg="#EDF0F2")
    marcoTodos.place(x=50, y=30)
    # estilo
    style = ttk.Style()
    style.configure('Treeview', background="#C0EAF8", foreground="black", fieldBackground="#C0EAF8")
    style.theme_use("default")
    style.map('Treeview', background=[('selected', '#DCA44C')])
    # creacion de tabla
    tablaTodos = ttk.Treeview(popup, columns=(0, 1, 2), show='headings', height=12)
    tablaTodos.place(x=70, y=55)
    tablaTodos.tag_configure('oddrow', background="#26C1F4")
    tablaTodos.tag_configure('evenrow', background="#C0EAF8")
    tablaTodos.heading(0, text="N°")
    tablaTodos.heading(1, text="Nombre")
    tablaTodos.heading(2, text="Rut")
    tablaTodos.column(0, width=10, minwidth=25)
    tablaTodos.column(1, width=120)
    tablaTodos.column(2, width=120)

    # agregando elementos
    index = 1
    for i in range(0, listaPacientesAM.contador()):

        if index % 2 == 0:
            tablaTodos.insert(parent='', index=i, iid=i,
                              values=(index, listaPacientesAM[i].getNombre(), listaPacientesAM[i].getRut()),
                              tags=('evenrow'))

        else:
            tablaTodos.insert(parent='', index=i, iid=i,
                              values=(index, listaPacientesAM[i].getNombre(), listaPacientesAM[i].getRut()),
                              tags=('oddrow'))

        index += 1
    popup.mainloop


def BuscarPaciente(rut):
    rutS = rut
    cNom = StringVar()
    cRut = StringVar()
    cEstado = StringVar()
    cDiagI = StringVar()
    cSexo = StringVar()
    cEdad = StringVar()
    cDiagnostico = StringVar()
    cTratamiento = StringVar()

    def selectPacient(rut):

        def close_window(root):
            root.destroy()

        def guardaT():

            diagnosticoAct = ""
            tratamientoAct = ""
            listaEnlazada.buscarPorIterar(rut).setDiagnostico(diagnostico.get())
            listaEnlazada.buscarPorIterar(rut).setTratamiento(tratamiento.get("1.0", "end"))

            if len(listaEnlazada.buscarPorIterar(rut).getDiagnostico()) == 0:
                diagnosticoAct = "No Disponible"
            else:
                diagnosticoAct = listaEnlazada.buscarPorIterar(rut).getDiagnostico()

            cDiagnostico.set(diagnosticoAct)

            if len(listaEnlazada.buscarPorIterar(rut).getTratamiento()) == 0:
                tratamientoAct = "No Disponible"
            else:
                tratamientoAct = listaEnlazada.buscarPorIterar(rut).getTratamiento()

            cTratamiento.set(tratamientoAct)

        top = Toplevel()
        top.geometry("350x270")
        top.title("Diagnostico")
        header = Frame(top, width=500, height=120)
        header.pack()
        body = Frame(top, width=500, height=380, bg="#00B8FF")
        body.pack()

        tk.Label(top, text="Diagnostico:").place(x=125, y=10)
        diagnostico = tk.Entry(top, width=40)
        diagnostico.place(x=50, y=30)

        tk.Label(top, text="Tratamiento:").place(x=125, y=50)
        tratamiento = tk.Text(top, height=5, width=25, padx=15, pady=15)
        tratamiento.place(x=50, y=70)

        imgAgrega = Image.open('images/solAtenAgregar.png')
        imgAgrega = ImageTk.PhotoImage(imgAgrega)
        agrega = Button(top, image=imgAgrega, borderwidth=0, bg="#00B8FF",
                        command=lambda: [guardaT(), close_window(top)])
        agrega.place(x=210, y=200)

        imgBac = Image.open('images/solAtenAtras.png')
        imgBac = ImageTk.PhotoImage(imgBac)
        bac = Button(top, image=imgBac, borderwidth=0, bg="#00B8FF", command=lambda: close_window(top))
        bac.place(x=280, y=200)

        top.mainloop()

    def altaMedica(rut):

        def showInfo():
            resp = messagebox.showinfo("Info", "Alta Medica Completa\n\n", parent=info)
            if resp == "ok":
                ActualizaTabla()

        listaPacientesAM.adicionarFinal(
            Paciente(listaEnlazada.buscarPorIterar(rut).getNombre(), listaEnlazada.buscarPorIterar(rut).getRut(),
                     listaEnlazada.buscarPorIterar(rut).getSexo(), listaEnlazada.buscarPorIterar(rut).getEdad(),
                     listaEnlazada.buscarPorIterar(rut).getDiagnosticoI(),
                     listaEnlazada.buscarPorIterar(rut).getEstado(), listaEnlazada.buscarPorIterar(rut).getDespacho(),
                     True, listaEnlazada.buscarPorIterar(rut).getNombreM(),
                     listaEnlazada.buscarPorIterar(rut).getRutM(), listaEnlazada.buscarPorIterar(rut).getDiagnostico(),
                     listaEnlazada.buscarPorIterar(rut).getTratamiento(),
                     listaEnlazada.buscarPorIterar(rut).getIdEspecialista(),
                     listaEnlazada.buscarPorIterar(rut).getNombreEspecialidad()))

        rutActual = listaEnlazada.buscarPorIterar(rut).getRut()
        listaEnlazada.borrarPorRut(rutActual)
        showInfo()

    def close_window(root):
        root.destroy()

    if listaEnlazada.buscarPorIterar(rut) == "Paciente no registrado":
        messagebox.showinfo("Info", "Paciente No Registrado\n\n")

    else:

        cNom.set(listaEnlazada.buscarPorIterar(rut).getNombre())
        cRut.set(listaEnlazada.buscarPorIterar(rut).getRut())
        cEstado.set(listaEnlazada.buscarPorIterar(rut).getEstado())
        cDiagI.set(listaEnlazada.buscarPorIterar(rut).getDiagnosticoI())
        cSexo.set(listaEnlazada.buscarPorIterar(rut).getSexo())
        cEdad.set(listaEnlazada.buscarPorIterar(rut).getEdad())

        diagnostico = ""
        if len(listaEnlazada.buscarPorIterar(rut).getDiagnostico()) == 0:
            diagnostico = "No Disponible"
        else:
            diagnostico = listaEnlazada.buscarPorIterar(rut).getDiagnostico()

        cDiagnostico.set(diagnostico)

        tratamiento = ""
        if len(listaEnlazada.buscarPorIterar(rut).getTratamiento()) == 0:
            tratamiento = "No Disponible"
        else:
            tratamiento = listaEnlazada.buscarPorIterar(rut).getTratamiento()

        cTratamiento.set(tratamiento)

        info = Toplevel()
        info.title("Paciente " + listaEnlazada.buscarPorIterar(rut).getNombre())
        info.geometry("420x360")
        header = Frame(info, width=550, height=167)
        header.pack()
        body = Frame(info, width=550, height=500, bg="#00B8FF")
        body.pack()

        Label(info, text="Nombre:").place(x=40, y=30)
        nombre = Entry(info, width=30, state="readonly", textvariable=cNom)
        nombre.focus()
        nombre.place(x=170, y=30)

        Label(info, text="Rut:").place(x=40, y=60)
        rut = Entry(info, width=30, state="readonly", textvariable=cRut)
        rut.place(x=170, y=60)

        Label(info, text="Edad:").place(x=40, y=90)
        Edad = Entry(info, width=30, state="readonly", textvariable=cEdad)
        Edad.place(x=170, y=90)

        Label(info, text="Diagnostico Inicial:").place(x=40, y=120)
        diagI = Entry(info, width=30, state="readonly", textvariable=cDiagI)
        diagI.place(x=170, y=120)

        # Label(info, text=f"Estado de {listaEnlazada.buscarPorIterar(rut).getNombre()}",bg = "#00B8FF", font=("Aharoni",10,'bold')).place(x=100,y=170)

        Label(info, text="Estado:", bg="#00B8FF").place(x=40, y=200)
        estado = Entry(info, width=30, state="readonly", textvariable=cEstado)
        estado.place(x=170, y=200)

        Label(info, text="Diaganostico:", bg="#00B8FF").place(x=40, y=230)
        estado = Entry(info, width=30, state="readonly", textvariable=cDiagnostico)
        estado.place(x=170, y=230)

        Label(info, text="Tratamiento:", bg="#00B8FF").place(x=40, y=260)
        datosBoxT = Entry(info, width=30, state="readonly", textvariable=cTratamiento)
        datosBoxT.place(x=170, y=260)

        imgamC = Image.open('images/btnAM.png')
        imgamC = ImageTk.PhotoImage(imgamC)
        btnAMC = Button(info, image=imgamC, borderwidth=0, bg="#EDF0F2",
                        command=lambda: [altaMedica(rutS), close_window(info)])
        btnAMC.place(x=260, y=300)

        imgdC = Image.open('images/btnD.png')
        imgdC = ImageTk.PhotoImage(imgdC)
        btnDC = Button(info, image=imgdC, borderwidth=0, bg="#EDF0F2", command=lambda: selectPacient(rutS))
        btnDC.place(x=310, y=300)

        info.mainloop()


def close_window(root):
    root.destroy()


def distribuirListas(nombre, rut, sexo, Edad, diagI, estado, despacho):
    if len(nombre) == 0 or len(rut) == 0 or len(Edad) == 0:
        messagebox.showerror("Error", "Todos Los Campos Son Obligatorios", parent=root)
    else:

        listaEnlazada.adicionarFinal(
            Paciente(nombre, rut, sexo, int(Edad), diagI, estado, despacho, False, medico[0], medico[1], medico[2],
                     medico[3], medico[4], medico[5]))

        #listas para ordenar por edad
        listaOrdenamiento.adicionarFinal(int(Edad))
        listaOrdenadaPorEdad.append(Paciente(nombre, rut, sexo, int(Edad), diagI, estado, despacho, False, medico[0], medico[1], medico[2],
                     medico[3], medico[4], medico[5]))

        #lista para ordenar por estado

        if str(estado) == "Reanimacion":
            listaEstado.adicionarFinal(1)
            listaOrdenadaPorEstado.append(Paciente(nombre, rut, sexo, int(Edad), diagI, estado, despacho, False, int(1), medico[1], medico[2],medico[3], medico[4], medico[5]))
        elif str(estado) == "Emergencia":
            listaEstado.adicionarFinal(2)
            listaOrdenadaPorEstado.append(Paciente(nombre, rut, sexo, int(Edad), diagI, estado, despacho, False, int(2), medico[1], medico[2],
                         medico[3], medico[4], medico[5]))
        elif str(estado) == "Urgencia":
            listaEstado.adicionarFinal(3)
            listaOrdenadaPorEstado.append(Paciente(nombre, rut, sexo, int(Edad), diagI, estado, despacho, False, int(3), medico[1], medico[2],
                         medico[3], medico[4], medico[5]))
        elif str(estado) == "Prioritario":
            listaEstado.adicionarFinal(4)
            listaOrdenadaPorEstado.append(Paciente(nombre, rut, sexo, int(Edad), diagI, estado, despacho, False, int(4), medico[1], medico[2],
                         medico[3], medico[4], medico[5]))
        elif str(estado) == "No urgencia":
            listaEstado.adicionarFinal(5)
            listaOrdenadaPorEstado.append(Paciente(nombre, rut, sexo, int(Edad), diagI, estado, despacho, False, int(5), medico[1], medico[2],
                         medico[3], medico[4], medico[5]))

        #lista para ordenar por diagnostico inicial
        if str(diagI) == "1-Hemorragia Traumatica":
            listaDiagnostico.adicionarFinal(1)
            listaOrdenadaPorDiagnostico.append(Paciente(nombre, rut, sexo, int(Edad), diagI, estado, despacho, False, int(1), int(1), medico[2],medico[3], medico[4], medico[5]))
        elif str(diagI) == "2-Impacto de Bala":
            listaEstado.adicionarFinal(2)
            listaOrdenadaPorEstado.append(Paciente(nombre, rut, sexo, int(Edad), diagI, estado, despacho, False, int(2), int(2), medico[2],medico[3], medico[4], medico[5]))
        elif str(diagI) == "3-Fractura Osea":
            listaEstado.adicionarFinal(3)
            listaOrdenadaPorEstado.append(
                Paciente(nombre, rut, sexo, int(Edad), diagI, estado, despacho, False, int(3), int(3), medico[2],medico[3], medico[4], medico[5]))
        elif str(diagI) == "4-Infeccion Bacteriana":
            listaDiagnostico.adicionarFinal(4)
            listaOrdenadaPorDiagnostico.append(
                Paciente(nombre, rut, sexo, int(Edad), diagI, estado, despacho, False, int(4), int(4), medico[2],medico[3], medico[4], medico[5]))
        elif str(diagI) == "5-Otro":
            listaDiagnostico.adicionarFinal(5)
            listaOrdenadaPorDiagnostico.append(
                Paciente(nombre, rut, sexo, int(Edad), diagI, estado, despacho, False, int(5), int(5), medico[2],medico[3], medico[4], medico[5]))



        # listaCompleta.agregar(Paciente(nombre,rut,sexo,Edad,diagI,estado,despacho,False    ,medico[0],medico[1],medico[2],medico[3],medico[4],medico[5]))

        if despacho == "traumatologia":
            listaTrauma.adicionarFinal(
                Paciente(nombre, rut, sexo, Edad, diagI, estado, despacho, False, "", "", "", "", "", ""))
        elif despacho == "neurologia":
            listaNeuro.adicionarFinal(
                Paciente(nombre, rut, sexo, Edad, diagI, estado, despacho, False, "", "", "", "", "", ""))
        elif despacho == "cardiologia":
            listaCardio.adicionarFinal(
                Paciente(nombre, rut, sexo, Edad, diagI, estado, despacho, False, "", "", "", "", "", ""))

        res = messagebox.showinfo("Info", "Paciente Registrado", parent=root)
        if res == "ok":
            borrarHistorial()


def borrarHistorial():
    nombre.delete(0, END)
    rut.delete(0, END)
    Edad.delete(0, END)


addList()
root = Tk()
root.title("Emergencias Medicas")

root.geometry("650x600")

# encabezado -> logo
header = Frame(root, width=1425, height=160, bg="white")
header.grid(columnspan=5, row=0)

# cuerpo
body = Frame(root, width=1425, height=450, bg="#0026fe")
body.grid(columnspan=5, row=1)

display_logo('./images/logoucen.png', 10, 20)

sexos = ["masculino", "femenino", "otro"]
estados = ["Reanimacion", "Emergencia", "Urgencia", "Prioritario", "No urgencia"]
dIniciales = ["1-Hemorragia Traumatica", "2-Impacto de Bala", "3-Fractura Osea", "4-Infeccion Bacteriana", "5-Otro"]

# labels

Label(root, text="Nombre:", bg="#0026fe", fg="white", font=("Aharoni", 12, 'bold')).place(x=230, y=170)
nombre = Entry(root, width=40)
nombre.focus()
nombre.place(x=360, y=170)

Label(root, text="Rut:", bg="#0026fe", fg="white", font=("Aharoni", 12, 'bold')).place(x=230, y=200)
rut = Entry(root, width=40)
rut.place(x=360, y=200)

Label(root, text="Sexo:", bg="#0026fe", fg="white", font=("Aharoni", 12, 'bold')).place(x=230, y=230)
sexo = Spinbox(root, values=sexos)
sexo.place(x=360, y=230)

Label(root, text="Edad:", bg="#0026fe", fg="white", font=("Aharoni", 12, 'bold')).place(x=230, y=260)
Edad = Entry(root, width=40)
Edad.place(x=360, y=260)

Label(root, text="Diagnostico I :", bg="#0026fe", fg="white", font=("Aharoni", 12, 'bold')).place(x=230, y=290)
diagI = Spinbox(root, values=dIniciales, width=30)
diagI.place(x=360, y=290)

Label(root, text="Estado:", bg="#0026fe", fg="white", font=("Aharoni", 12, 'bold')).place(x=230, y=320)
estado = Spinbox(root, values=estados)
estado.place(x=360, y=320)

Label(root, text="Despacho:", bg="#0026fe", fg="white", font=("Aharoni", 12, 'bold')).place(x=230, y=350)

despacho = StringVar()
trauma = Radiobutton(root, text="Traumatologia", variable=despacho, value="traumatologia", bg="#0026fe",
                     font=("Aharoni", 10, 'bold'))
trauma.place(x=360, y=350)
trauma.select()

neuro = Radiobutton(root, text="Neurologia", variable=despacho, value="neurologia", bg="#0026fe", fg="black",
                    font=("Aharoni", 10, 'bold'))
neuro.place(x=360, y=370)

cardio = Radiobutton(root, text="Cardiologia", variable=despacho, value="cardiologia", bg="#0026fe", fg="black",
                     font=("Aharoni", 10, 'bold'))
cardio.place(x=360, y=390)

imgAgregar = Image.open('images/agregarPrin.png')
imgAgregar = ImageTk.PhotoImage(imgAgregar)
agregar = Button(root, image=imgAgregar, borderwidth=0, bg="#0026fe", command=lambda: [
    distribuirListas(nombre.get(), rut.get(), sexo.get(), Edad.get(), diagI.get(), estado.get(), despacho.get()),
    ActualizaTabla()])
agregar.place(x=530, y=370)

# Buscar Paciente
marco = LabelFrame(root, text="Buscar Pacientes", bd=4, width=350, height=100, bg="light grey")
marco.place(x=230, y=460)
Label(root, text="Rut: ", fg="black", bg="light grey", height=1, font=("Aharoni", 12, 'bold')).place(x=240, y=500)
buscaPaciente = StringVar()
buscaPaciente = Entry(root, width=20)
buscaPaciente.place(x=300, y=500)

# buton buscar paciente
imgAgrega = Image.open('images/buscarPrincipal.png')
imgAgrega = ImageTk.PhotoImage(imgAgrega)
agregar = Button(root, image=imgAgrega, bg="light grey", borderwidth=0,
                 command=lambda: [BuscarPaciente(buscaPaciente.get()), buscaPaciente.delete(0, 'end')])
agregar.place(x=470, y=490)

treeInit()

root.mainloop()
