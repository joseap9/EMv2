from tkinter.constants import NO
from Medico import *
from Persona import *
from Nodo import *
import tkinter as tk



class Paciente( Persona, Medico) :

    def __init__(self,nombre,rut,sexo,edad,diagnosticoI,estado,despacho,altaMedica, nombreM,rutM,diagnostico,tratamiento,idEspecialista,nombreEspecialidad):
        Persona.__init__(self,nombre,rut,sexo,edad)
        Medico.__init__(self,nombreM,rutM,diagnostico,tratamiento,idEspecialista,nombreEspecialidad)
        self.estado = estado
        self.altaMedica = altaMedica
        self.diagnosticoI=diagnosticoI
        self.despacho = despacho
        

    def getEstado(self):
        return self.estado

    def getaltaMedica(self):
        return self.altaMedica
    
    def getDespacho(self):
        return self.despacho

    def getDiagnosticoI(self):
        return self.diagnosticoI
    

    def setEstado(self, estado):
        self.estado = estado

    def setaltaMedica(self):
        self.altaMedica = True


    def setDiagnosticoI(self,d):
        self.diagnosticoI = d
    
    def setDespacho(self, des):
        self.despacho = des

    
    def solicitarAtencion(self,nombre,rut,sexo,direccion,diagnosticoI, estado, despacho, camaAsig, numAtencion):
        nuevoPaciente = Paciente(nombre,rut,sexo,direccion,diagnosticoI,estado,despacho,camaAsig,numAtencion)
        self.listaPacientes.append(nuevoPaciente)

        n = 1
        for x in range(len(self.listaPacientes)):
            if len(self.listaPacientes) == n:
                print("agregado")
                print("hay ", n, "pacientes agregados")
            n = n + 1

    def muestraTree(self):
        diag = ""
        tra = ""
        am = ""
        if len(self.diagnostico) != 0:
            diag = self.diagnostico
        else:
            diag = "No Disponible"
        
        if len(self.tratamiento) != 0:
            tra = self.tratamiento
        else:
            tra = "No Disponible"

        if self.altaMedica == False:
            am = "No"
        else:
            am = "Si"

        return "        Datos del Paciente"+"\n\nNombre: "+self.nombre+ "\nRut: " + self.rut +"\nDireccion: "+self.direccion +"\n\n         Estado Del Paciente\n\nEstado: " + self.estado + "\nAlta medica: "+am+"\nDiagnostico: "+diag+"\nTratamiento: "+tra 

    
    def __str__(self):
        return Persona.__str__(self) + "\n" + self.diagnosticoI + "\n" + self.estado + "\n" + self.despacho
    








class ListaCompleta():

    listaPacientes = []  # Esta lista contendrá objetos de la clase Paciente

    def __init__(self, listaPacientes=[]):
        self.paciente = listaPacientes 

    def getPos(self, pos):
        for x in len(0 , self.listaPacientes):
            if x == pos:
                return self.listaPacientes[x]
        return False

    def getNombre(self):
        for paciente in self.listaPacientes:
            return paciente.getNombre()

    def getRut(self):
        for paciente in self.listaPacientes:
            return paciente.getRut()
    
    def getEstado(self):
        for paciente in self.listaPacientes:
            return paciente.getEstado()

    def getDiagnosticoI(self):
        for paciente in self.listaPacientes:
            return paciente.getDiagnosticoI() 

    def getTratamiento(self):
        for paciente in self.listaPacientes:
            return paciente.getTratamiento() 

    def setTratamiento(self,t):
        for paciente in self.listaPacientes:
            paciente.setTratamiento(t)


    def agregar(self, paciente):  
        self.listaPacientes.append(paciente)

    def mostrar(self):
        
        for paciente in self.listaPacientes:
            print(paciente)


    def buscar(self, rut):
        for paciente in self.listaPacientes:
            if paciente.getRut() == rut:
                return paciente
        return "Paciente no registrado"

    def buscarMedico(self, rut):

        for paciente in self.listaPacientes:
            if paciente.getRut() == rut:
                return paciente.muestraMedicoE()
               
        return "Paciente no registrado"

        
        
                

    def mostrarT(self, rut):
        
        for paciente in self.listaPacientes:
            if rut == paciente.getRut():
                return paciente.getTratamiento()
            
            
            
    def actualizaT(self, rut, tratamiento):

        for paciente in self.listaPacientes:
            if rut == paciente.getRut():
                paciente.setTratamiento(tratamiento)
            paciente.setRut(rut) 

    def mostrarD(self, rut):
        
        for paciente in self.listaPacientes:
            if rut == paciente.getRut():
                return paciente.getDiagnostico()
            
            
            
    def actualizaD(self, rut, diagnostico):

        for paciente in self.listaPacientes:
            if rut == paciente.getRut():
                paciente.setDiagnostico(diagnostico)
            paciente.setRut(rut) 

        



class ListaEnlazada: 
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.size = 0
    #________________________________________________
    def ordenamientoSeleccion(self):

        temp = self.cabeza

        # Traverse the List
        while (temp):

            minn = temp
            r = temp.proximo

            # Traverse the unsorted sublist
            while (r):
                if (minn.data > r.data):
                    minn = r

                r = r.proximo

            # Swap Data
            x = temp.data
            temp.data = minn.data
            minn.data = x
            temp = temp.proximo

    # funcion para ordenar por burbuja
    def ordenamientoBurbuja(self):
        for i in range(self.size - 1):  # for controlling passes of Bubble Sort
            curr = self.cabeza
            nxt = curr.proximo
            prev = None
            while nxt:  # Comparisons in passes
                if curr.data > nxt.data:
                    if prev == None:
                        prev = curr.proximo
                        nxt = nxt.proximo
                        prev.proximo = curr
                        curr.proximo = nxt
                        self.cabeza = prev
                    else:
                        temp = nxt
                        nxt = nxt.proximo
                        prev.proximo = curr.proximo
                        prev = temp
                        temp.proximo = curr
                        curr.proximo = nxt
                else:
                    prev = curr
                    curr = nxt
                    nxt = nxt.proximo
            i = i + 1




    # Método para agregar elementos en el frente de la lsta encadena
    def adicionarFrente(self, data):
        self.cabeza = Nodo(data=data, proximo=self.cabeza)  
    #________________________________________________
    # Método para verificar si la estructura de datos esta vacia
    def esVacio(self):
        return self.cabeza == None
    #_________________________________________________
    # Método para agregar elementos al final de la lista encadenada 
    def adicionarFinal(self, data):
        self.size += 1
        if not self.cabeza:
            self.cabeza = Nodo(data=data)
            return
        curr = self.cabeza
        while curr.proximo:
            curr = curr.proximo
        curr.proximo = Nodo(data=data)
    
    # Método para eliminar Nodos
    #__________________________________________________
    def eliminarNodo(self, key):
        curr = self.cabeza
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.proximo
        if prev is None:
            self.cabeza = curr.proximo
        elif curr:
            prev.proximo = curr.proximo
            curr.proximo = None
    # __________________________________________
    def estaEnLista(self,keyBuscar):
          esta = False
          curr=self.cabeza
          while curr and not esta :
              if curr.clave==keyBuscar :
                      esta=True
                      break
              curr = curr.proximo
          return esta
    #___________________________________________________
    # Método para obtener el ultimo Nodo
    def ultimoNodo(self):
        temp = self.cabeza
        while(temp.proximo is not None):
            temp = temp.proximo
        print (temp.data)

    def PrimerNodo(self):
        temp = self.cabeza
        while(temp.proximo is not None):
            temp = temp.proximo
        print (temp.data)
    #___________________________________________________
    # Método para imprimir la lista de Nodos
    def imprimirLista( self ):
        Nodo = self.cabeza
        while Nodo != None:
            print(Nodo.data, end ="\n ")
            Nodo = Nodo.proximo

    def contador(self):
        Nodo =  self.cabeza
        len = 0
        while Nodo != None:
            len = len + 1
            Nodo = Nodo.proximo

        return len
        

    def borrarPrimero(self):
        Nodo = self.cabeza
        if self.esVacio() == False:
            Nodo = Nodo.proximo

    def iterar(self):
        Nodo = self.cabeza
        while Nodo:
            dato = Nodo.data
            Nodo = Nodo.proximo
            yield dato

    def buscarPorIterar(self , rut):
        
        for n in self.iterar():
            if  rut == n.getRut():
                return n
        return "Paciente no registrado"


    def buscarRut(self, rut):
        Nodo = self.cabeza
        while Nodo != None:
            if Nodo.data.getRut() == rut:
                return Nodo.data
            Nodo = Nodo.proximo
        return "Paciente no registrado"



    def buscarMedicoPorRut(self , rut):
        
        for n in self.iterar():
            if  rut == n.getRut():
                return n.muestraMedicoE()
        return "Paciente no registrado"

    def buscarTratamientoPorRut(self , rut):
        
        for n in self.iterar():
            if  rut == n.getRut():
                return n.getTratamiento()
        return "---"

    def buscarInfoPaciente(self,rut):
        for n in self.iterar():
            if  rut == n.getRut():
                return n.getInfoBreve()
        return "---"


    def buscarDiagnosticoPorRut(self , rut):
        
        for n in self.iterar():
            if  rut == n.getRut():
                return n.getDiagnostico()
        return "---"

    def borrarPorRut(self , rut):
        anterior = self.cabeza
        actual =  self.cabeza
       
        while actual:
            if actual.data.getRut() == rut:
                if actual == self.cabeza:
                    self.cabeza = actual.proximo
                else:
                    anterior.proximo = actual.proximo
                self.size -= 1
                return
            anterior = actual
            actual = actual.proximo
            

    def __getitem__(self, index):
        
        Nodo = self.cabeza

        for i in range(index):
            Nodo = Nodo.proximo
        return Nodo.data
       


class ListaTrauma: 
    def __init__(self):
        self.cabeza = None
    #________________________________________________    
    # Método para agregar elementos en el frente de la lsta encadena
    def adicionarFrente(self, data):
        self.cabeza = Nodo(data=data, proximo=self.cabeza)  
    #________________________________________________
    # Método para verificar si la estructura de datos esta vacia
    def esVacio(self):
        return self.cabeza == None
    #_________________________________________________
    # Método para agregar elementos al final de la lista encadenada 
    def adicionarFinal(self, data):
        if not self.cabeza:
            self.cabeza = Nodo(data=data)
            return
        curr = self.cabeza
        while curr.proximo:
            curr = curr.proximo
        curr.proximo = Nodo(data=data)
    
    # Método para eliminar Nodos
    #__________________________________________________
    def eliminarNodo(self, key):
        curr = self.cabeza
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.proximo
        if prev is None:
            self.cabeza = curr.proximo
        elif curr:
            prev.proximo = curr.proximo
            curr.proximo = None
    # __________________________________________
    def estaEnLista(self,keyBuscar):
          esta = False
          curr=self.cabeza
          while curr and not esta :
              if curr.clave==keyBuscar :
                      esta=True
                      break
              curr = curr.proximo
          return esta
    #___________________________________________________
    # Método para obtener el ultimo Nodo
    def ultimoNodo(self):
        temp = self.cabeza
        while(temp.proximo is not None):
            temp = temp.proximo
        print (temp.data)

    def PrimerNodo(self):
        temp = self.cabeza
        while(temp.proximo is not None):
            temp = temp.proximo
        print (temp.data)
    #___________________________________________________
    # Método para imprimir la lista de Nodos
    def imprimirLista( self ):
        Nodo = self.cabeza
        while Nodo != None:
            print(Nodo.data, end ="\n ")
            Nodo = Nodo.proximo

    def contador(self):
        Nodo =  self.cabeza
        len = 0
        while Nodo != None:
            len = len + 1
            Nodo = Nodo.proximo
        print(len)
        return len

    def borrarPrimero(self):
        Nodo = self.cabeza
        if self.esVacio() == False:
            Nodo = Nodo.proximo

    def iterar(self):
        Nodo = self.cabeza
        while Nodo:
            dato = Nodo.data
            Nodo = Nodo.proximo
            yield dato

    def buscarPorIterar(self , rut):
        
        for n in self.iterar():
            if  rut == n.getRut():
                return n
        return "Paciente no registrado"


    def buscarRut(self, rut):
        Nodo = self.cabeza
        while Nodo != None:
            if Nodo.data.getRut() == rut:
                return Nodo.data
            Nodo = Nodo.proximo
        return "Paciente no registrado"

    def __getitem__(self, index):
        Nodo = self.cabeza
        for i in range(index):
            Nodo = Nodo.proximo
        return Nodo.data


class ListaNeuro: 
    def __init__(self):
        self.cabeza = None
    #________________________________________________    
    # Método para agregar elementos en el frente de la lsta encadena
    def adicionarFrente(self, data):
        self.cabeza = Nodo(data=data, proximo=self.cabeza)  
    #________________________________________________
    # Método para verificar si la estructura de datos esta vacia
    def esVacio(self):
        return self.cabeza == None
    #_________________________________________________
    # Método para agregar elementos al final de la lista encadenada 
    def adicionarFinal(self, data):
        if not self.cabeza:
            self.cabeza = Nodo(data=data)
            return
        curr = self.cabeza
        while curr.proximo:
            curr = curr.proximo
        curr.proximo = Nodo(data=data)
    
    # Método para eliminar Nodos
    #__________________________________________________
    def eliminarNodo(self, key):
        curr = self.cabeza
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.proximo
        if prev is None:
            self.cabeza = curr.proximo
        elif curr:
            prev.proximo = curr.proximo
            curr.proximo = None
    # __________________________________________
    def estaEnLista(self,keyBuscar):
          esta = False
          curr=self.cabeza
          while curr and not esta :
              if curr.clave==keyBuscar :
                      esta=True
                      break
              curr = curr.proximo
          return esta
    #___________________________________________________
    # Método para obtener el ultimo Nodo
    def ultimoNodo(self):
        temp = self.cabeza
        while(temp.proximo is not None):
            temp = temp.proximo
        print (temp.data)

    def PrimerNodo(self):
        temp = self.cabeza
        while(temp.proximo is not None):
            temp = temp.proximo
        print (temp.data)
    #___________________________________________________
    # Método para imprimir la lista de Nodos
    def imprimirLista( self ):
        Nodo = self.cabeza
        while Nodo != None:
            print(Nodo.data, end ="\n ")
            Nodo = Nodo.proximo

    def contador(self):
        Nodo =  self.cabeza
        len = 0
        while Nodo != None:
            len = len + 1
            Nodo = Nodo.proximo
        return len

    def borrarPrimero(self):
        Nodo = self.cabeza
        if self.esVacio() == False:
            Nodo = Nodo.proximo

    def iterar(self):
        Nodo = self.cabeza
        while Nodo:
            dato = Nodo.data
            Nodo = Nodo.proximo
            yield dato

    def buscarPorIterar(self , rut):
        
        for n in self.iterar():
            if  rut == n.getRut():
                return n
        return "Paciente no registrado"


    def buscarRut(self, rut):
        Nodo = self.cabeza
        while Nodo != None:
            if Nodo.data.getRut() == rut:
                return Nodo.data
            Nodo = Nodo.proximo
        return "Paciente no registrado"

    def __getitem__(self, index):
        Nodo = self.cabeza
        for i in range(index):
            Nodo = Nodo.proximo
        return Nodo.data

class ListaCardio: 
    def __init__(self):
        self.cabeza = None
    #________________________________________________    
    # Método para agregar elementos en el frente de la lsta encadena
    def adicionarFrente(self, data):
        self.cabeza = Nodo(data=data, proximo=self.cabeza)  
    #________________________________________________
    # Método para verificar si la estructura de datos esta vacia
    def esVacio(self):
        return self.cabeza == None
    #_________________________________________________
    # Método para agregar elementos al final de la lista encadenada 
    def adicionarFinal(self, data):
        if not self.cabeza:
            self.cabeza = Nodo(data=data)
            return
        curr = self.cabeza
        while curr.proximo:
            curr = curr.proximo
        curr.proximo = Nodo(data=data)
    
    # Método para eliminar Nodos
    #__________________________________________________
    def eliminarNodo(self, key):
        curr = self.cabeza
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.proximo
        if prev is None:
            self.cabeza = curr.proximo
        elif curr:
            prev.proximo = curr.proximo
            curr.proximo = None
    # __________________________________________
    def estaEnLista(self,keyBuscar):
          esta = False
          curr=self.cabeza
          while curr and not esta :
              if curr.clave==keyBuscar :
                      esta=True
                      break
              curr = curr.proximo
          return esta
    #___________________________________________________
    # Método para obtener el ultimo Nodo
    def ultimoNodo(self):
        temp = self.cabeza
        while(temp.proximo is not None):
            temp = temp.proximo
        print (temp.data)

    def PrimerNodo(self):
        temp = self.cabeza
        while(temp.proximo is not None):
            temp = temp.proximo
        print (temp.data)
    #___________________________________________________
    # Método para imprimir la lista de Nodos
    def imprimirLista( self ):
        Nodo = self.cabeza
        while Nodo != None:
            print(Nodo.data, end ="\n ")
            Nodo = Nodo.proximo

    def contador(self):
        Nodo =  self.cabeza
        len = 0
        while Nodo != None:
            len = len + 1
            Nodo = Nodo.proximo
        return len

    def borrarPrimero(self):
        Nodo = self.cabeza
        if self.esVacio() == False:
            Nodo = Nodo.proximo

    def iterar(self):
        Nodo = self.cabeza
        while Nodo:
            dato = Nodo.data
            Nodo = Nodo.proximo
            yield dato

    def buscarPorIterar(self , rut):
        
        for n in self.iterar():
            if  rut == n.getRut():
                return n
        return "Paciente no registrado"


    def buscarRut(self, rut):
        Nodo = self.cabeza
        while Nodo != None:
            if Nodo.data.getRut() == rut:
                return Nodo.data
            Nodo = Nodo.proximo
        return "Paciente no registrado"

    def __getitem__(self, index):
        Nodo = self.cabeza
        for i in range(index):
            Nodo = Nodo.proximo
        return Nodo.data


        


    


    






def ventanaAtencion(self):

        def close_window(root):
            root.destroy()

        sexos= ["masculino","femenino","otro"]
        estados=["reanimacion","emergencia","urgencia","prioritario","no urgencia"]
        #despachos=["traumatologia","neurologia","cardiologia"]
        root = tk.Tk()
        root.title("Solicitar Atencion")
        root.geometry("450x350")

        #labels

        tk.Label(root, text="Nombre:").place(x=40, y=30)
        nombre = tk.Entry(root, width=40)
        nombre.focus()
        nombre.place(x=170,y=30)
        


        tk.Label(root, text="rut:").place(x=40,y=60)
        rut = tk.Entry(root, width=40)
        rut.place(x=170,y=60)

        tk.Label(root, text="sexo:").place(x=40,y=90)
        sexo= tk.Spinbox(root, values=sexos)
        sexo.place(x=170,y=90)


        tk.Label(root, text="direccion:").place(x=40,y=120)
        direccion = tk.Entry(root, width=40)
        direccion.place(x=170,y=120)

        #tk.Label(root, text="cama Asignada:").grid(pady=5, row=4, column=0)
        #camaAsig = tk.Entry(root, width=40)
        #camaAsig.grid(padx=5, row=4, column=1)

        tk.Label(root, text="Diagnostico Inicial:").place(x=40,y=150)
        diagI = tk.Entry(root, width=40)
        diagI.place(x=170,y=150)

        tk.Label(root, text="estado:").place(x=40,y=180)
        estado = tk.Spinbox(root, values=estados)
        estado.place(x=170,y=180)

        tk.Label(root, text="despacho:").place(x=40,y=210)
        despacho= tk.StringVar()
        tk.Radiobutton(root, variable=despacho, text="Traumatologia",value="Traumatologia").place(x=170,y=210)
        tk.Radiobutton(root, variable=despacho, text="neurologia",value="neurologia").place(x=170,y=230)
        tk.Radiobutton(root, variable=despacho, text="cardiologia", value="cardiologia").place(x=170,y=250)
        

        #tk.Label(root, text="numero de atencion:").grid(pady=5, row=6, column=0)
        #numAtencion = tk.Entry(root, width=40)
        #numAtencion.grid(padx=5, row=6, column=1)

        agregar = tk.Button(root, text="Agregar", width=50, command=lambda: [self.solicitarAtencion(nombre.get(),rut.get(),sexo.get(),direccion.get(),diagI.get(),estado.get(),despacho.get(),"",""), self.muestra(),close_window(root)])
        agregar.place(x=50,y=300)

        #mostrar = tk.Button(root, text="Listado de Pacientes", width=50, command=lambda: btnMostrar())
        #mostrar.grid(padx=10, pady=10, row=7, column=0, columnspan=2)

        root.mainloop()





    











    
