
from Especialidad import *
import tkinter as tk


class Medico( Especialidad ):

    def __init__(self,nombreM,rutM,diagnostico,tratamiento,idEspecialista,nombreEspecialidad):
        super().__init__(idEspecialista,nombreEspecialidad)
        self.nombreM = nombreM
        self.rutM = rutM
        self.diagnostico = diagnostico
        self.tratamiento=tratamiento




    def getNombreM(self):
        return self.nombreM

    def getRutM(self):
        return self.rutM

    def setIdMedico(self,idMedico):
        self.idMedico=idMedico

    def setDiagnostico(self,d):
        self.diagnostico = d

    def setTratamiento(self,t):
        self.tratamiento = t
    

    def muestraMedicoE(self):
        return self.nombreM+" - "+self.rutM+" - "+self.nombreEspecialidad

    def getDiagnostico(self):
        return self.diagnostico

    def getTratamiento(self):
        return self.tratamiento


    #def altamedica(self,listaPacienteConCama,paciente):
        #devera eliminar de una lista de pacientes al paciente ingresado

    def indicarTratamiento(self,tratamiento):
        return tratamiento

    #def diasnoticar(self,listaPacienteConCama):
        #metodo de selecion de area para un paciente

    #esta funcion deveria ser ejecutada fuera de la clase medico ya que estariamos adcediendo a un valor que se
    #creara un aves creado los medicos
    #def morbilidad(self):
        #self.morbilidad = persona.getarea()

    def activarAutoridades(self,respuesta):
        if respuesta=="si":
            return "llamando al 133"

    #deveria ser una funcion y no un contenido de la clase
    #def mostrarMedico(self,listadoDeMedicos):
        #buscar medico por el rut del medico

class ListaMedicosTrauma:

    listaMedicos = []  # Esta lista contendrá objetos de la clase Medico


    def __init__(self, listaMedicos=[]):
        self.medico = listaMedicos 

    def getNombre(self):
        for medico in self.listaMedicos:
            return medico.getNombre()

    def getRut(self):
        for medico in self.listaMedicos:
            return medico.getRut()

    def getEsp(self):
        for medico in self.listaMedicos:
            return medico.getNombreEspecialidad()
    
    def getId(self):
        for medico in self.listaMedicos:
            return medico.getIdMedico()


    def agregar(self, medico):  
        self.listaMedicos.append(medico)

    def mostrar(self):
        
        for medico in self.listaMedicos:
            return medico


    def buscar(self, rut):
        for medico in self.listaMedicos:
            if medico.getRut() == rut:
                return medico
        return "Medico no encontrado"


def ventanaMedicoEsp():

        def close_window(root):
            root.destroy()

        def med(val):
            print(val.get())

        
        root = tk.Toplevel()
        root.title("Medico Especialista")
        root.geometry("550x500")

        #labels

        tk.Label(root, text="filtrar ", font=("Aharoni",10,'bold')).place(x=40,y=30)
        buscaP= tk.StringVar()

        trauma = tk.Radiobutton(root, value='Traumatologia', variable=buscaP, text='Traumatologia')
        trauma.place(x=100,y=30)
        trauma.select()

        neuro = tk.Radiobutton(root, value='neurologia', variable=buscaP, text='neurologia')
        neuro.place(x=220,y=30)

        cardio = tk.Radiobutton(root, value='cardiologia', variable=buscaP, text='cardiologia')
        cardio.place(x=320,y=30)

        tk.Button(root, text="ok", width=5).place(x=450,y=30)

        tk.Label(root, text="Nombre:").place(x=40, y=100)
        nombre = tk.Entry(root, width=40,state="readonly")
        nombre.focus()
        nombre.place(x=170,y=100)
        


        tk.Label(root, text="Rut:").place(x=40,y=130)
        rut = tk.Entry(root, width=40,state="readonly")
        rut.place(x=170,y=130)



        tk.Label(root, text="Diagnostico Inicial:").place(x=40,y=160)
        diagI = tk.Entry(root, width=40,state="readonly")
        diagI.place(x=170,y=160)

        tk.Label(root, text="Estado:").place(x=40,y=190)
        estado = tk.Entry(root, width=40,state="readonly")
        estado.place(x=170,y=190)

        tk.Label(root, text="Diagnostico:").place(x=40,y=250)
        diagnostico = tk.Entry(root, width=40)
        diagnostico.place(x=170,y=250)

        tk.Label(root, text="Tratamiento:").place(x=40,y=280)
        tratamiento =  tk.Text(root, height = 5, width= 25, padx=15,pady=15)
        tratamiento.place(x=170,y=280)

        tk.Button(root, text = "llamar autoridades",width = 15).place(x=77, y=425)

        tk.Button(root, text = "alta medica",width = 10, command = lambda: [close_window(root) , med(buscaP)] ).place(x=250, y=425)

        tk.Button(root, text = "siguiente",width = 10).place(x=400, y=425)

        
        
        


        

        root.mainloop()