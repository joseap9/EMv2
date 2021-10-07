from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import numpy as np
from numpy.lib.twodim_base import diag
import pylab as pl
import pandas as pd
from PIL import Image,ImageTk
from Medico import *
from Paciente import *
from Persona import *
from Especialidad import *
from functions import display_logo
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter.messagebox import showinfo




medico = Medico("","","","","","")
paciente = Paciente("","-","-","","","","",False  ,"","","","","","")


# lista completa de pacientes
listaEnlazada = ListaEnlazada()
#lista de pacientes de alta Medica
listaPacientesAM = ListaEnlazada()
#lista de pacientes por es
listaTrauma = ListaTrauma()
listaNeuro = ListaNeuro()
listaCardio =  ListaCardio()

listaEnlazada.adicionarFinal(Paciente("Silvia Gonzalez","27039327-6","M","portugal 272","1-Hemorragia Traumática","normal","traumatologia",False  ,"jose Perdomo","","","","",""))
listaEnlazada.adicionarFinal(Paciente("Ana Navarro","27039327-5","M","portugal 272","2-Impacto de bala","normal","neurologia",False  ,"","","","","",""))
listaEnlazada.adicionarFinal(Paciente("Jose Lopez","27039327-4","M","portugal 272","---","normal","cardiologia",False  ,"","","","","",""))
listaEnlazada.adicionarFinal(Paciente("Gabriel Pose","27039327-2","M","portugal 272","1-Hemorragia Traumática","normal","traumatologia",False  ,"","","","","",""))
listaEnlazada.adicionarFinal(Paciente("Maria Ahumada","27039327-1","M","portugal 272","2-Impacto de bala","normal","neurologia",False  ,"","","","","",""))
listaEnlazada.adicionarFinal(Paciente("Jaime Navarro","27039327-0","M","portugal 272","---","","cardiologia",False  ,"","","","","",""))
listaEnlazada.adicionarFinal(Paciente("Jessica Lopez","26039327-6","M","portugal 272","1-Hemorragia Traumática","normal","traumatologia",False  ,"","","","","",""))
listaEnlazada.adicionarFinal(Paciente("Mauro Sanchez","27039317-6","M","portugal 272","2-Impacto de bala","normal","neurologia",False  ,"","","","","",""))
listaEnlazada.adicionarFinal(Paciente("Gimena Lazaro","27034327-6","M","portugal 272","---","normal","cardiologia",False  ,"","","","","",""))
listaEnlazada.adicionarFinal(Paciente("Gabriel Pose","27019327-2","M","portugal 272","1-Hemorragia Traumática","normal","traumatologia",False  ,"","","","","",""))
listaEnlazada.adicionarFinal(Paciente("Maria Ahumada","27032327-1","M","portugal 272","2-Impacto de bala","normal","neurologia",False  ,"","","","","",""))
listaEnlazada.adicionarFinal(Paciente("Jaime Navarro","25039327-0","M","portugal 272","---","normal","cardiologia",False  ,"","","","","",""))
listaEnlazada.adicionarFinal(Paciente("Jessica Lopez","23039327-6","M","portugal 272","1-Hemorragia Traumática","normal","traumatologia",False  ,"","","","","",""))
listaEnlazada.adicionarFinal(Paciente("Mauro Sanchez","20039317-6","M","portugal 272","2-Impacto de bala","normal","neurologia",False  ,"","","","","",""))
listaEnlazada.adicionarFinal(Paciente("Gimena Lazaro","19034327-6","M","portugal 272","---","normal","cardiologia",False  ,"","","","","",""))
listaEnlazada.adicionarFinal(Paciente("Silvia Gonzalez","27039327-6","M","portugal 272","1-Hemorragia Traumática","normal","traumatologia",False  ,"jose Perdomo","","","","",""))
listaEnlazada.adicionarFinal(Paciente("Silvia Gonzalez","27039327-6","M","portugal 272","1-Hemorragia Traumática","normal","traumatologia",False  ,"jose Perdomo","","","","",""))
listaEnlazada.adicionarFinal(Paciente("Silvia Gonzalez","27039327-6","M","portugal 272","1-Hemorragia Traumática","normal","neurologia",False  ,"jose Perdomo","","","","",""))

listaTrauma.adicionarFinal(Paciente("Silvia Gonzalez","27039327-6","M","portugal 272","1-Hemorragia Traumática","normal","traumatologia",False  ,"jose Perdomo","","","","",""))
listaTrauma.adicionarFinal(Paciente("Silvia Gonzalez","27039327-6","M","portugal 272","1-Hemorragia Traumática","normal","traumatologia",False  ,"jose Perdomo","","","","",""))
listaTrauma.adicionarFinal(Paciente("Silvia Gonzalez","27039327-6","M","portugal 272","1-Hemorragia Traumática","normal","traumatologia",False  ,"jose Perdomo","","","","",""))
listaTrauma.adicionarFinal(Paciente("Silvia Gonzalez","27039327-6","M","portugal 272","1-Hemorragia Traumática","normal","traumatologia",False  ,"jose Perdomo","","","","",""))
listaTrauma.adicionarFinal(Paciente("Silvia Gonzalez","27039327-6","M","portugal 272","1-Hemorragia Traumática","normal","traumatologia",False  ,"jose Perdomo","","","","",""))
listaTrauma.adicionarFinal(Paciente("Silvia Gonzalez","27039327-6","M","portugal 272","1-Hemorragia Traumática","normal","traumatologia",False  ,"jose Perdomo","","","","",""))
listaTrauma.adicionarFinal(Paciente("Silvia Gonzalez","27039327-6","M","portugal 272","1-Hemorragia Traumática","normal","traumatologia",False  ,"jose Perdomo","","","","",""))

listaNeuro.adicionarFinal(Paciente("Silvia Gonzalez","27039327-6","M","portugal 272","---","normal","traumatologia",False  ,"jose Perdomo","","","","",""))
listaNeuro.adicionarFinal(Paciente("Silvia Gonzalez","27039327-6","M","portugal 272","---","normal","traumatologia",False  ,"jose Perdomo","","","","",""))
listaNeuro.adicionarFinal(Paciente("Silvia Gonzalez","27039327-6","M","portugal 272","---","normal","traumatologia",False  ,"jose Perdomo","","","","",""))
listaNeuro.adicionarFinal(Paciente("Silvia Gonzalez","27039327-6","M","portugal 272","---","normal","traumatologia",False  ,"jose Perdomo","","","","",""))
listaNeuro.adicionarFinal(Paciente("Silvia Gonzalez","27039327-6","M","portugal 272","---","normal","traumatologia",False  ,"jose Perdomo","","","","",""))
listaNeuro.adicionarFinal(Paciente("Silvia Gonzalez","27039327-6","M","portugal 272","1-Hemorragia Traumática","normal","neurologia",False  ,"jose Perdomo","","","","",""))

listaCardio.adicionarFinal(Paciente("Silvia Gonzalez","27039327-6","M","portugal 272","---","normal","traumatologia",False  ,"jose Perdomo","","","","",""))
listaCardio.adicionarFinal(Paciente("Silvia Gonzalez","27039327-6","M","portugal 272","---","normal","traumatologia",False  ,"jose Perdomo","","","","",""))
listaCardio.adicionarFinal(Paciente("Silvia Gonzalez","27039327-6","M","portugal 272","---","normal","traumatologia",False  ,"jose Perdomo","","","","",""))
listaCardio.adicionarFinal(Paciente("Silvia Gonzalez","27039327-6","M","portugal 272","---","normal","traumatologia",False  ,"jose Perdomo","","","","",""))
listaCardio.adicionarFinal(Paciente("Silvia Gonzalez","27039327-6","M","portugal 272","---","normal","traumatologia",False  ,"jose Perdomo","","","","",""))


#Lista de medicos
medico = ["Dr. Alberto Rojas","26970671-6","No disponible","No Disponible","543","Traumatologia"]


#=========================================================================
#TREE VIEW
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
                listaEnlazada[index].setTratamiento(tratamiento.get("1.0","end"))
                
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
            header = Frame(top, width = 500, height = 120)
            header.pack()
            body = Frame(top, width = 500, height = 380, bg = "#00B8FF")
            body.pack()
            
            selected = tree.selection()
            values = tree.item(selected, 'values')
            text = tree.item(selected, 'text')
            index = int(values[0])
            
            
            

            tk.Label(top, text="Diagnostico:").place(x=125 , y = 10)
            diagnostico = tk.Entry(top, width=40)
            diagnostico.place(x = 50, y = 30)

            tk.Label(top, text="Tratamiento:").place(x = 125, y = 50)
            tratamiento =  tk.Text(top, height = 5, width= 25, padx=15,pady=15)
            tratamiento.place(x= 50, y = 70)

        
            
                    
            imgAgrega = Image.open('images/solAtenAgregar.png')
            imgAgrega= ImageTk.PhotoImage(imgAgrega)
            agrega = Button(top, image=imgAgrega, borderwidth=0, bg = "#00B8FF",command=lambda:[guardaT(), close_window(top)]   )
            agrega.place(x=210 ,  y = 200)

            imgBac = Image.open('images/solAtenAtras.png')
            imgBac= ImageTk.PhotoImage(imgBac)
            bac = Button(top, image=imgBac, borderwidth=0, bg = "#00B8FF",command=lambda:close_window(top))
            bac.place(x= 280,  y = 200)
            #guardaB = Button(top, text="Diagnosticar", width=50, bg = "#00B8FF", command=lambda: [print(index), guardaT(), close_window(top)])
            #guardaB.pack(pady = 5)

            top.mainloop()


        def altaMedica():

            def showInfo():
                resp = messagebox.showinfo("Info","Alta Medica Completa\n\n", parent = info)
                if resp == "ok":
                    ActualizaTabla()
            
            
        
            selected = tree.focus()
            values = tree.item(selected, 'values')
            index = int(values[0])
            listaEnlazada[index].setaltaMedica()

            listaPacientesAM.adicionarFinal(Paciente(listaEnlazada[index].getNombre(),listaEnlazada[index].getRut(),listaEnlazada[index].getSexo(),listaEnlazada[index].getDireccion(),listaEnlazada[index].getDiagnosticoI(),listaEnlazada[index].getEstado(),listaEnlazada[index].getDespacho(),True ,listaEnlazada[index].getNombreM(),listaEnlazada[index].getRutM(),listaEnlazada[index].getDiagnostico(),listaEnlazada[index].getTratamiento(),listaEnlazada[index].getIdEspecialista(),listaEnlazada[index].getNombreEspecialidad()))
            
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
        cDireccion = StringVar()
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
        cDireccion.set(listaEnlazada[index].getDireccion())

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
        info.title("Paciente "+listaEnlazada[index].getNombre())
        info.geometry("420x360")
        header = Frame(info, width = 550, height = 167)
        header.pack()
        body = Frame(info, width = 550, height = 500, bg = "#00B8FF")
        body.pack()


        Label(info, text="Nombre:").place(x=40, y=30)
        nombre = Entry(info, width=30,state="readonly",textvariable = cNom)
        nombre.focus()
        nombre.place(x=170,y=30)
        


        Label(info, text="Rut:").place(x=40,y=60)
        rut = Entry(info, width=30,state="readonly",textvariable = cRut)
        rut.place(x=170,y=60)


        Label(info, text="Direccion:" ).place(x=40,y=90)
        direccion = Entry(info, width=30,state="readonly",textvariable = cDireccion)
        direccion.place(x=170,y=90)


        Label(info, text="Diagnostico Inicial:").place(x=40,y=120)
        diagI= Entry(info, width=30,state="readonly",textvariable = cDiagI)
        diagI.place(x=170,y=120)

        Label(info, text=f"Estado de {listaEnlazada[index].getNombre()}",bg = "#00B8FF", font=("Aharoni",10,'bold')).place(x=100,y=170)
        

        Label(info, text="Estado:",bg = "#00B8FF").place(x=40,y=200)
        estado = Entry(info, width=30,state="readonly",textvariable = cEstado)
        estado.place(x=170,y=200)

        Label(info, text="Diaganostico:",bg = "#00B8FF").place(x=40,y=230)
        estado = Entry(info, width=30,state="readonly",textvariable = cDiagnostico)
        estado.place(x=170,y=230)

        Label(info, text="Tratamiento:",bg = "#00B8FF").place(x=40,y=260)
        datosBoxT = Entry(info, width=30,state="readonly",textvariable = cTratamiento)
        datosBoxT.place(x=170, y=260)

        imgamC= Image.open('images/btnAM.png')
        imgamC = ImageTk.PhotoImage(imgamC)
        btnAMC = Button(info, image=imgamC, borderwidth=0, bg="#EDF0F2", command =lambda: [altaMedica(), close_window(info)]  )
        btnAMC.place(x = 260, y=300)

        imgdC = Image.open('images/btnD.png')
        imgdC = ImageTk.PhotoImage(imgdC)
        btnDC = Button(info, image=imgdC, borderwidth=0, bg="#EDF0F2", command =lambda: selectPacient() )
        btnDC.place(x = 310, y=300)

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
            else:
                infoTree()
            
    #otra opcion para selecionar item del treeview
    def sele(e):
        selected = tree.selection()
        values = tree.item(selected, 'values')
        text = tree.item(selected, 'text')
        indexx = int(values[0])
        if text == listaEnlazada[indexx].getNombre():
            showinfo(title="Paciente " +listaEnlazada[indexx].getNombre(), message="Tomado un hijo "+listaEnlazada[indexx].getNombre())
        print(values)
        print(indexx)
        print(text)  

    inde =0
    # crear el treeview
    tree = ttk.Treeview(root,height = 23)
    # ubica el arbol en la raiz 
    tree.place(x=5,y=15)
    tree.heading('#0', text='Emergencias Medicas', anchor='w')

    tree.insert('', tk.END, text='Solicitar Atencion', iid=0, open=False)

    tree.insert('', tk.END, text=opcionPacientesIngresados, iid=1000, open=False)
    tree.insert('', tk.END, text='Traumatologia', iid=2000, open=False)
    tree.insert('', tk.END, text='Neurologia', iid=3000, open=False)
    tree.insert('', tk.END, text='Cardiologia', iid=4000, open=False)

    tree.insert('', tk.END, text='Dashboard', iid=5000, open=False)
    tree.insert('', tk.END, text=opcionGrafico, iid=5001, open=False)
    tree.insert('', tk.END, text='Analitica De Pacientes', iid=5002, open=False)
    tree.insert('', tk.END, text='Altas Medicas', iid=5003, open=False)



    tree.move(2000,1000,0)
    tree.move(3000,1000,1)
    tree.move(4000,1000,2)

    tree.move(5001,5000,0)
    tree.move(5002,5000,1)
    tree.move(5003,5000,2)

    for i in range(0,listaEnlazada.contador()):
        if listaEnlazada[i].getDespacho() == "traumatologia":
            
            tree.insert('', tk.END, iid=i+1, text=listaEnlazada[i].getNombre(),values=inde, open=False)
            tree.move(i+1,2000,i+1)
        elif listaEnlazada[i].getDespacho() == "neurologia":
            
            tree.insert('', tk.END, iid=i+1, text=listaEnlazada[i].getNombre(),values=inde, open=False)
            tree.move(i+1,3000,i+1)
        elif listaEnlazada[i].getDespacho() == "cardiologia":
            
            tree.insert('', tk.END, iid=i+1, text=listaEnlazada[i].getNombre(),values=inde, open=False)
            tree.move(i+1,4000,i+1)

        
        inde = inde + 1
 

    # control de la opcion escogida
    tree.bind('<Double-1>', item_selected)



def bLimpiar():
    frame = Frame(root, width=422,height=283, bg ="#B3B6B7")
    frame.place(x=600, y=150)
    imgLim = Image.open("images/defLimpiar.png")
    imgLim = ImageTk.PhotoImage(imgLim)
    img_label = tk.Label(image = imgLim , bg="#B3B6B7")
    img_label.Image = imgLim
    img_label.place(x=604, y=200)

    



def mostrarEstado(rut,rutD, rutT, rutN,comprobar):
    if len(comprobar) == 0:
        messagebox.showwarning("Warning","Campo ' rut ' Obligatorio", parent = root)
    else:
        txt = StringVar()
        txt1 = StringVar()
        txt2 = StringVar()
        frame = Frame(root, width=410,height=221, bg ="#B3B6B7")
        frame.place(x=604, y=200)
        
        tNombre = Frame(root,width=413,height=23,bg="#909497" )
        tNombre.place(x=604,y=152)
        tNombreF = Frame(root,width=413,height=25,bg="#B3B6B7" )
        tNombreF.place(x=604,y=175)

        Label(root, text = "Paciente",bg = "#909497", fg="black",height = 1,font=("Cascadia Code PL",12) ).place(x=750,y=150)
        mNombre = Label(root, textvariable= txt2,bg = "#B3B6B7", fg="#0026fe",height = 1,font=("Cascadia Code PL",10) )
        mNombre.place(x=640,y=175)
        txt2.set(rutN) 

        tMedico = Frame(root,width=413,height=30,bg="#909497" )
        tMedico.place(x=604,y=200)
        Label(root, text = "Medico Tratante",bg = "#909497", fg="black",height = 1,font=("Cascadia Code PL",12) ).place(x=750,y=202)
        mMedico = Label(root, textvariable= txt,bg = "#B3B6B7", fg="#0026fe",height = 1,font=("Cascadia Code PL",10) )
        mMedico.place(x=640,y=231)
        txt.set(rut)
        
        
        fDiagnostico = Frame(root,width=413,height=30,bg="#909497" )
        fDiagnostico.place(x=604,y=260)
        Label(root, text = "Diagnostico",bg = "#909497", fg="black",height = 1,font=("Cascadia Code PL",12) ).place(x=750,y=260)
        tdiagnostico = Label(root, textvariable= txt1,bg = "#B3B6B7", fg="#0026fe",height = 1,font=("Cascadia Code PL",10) )
        tdiagnostico.place(x=630,y=295)
        txt1.set(rutD)

        fTratamiento = Frame(root,width=413,height=30,bg="#909497" )
        fTratamiento.place(x=604,y=320)
        Label(root, text = "Tratamiento",bg = "#909497", fg="black",height = 1,font=("Cascadia Code PL",12) ).place(x=750,y=320)
        datosBoxT = Text(root,height = 3.0, width= 48, font=("Cascadia Code PL SemiBold",10) ,bg = "#B3B6B7", fg="#0026fe")
        datosBoxT.insert(1.0,rutT)
        datosBoxT.place(x=615, y=355)

        
    
    




def mostrarDatos(rut, comprobar):


    if len(comprobar) == 0:
        messagebox.showwarning("Warning","Campo ' rut ' Obligatorio", parent = root)
    else:
        frame = Frame(root, width=150,height=271, bg ="#909497")
        frame.place(x=600, y=150)
        Label(root, text = "Nombre",bg = "#909497", fg="black",height = 1,font=("Cascadia Code PL SemiBold",12) ).place(x=610,y=160)
        Label(root, text = "Rut",bg = "#909497", fg="black",height = 1,font=("Cascadia Code PL SemiBold",12) ).place(x=610,y=180)
        Label(root, text = "Sexo",bg = "#909497", fg="black",height = 1,font=("Cascadia Code PL SemiBold",12) ).place(x=610,y=200)
        Label(root, text = "Direccion",bg = "#909497", fg="black",height = 1,font=("Cascadia Code PL SemiBold",12) ).place(x=610,y=220)
        Label(root, text = "Diagnostico I.",bg = "#909497", fg="black",height = 1,font=("Cascadia Code PL SemiBold",12) ).place(x=610,y=240)
        Label(root, text = "Estado",bg = "#909497", fg="black",height = 1,font=("Cascadia Code PL SemiBold",12) ).place(x=610,y=260)
        Label(root, text = "Despacho",bg = "#909497", fg="black",height = 1,font=("Cascadia Code PL SemiBold",12) ).place(x=610,y=280)
        #Label(root, text = "N° de Atencion",bg = "#909497", fg="black",height = 1,font=("Cascadia Code PL SemiBold",12) ).place(x=410,y=360)
        #Label(root, text = "Cama Asig",bg = "#909497", fg="black",height = 1,font=("Cascadia Code PL SemiBold",12) ).place(x=410,y=380)
   

        #textBox muestra datos del paciente
        datosBox = Text(root,height = 11, width= 26, padx=15,pady=15, font=("Cascadia Code PL SemiBold",12) ,bg = "#B3B6B7", fg="#0026fe")
        datosBox.insert(1.0,rut)
        datosBox.place(x=750, y=150)




def ventanaAtencion():

        def close_window(root):
            root.destroy()

        

        def distribuirListas(nombre,rut,sexo,direccion,diagI,estado,despacho):

            if len(nombre) == 0 or len(rut) == 0 or len(direccion) == 0:
                messagebox.showerror("Error", "Todos Los Campos Son Obligatorios", parent=root)
            else:

                listaEnlazada.adicionarFinal(Paciente(nombre,rut,sexo,direccion,diagI,estado,despacho,False    ,medico[0],medico[1],medico[2],medico[3],medico[4],medico[5])) 
                
                #listaCompleta.agregar(Paciente(nombre,rut,sexo,direccion,diagI,estado,despacho,False    ,medico[0],medico[1],medico[2],medico[3],medico[4],medico[5]))

                if despacho == "traumatologia":
                    listaTrauma.adicionarFinal(Paciente(nombre,rut,sexo,direccion,diagI,estado,despacho,False  ,"","","","","","" ))
                elif despacho == "neurologia":
                    listaNeuro.adicionarFinal(Paciente(nombre,rut,sexo,direccion,diagI,estado,despacho,False ,"","","","","","" ))
                elif despacho == "cardiologia":
                    listaCardio.adicionarFinal(Paciente(nombre,rut,sexo,direccion,diagI,estado,despacho,False    ,"","","","","","" ))

                res = messagebox.showinfo("Info","Paciente Registrado", parent = root)
                if res == "ok":
                    close_window(root)

    
           

        
                

        root = Toplevel()
        root.title("Solicitar Atencion")
        root.geometry("450x350")

        header = Frame(root, width = 450, height = 117)
        header.pack()

        #cuerpo
        body = Frame(root, width = 450, height = 233, bg = "#00B8FF")
        body.pack()

        sexos= ["masculino","femenino","otro"]
        estados=["reanimacion","emergencia","urgencia","prioritario","no urgencia"]
        dIniciales=["1-Hemorragia Traumática","2-Impacto de bala","3-Fractura ósea","4-Infección bacteriana","5-otro"]


        

        #labels

        Label(root, text="Nombre:").place(x=40, y=30)
        nombre = Entry(root, width=40)
        nombre.focus()
        nombre.place(x=170,y=30)
        


        Label(root, text="Rut:").place(x=40,y=60)
        rut = Entry(root, width=40)
        rut.place(x=170,y=60)

        Label(root, text="Sexo:").place(x=40,y=90)
        sexo= Spinbox(root, values=sexos)
        sexo.place(x=170,y=90)


        Label(root, text="Direccion:" ,bg = "#00B8FF").place(x=40,y=120)
        direccion = Entry(root, width=40)
        direccion.place(x=170,y=120)

    

        Label(root, text="Diagnostico Inicial:",bg = "#00B8FF").place(x=40,y=150)
        diagI= Spinbox(root, values=dIniciales, width = 30)
        diagI.place(x=170,y=150)
        

        Label(root, text="Estado:",bg = "#00B8FF").place(x=40,y=180)
        estado = Spinbox(root, values=estados)
        estado.place(x=170,y=180)

        Label(root, text="Despacho:",bg = "#00B8FF").place(x=40,y=210)
    
        
        despacho = StringVar()
        trauma = Radiobutton(root,  text="Traumatologia",variable=despacho,value="traumatologia",bg = "#00B8FF")
        trauma.place(x=170,y=210)
        trauma.select()

        neuro = Radiobutton(root,  text="Neurologia",variable=despacho,value="neurologia",bg = "#00B8FF")
        neuro.place(x=170,y=230)

        cardio = Radiobutton(root,  text="Cardiologia", variable=despacho,value="cardiologia",bg = "#00B8FF")
        cardio.place(x=170,y=250)

        
            
        imgAgregar = Image.open('images/solAtenAgregar.png')
        imgAgregar= ImageTk.PhotoImage(imgAgregar)
        agregar = Button(root, image=imgAgregar, borderwidth=0, bg = "#00B8FF", command=lambda: [distribuirListas(nombre.get(),rut.get(),sexo.get(),direccion.get(),diagI.get(),estado.get(),despacho.get()), ActualizaTabla()])
        agregar.place(x=350 ,  y = 280)

        imgBack = Image.open('images/solAtenAtras.png')
        imgBack= ImageTk.PhotoImage(imgBack)
        back = Button(root, image=imgBack, borderwidth=0, bg = "#00B8FF", command=lambda: [ close_window(root)  ])
        back.place(x=280 ,  y = 280)
        
        root.mainloop()





def info(tabla):

        def close_window(root):
            root.destroy()

        def showInfo():
            messagebox.showerror("Error","Todos los campos son obligatorios", parent = info)

        def setInfo(nombre,rut,sexo,diagI,direccion,estado):
            if len(nombre) == 0 or len(rut) == 0 or len(direccion) == 0:
                showInfo()
            else:

                listaEnlazada[index].setNombre(nombre)
                listaEnlazada[index].setRut(rut)
                listaEnlazada[index].setSexo(sexo)
                listaEnlazada[index].setDiagnosticoI(diagI)
                listaEnlazada[index].setDireccion(direccion)
                listaEnlazada[index].setEstado(estado)

                cNom.set(listaEnlazada[index].getNombre())
                cRut.set(listaEnlazada[index].getRut())
                cEstado.set(listaEnlazada[index].getEstado())
                cDiagI.set(listaEnlazada[index].getDiagnosticoI())
                cSexo.set(listaEnlazada[index].getSexo())
                cDireccion.set(listaEnlazada[index].getDireccion())
                messagebox.showinfo("Info","Datos Cambiados Correctamente\n\n Actualice Para Reflejar Cambios En Tabla", parent = info)


                
        def delete(nombre,rut,direccion):
            nombre.delete(0, 'end')
            rut.delete(0, 'end')
            direccion.delete(0, 'end')
                        
            



        cNom = StringVar()
        cRut = StringVar()
        cEstado = StringVar()
        cDiagI = StringVar()
        cSexo = StringVar()
        cDireccion = StringVar()

        selected = tabla.focus()
        values = tabla.item(selected, 'values')
        indexx = int(values[0])
        index = indexx - 1

        cNom.set(listaEnlazada[index].getNombre())
        cRut.set(listaEnlazada[index].getRut())
        cEstado.set(listaEnlazada[index].getEstado())
        cDiagI.set(listaEnlazada[index].getDiagnosticoI())
        cSexo.set(listaEnlazada[index].getSexo())
        cDireccion.set(listaEnlazada[index].getDireccion())
        

        info = Toplevel()
        info.title("Paciente "+listaEnlazada[index].getNombre())
        info.geometry("500x420")
        header = Frame(info, width = 550, height = 120)
        header.pack()
        body = Frame(info, width = 550, height = 380, bg = "#00B8FF")
        body.pack()


        Label(info, text="Nombre:").place(x=40, y=30)
        nombre = Entry(info, width=30,state="readonly",textvariable = cNom)
        nombre.focus()
        nombre.place(x=170,y=30)
        


        Label(info, text="Rut:").place(x=40,y=60)
        rut = Entry(info, width=30,state="readonly",textvariable = cRut)
        rut.place(x=170,y=60)

        Label(info, text="Sexo:").place(x=40,y=90)
        sexo= Entry(info, width=30,state="readonly",textvariable = cSexo)
        sexo.place(x=170,y=90)


        Label(info, text="Direccion:" ,bg = "#00B8FF").place(x=40,y=120)
        direccion = Entry(info, width=30,state="readonly",textvariable = cDireccion)
        direccion.place(x=170,y=120)


        Label(info, text="Diagnostico Inicial:",bg = "#00B8FF").place(x=40,y=150)
        diagI= Entry(info, width=30,state="readonly",textvariable = cDiagI)
        diagI.place(x=170,y=150)
        

        Label(info, text="Estado:",bg = "#00B8FF").place(x=40,y=180)
        estado = Entry(info, width=30,state="readonly",textvariable = cEstado)
        estado.place(x=170,y=180)

        marco = LabelFrame(info, text = "Modificar",bd = 4 , width = 480 , height = 150, bg = "#EDF0F2")
        marco.place(x=10 , y = 220)

        sexos= ["masculino","femenino","otro"]
        estados=["reanimacion","emergencia","urgencia","prioritario","no urgencia"]
        dIniciales=["1-Hemorragia Traumática","2-Impacto de bala","3-Fractura ósea","4-Infección bacteriana","5-otro"]

        #labels

        Label(info, text="Nombre:").place(x=20, y=240)
        nombre = Entry(info, width=15)
        nombre.focus()
        nombre.place(x=80,y=240)
        


        Label(info, text="Rut:").place(x=180,y=240)
        rut = Entry(info, width=15)
        rut.place(x=210,y=240)

        Label(info, text="Sexo:").place(x=310,y=240)
        sexo= Spinbox(info, values=sexos,width=10)
        sexo.place(x=350,y=240)


        Label(info, text="Direccion:").place(x=20,y=280)
        direccion = Entry(info, width=15)
        direccion.place(x=80,y=280)

        Label(info, text="Estado:").place(x=180,y=280)
        estado = Spinbox(info, values=estados, width=15)
        estado.place(x=230,y=280)



        Label(info, text="Diag. Inicial:").place(x=20,y=320)
        diagI= Spinbox(info, values=dIniciales, width = 37)
        diagI.place(x=100,y=320)
        

        
           
        imgAgrega = Image.open('images/btnAM.png')
        imgAgrega= ImageTk.PhotoImage(imgAgrega)
        agrega = Button(info, image=imgAgrega, borderwidth=0,command=lambda:[setInfo(nombre.get(),rut.get(),sexo.get(),diagI.get(),direccion.get(),estado.get()), delete(nombre,rut,direccion) ])
        agrega.place(x=400 ,  y = 310)

        imgBac = Image.open('images/solAtenAtras.png')
        imgBac= ImageTk.PhotoImage(imgBac)
        bac = Button(info, image=imgBac, borderwidth=0, bg = "#00B8FF",command=lambda:close_window(info))
        bac.place(x=410 ,  y = 370)
        



        info.mainloop()


def tratarPacientes():


    def actualizaColas():
        #marco
        marcoTrauma = LabelFrame(roott, text = "Traumatologia",bd = 4 , width = 290 , height = 330, bg = "#EDF0F2")
        marcoTrauma.place(x=30 , y = 25)
        #estilo
        style = ttk.Style()
        style.configure('Treeview', background = "#C0EAF8",foreground = "black", fieldBackground = "#C0EAF8")
        style.theme_use("default")
        style.map('Treeview',background=[('selected','#DCA44C')])
        #creacion de tabla
        tablaT = ttk.Treeview(roott , columns=(0,1, 2), show='headings', height=12)
        tablaT.place(x=50 , y = 50)
        tablaT.tag_configure('oddrow',background="#26C1F4")
        tablaT.tag_configure('evenrow',background="#C0EAF8")
        tablaT.heading(0, text = "N°")
        tablaT.heading(1, text = "Nombre")
        tablaT.heading(2, text = "Rut")
        tablaT.column(0, width = 10, minwidth =25)
        tablaT.column(1, width = 120)
        tablaT.column(2, width = 120)
        #scrollBar
        yscrollbar = ttk.Scrollbar(roott,orient = "vertical", command = tablaT.yview)
        yscrollbar.place(x=300,y=50)
        #yscrollbar.place(x = 300, y =50, fill = Y)

        

    
        #=00=========================================================================================================================================
        #marco
        marcoNeuro = LabelFrame(roott, text = "Neurologia" ,bd = 4 , width = 290 , height = 330, bg = "#EDF0F2")
        marcoNeuro.place(x=380 , y = 25)
        #estilo
        style = ttk.Style()
        style.configure('Treeview', background = "#C0EAF8",foreground = "black", fieldBackground = "#C0EAF8")
        style.theme_use("default")
        style.map('Treeview',background=[('selected','#DCA44C')])
        #creacion de tabla
        tablaN = ttk.Treeview(roott , columns=(0,1, 2), show='headings', height=12)
        tablaN.pack(side="left")
        tablaN.place(x=400 , y = 50)
        tablaN.tag_configure('oddrow',background="#26C1F4")
        tablaN.tag_configure('evenrow',background="#C0EAF8")
        tablaN.heading(0, text = "N°")
        tablaN.heading(1, text = "Nombre")
        tablaN.heading(2, text = "Rut")
        tablaN.column(0, width = 10, minwidth =25)
        tablaN.column(1, width = 120)
        tablaN.column(2, width = 120)

        #scrollBar
        yscrollbar = ttk.Scrollbar(roott,orient = "vertical", command = tablaN.yview)
        yscrollbar.place(x=650,y=50)
        #yscrollbar.place(x = 300, y =50, fill = Y)
        tablaN.configure(yscrollcommand=yscrollbar.set)

        #=======================================================================================================================
        #=00=========================================================================================================================================
        #marco
        marcoCardio = LabelFrame(roott, text = "Cardiologia" ,bd = 4 , width = 290 , height = 330, bg = "#EDF0F2")
        marcoCardio.place(x=730 , y = 25)
        #estilo
        style = ttk.Style()
        style.configure('Treeview', background = "#C0EAF8",foreground = "black", fieldBackground = "#C0EAF8")
        style.theme_use("default")
        style.map('Treeview',background=[('selected','#DCA44C')])
        #creacion de tabla
        tablaC = ttk.Treeview(roott , columns=(0,1, 2), show='headings', height=12)
        tablaC.pack(side="left")
        tablaC.place(x=750 , y = 50)
        tablaC.tag_configure('oddrow',background="#26C1F4")
        tablaC.tag_configure('evenrow',background="#C0EAF8")
        tablaC.heading(0, text = "N°")
        tablaC.heading(1, text = "Nombre")
        tablaC.heading(2, text = "Rut")
        tablaC.column(0, width = 10, minwidth =25)
        tablaC.column(1, width = 120)
        tablaC.column(2, width = 120)

        #scrollBar
        yscrollbar = ttk.Scrollbar(roott,orient = "vertical", command = tablaC.yview)
        yscrollbar.place(x=1000,y=50)
        #yscrollbar.place(x = 300, y =50, fill = Y)
        tablaC.configure(yscrollcommand=yscrollbar.set)
        

        #agregando elementos
        index = 1
        t = 0
        c = 0
        n = 1
        for i in range(0,listaEnlazada.contador()):
            if listaEnlazada[i].getDespacho() == "traumatologia":
                if t % 2 == 0:
                    tablaT.insert(parent='', index=i, iid=i, values=(index,listaEnlazada[i].getNombre(), listaEnlazada[i].getRut()), tags = ('evenrow'))
                    
                else:
                    tablaT.insert(parent='', index=i, iid=i, values=(index,listaEnlazada[i].getNombre(), listaEnlazada[i].getRut()), tags = ('oddrow'))
                    
                t+=1    
            elif listaEnlazada[i].getDespacho() == "cardiologia":
                if index % 2 == 0:
                    tablaC.insert(parent='', index=i, iid=i, values=(index,listaEnlazada[i].getNombre(), listaEnlazada[i].getRut()), tags = ('evenrow'))
                    
                else:
                    tablaC.insert(parent='', index=i, iid=i, values=(index,listaEnlazada[i].getNombre(), listaEnlazada[i].getRut()), tags = ('oddrow'))        
                c+=1
            else:
                if index % 2 == 0:
                    tablaN.insert(parent='', index=i, iid=i, values=(index,listaEnlazada[i].getNombre(), listaEnlazada[i].getRut()), tags = ('evenrow'))
                    
                else:
                    tablaN.insert(parent='', index=i, iid=i, values=(index,listaEnlazada[i].getNombre(), listaEnlazada[i].getRut()), tags = ('oddrow'))    
                n+=1
        
            index += 1
        
        #botones Trauma
        imgL = Image.open('images/btnAM.png')
        imgL = ImageTk.PhotoImage(imgL)
        btnAM = Button(roott, image=imgL, borderwidth=0, bg="#EDF0F2", command =lambda: [altaMedica(tablaT), showInfo()]  )
        btnAM.place(x = 265, y=310)

        img = Image.open('images/btnD.png')
        img = ImageTk.PhotoImage(img)
        btnD = Button(roott, image=img, borderwidth=0, bg="#EDF0F2", command =lambda: selectPacient(tablaT)  )
        btnD.place(x = 225, y=310)

        imgC = Image.open('images/btnInfo.png')
        imgC = ImageTk.PhotoImage(imgC)
        btnC = Button(roott, image=imgC, borderwidth=0, bg="#EDF0F2", command =lambda: [info(tablaT)]  )
        btnC.place(x = 185, y=310)

        #botones Neurologia
        
        imgamN= Image.open('images/btnAM.png')
        imgamN = ImageTk.PhotoImage(imgamN)
        btnAMN = Button(roott, image=imgamN, borderwidth=0, bg="#EDF0F2", command =lambda: [altaMedica(tablaN), showInfo()]  )
        btnAMN.place(x = 620, y=310)

        imgdn = Image.open('images/btnD.png')
        imgdn = ImageTk.PhotoImage(imgdn)
        btnDn = Button(roott, image=imgdn, borderwidth=0, bg="#EDF0F2", command =lambda: selectPacient(tablaN)  )
        btnDn.place(x = 580, y=310)

        imgmn = Image.open('images/btnInfo.png')
        imgmn = ImageTk.PhotoImage(imgmn)
        btnMn= Button(roott, image=imgmn, borderwidth=0, bg="#EDF0F2", command =lambda: [info(tablaN)]  )
        btnMn.place(x = 540, y=310)

        #botones Cradiologia
        
        imgamC= Image.open('images/btnAM.png')
        imgamC = ImageTk.PhotoImage(imgamC)
        btnAMC = Button(roott, image=imgamC, borderwidth=0, bg="#EDF0F2", command =lambda: [altaMedica(tablaC), showInfo()]  )
        btnAMC.place(x = 970, y=310)

        imgdC = Image.open('images/btnD.png')
        imgdC = ImageTk.PhotoImage(imgdC)
        btnDC = Button(roott, image=imgdC, borderwidth=0, bg="#EDF0F2", command =lambda: selectPacient(tablaC)  )
        btnDC.place(x = 930, y=310)

        imgmC = Image.open('images/btnInfo.png')
        imgmC = ImageTk.PhotoImage(imgmC)
        btnMC= Button(roott, image=imgmC, borderwidth=0, bg="#EDF0F2", command =lambda: [info(tablaC)]  )
        btnMC.place(x = 890, y=310)

        roott.mainloop()


    def selectPacient(tabla):


        def close_window(root):
            root.destroy()

        def guardaT():
            
            
            listaEnlazada[index].setDiagnostico(diagnostico.get())
            listaEnlazada[index].setTratamiento(tratamiento.get("1.0","end"))

        top = Toplevel(roott)
        top.geometry("350x270")
        top.title("Diagnostico")
        header = Frame(top, width = 500, height = 120)
        header.pack()
        body = Frame(top, width = 500, height = 380, bg = "#00B8FF")
        body.pack()
        
        selected = tabla.focus()
        values = tabla.item(selected, 'values')
        indexx = int(values[0])
        index = indexx - 1
        
        

        tk.Label(top, text="Diagnostico:").place(x=125 , y = 10)
        diagnostico = tk.Entry(top, width=40)
        diagnostico.place(x = 50, y = 30)

        tk.Label(top, text="Tratamiento:").place(x = 125, y = 50)
        tratamiento =  tk.Text(top, height = 5, width= 25, padx=15,pady=15)
        tratamiento.place(x= 50, y = 70)

    
        
                
        imgAgrega = Image.open('images/solAtenAgregar.png')
        imgAgrega= ImageTk.PhotoImage(imgAgrega)
        agrega = Button(top, image=imgAgrega, borderwidth=0, bg = "#00B8FF",command=lambda:[guardaT(), close_window(top)]   )
        agrega.place(x=210 ,  y = 200)

        imgBac = Image.open('images/solAtenAtras.png')
        imgBac= ImageTk.PhotoImage(imgBac)
        bac = Button(top, image=imgBac, borderwidth=0, bg = "#00B8FF",command=lambda:close_window(top))
        bac.place(x= 280,  y = 200)
        #guardaB = Button(top, text="Diagnosticar", width=50, bg = "#00B8FF", command=lambda: [print(index), guardaT(), close_window(top)])
        #guardaB.pack(pady = 5)

        top.mainloop()

    
    def altaMedica(tabla):
        
        selected = tabla.focus()
        values = tabla.item(selected, 'values')
        indexx = int(values[0])
        index = indexx - 1
        listaEnlazada[index].setaltaMedica()

        listaPacientesAM.adicionarFinal(Paciente(listaEnlazada[index].getNombre(),listaEnlazada[index].getRut(),listaEnlazada[index].getSexo(),listaEnlazada[index].getDireccion(),listaEnlazada[index].getDiagnosticoI(),listaEnlazada[index].getEstado(),listaEnlazada[index].getDespacho(),True ,listaEnlazada[index].getNombreM(),listaEnlazada[index].getRutM(),listaEnlazada[index].getDiagnostico(),listaEnlazada[index].getTratamiento(),listaEnlazada[index].getIdEspecialista(),listaEnlazada[index].getNombreEspecialidad()))
        
        rutActual = listaEnlazada[index].getRut()
        listaEnlazada.borrarPorRut(rutActual)
    



    def showInfo():
        resp = messagebox.showinfo("Info","Alta Medica Completa\n\n", parent = roott)
        if resp == "ok":
            actualizaColas()
        

    
        

    
    roott = Toplevel()
    roott.title("Tratar Paciente")
    roott.geometry("1100x400")
    header = Frame(roott, width = 1200, height = 120, bg = "white")
    header.pack()
    body = Frame(roott, width = 1200, height = 380, bg = "#00B8FF")
    body.pack()

    

    #marco
    marcoTrauma = LabelFrame(roott, text = "Traumatologia",bd = 4 , width = 290 , height = 330, bg = "#EDF0F2")
    marcoTrauma.place(x=30 , y = 25)
    #estilo
    style = ttk.Style()
    style.configure('Treeview', background = "#C0EAF8",foreground = "black", fieldBackground = "#C0EAF8")
    style.theme_use("default")
    style.map('Treeview',background=[('selected','#DCA44C')])
    #creacion de tabla
    tablaT = ttk.Treeview(roott , columns=(0,1, 2), show='headings', height=12)
    tablaT.place(x=50 , y = 50)
    tablaT.tag_configure('oddrow',background="#26C1F4")
    tablaT.tag_configure('evenrow',background="#C0EAF8")
    tablaT.heading(0, text = "N°")
    tablaT.heading(1, text = "Nombre")
    tablaT.heading(2, text = "Rut")
    tablaT.column(0, width = 10, minwidth =25)
    tablaT.column(1, width = 120)
    tablaT.column(2, width = 120)
    #scrollBar
    yscrollbar = ttk.Scrollbar(roott,orient = "vertical", command = tablaT.yview)
    yscrollbar.place(x=300,y=50)
    #yscrollbar.place(x = 300, y =50, fill = Y)

    

   
    #=00=========================================================================================================================================
    #marco
    marcoNeuro = LabelFrame(roott, text = "Neurologia" ,bd = 4 , width = 290 , height = 330, bg = "#EDF0F2")
    marcoNeuro.place(x=380 , y = 25)
    #estilo
    style = ttk.Style()
    style.configure('Treeview', background = "#C0EAF8",foreground = "black", fieldBackground = "#C0EAF8")
    style.theme_use("default")
    style.map('Treeview',background=[('selected','#DCA44C')])
    #creacion de tabla
    tablaN = ttk.Treeview(roott , columns=(0,1, 2), show='headings', height=12)
    tablaN.pack(side="left")
    tablaN.place(x=400 , y = 50)
    tablaN.tag_configure('oddrow',background="#26C1F4")
    tablaN.tag_configure('evenrow',background="#C0EAF8")
    tablaN.heading(0, text = "N°")
    tablaN.heading(1, text = "Nombre")
    tablaN.heading(2, text = "Rut")
    tablaN.column(0, width = 10, minwidth =25)
    tablaN.column(1, width = 120)
    tablaN.column(2, width = 120)

    #scrollBar
    yscrollbar = ttk.Scrollbar(roott,orient = "vertical", command = tablaN.yview)
    yscrollbar.place(x=650,y=50)
    #yscrollbar.place(x = 300, y =50, fill = Y)
    tablaN.configure(yscrollcommand=yscrollbar.set)

    #=======================================================================================================================
     #=00=========================================================================================================================================
    #marco
    marcoCardio = LabelFrame(roott, text = "Cardiologia" ,bd = 4 , width = 290 , height = 330, bg = "#EDF0F2")
    marcoCardio.place(x=730 , y = 25)
    #estilo
    style = ttk.Style()
    style.configure('Treeview', background = "#C0EAF8",foreground = "black", fieldBackground = "#C0EAF8")
    style.theme_use("default")
    style.map('Treeview',background=[('selected','#DCA44C')])
    #creacion de tabla
    tablaC = ttk.Treeview(roott , columns=(0,1, 2), show='headings', height=12)
    tablaC.pack(side="left")
    tablaC.place(x=750 , y = 50)
    tablaC.tag_configure('oddrow',background="#26C1F4")
    tablaC.tag_configure('evenrow',background="#C0EAF8")
    tablaC.heading(0, text = "N°")
    tablaC.heading(1, text = "Nombre")
    tablaC.heading(2, text = "Rut")
    tablaC.column(0, width = 10, minwidth =25)
    tablaC.column(1, width = 120)
    tablaC.column(2, width = 120)

    #scrollBar
    yscrollbar = ttk.Scrollbar(roott,orient = "vertical", command = tablaC.yview)
    yscrollbar.place(x=1000,y=50)
    #yscrollbar.place(x = 300, y =50, fill = Y)
    tablaC.configure(yscrollcommand=yscrollbar.set)
    

    #agregando elementos
    index = 1
    t = 0
    c = 0
    n = 1
    for i in range(0,listaEnlazada.contador()):
        if listaEnlazada[i].getDespacho() == "traumatologia":
            if t % 2 == 0:
                tablaT.insert(parent='', index=i, iid=i, values=(index,listaEnlazada[i].getNombre(), listaEnlazada[i].getRut()), tags = ('evenrow'))
                
            else:
                tablaT.insert(parent='', index=i, iid=i, values=(index,listaEnlazada[i].getNombre(), listaEnlazada[i].getRut()), tags = ('oddrow'))
                
            t+=1    
        elif listaEnlazada[i].getDespacho() == "cardiologia":
            if index % 2 == 0:
                tablaC.insert(parent='', index=i, iid=i, values=(index,listaEnlazada[i].getNombre(), listaEnlazada[i].getRut()), tags = ('evenrow'))
                
            else:
                tablaC.insert(parent='', index=i, iid=i, values=(index,listaEnlazada[i].getNombre(), listaEnlazada[i].getRut()), tags = ('oddrow'))        
            c+=1
        else:
            if index % 2 == 0:
                tablaN.insert(parent='', index=i, iid=i, values=(index,listaEnlazada[i].getNombre(), listaEnlazada[i].getRut()), tags = ('evenrow'))
                
            else:
                tablaN.insert(parent='', index=i, iid=i, values=(index,listaEnlazada[i].getNombre(), listaEnlazada[i].getRut()), tags = ('oddrow'))    
            n+=1
     
        index += 1
    
    #botones Trauma
    imgL = Image.open('images/btnAM.png')
    imgL = ImageTk.PhotoImage(imgL)
    btnAM = Button(roott, image=imgL, borderwidth=0, bg="#EDF0F2", command =lambda: [altaMedica(tablaT), showInfo()]  )
    btnAM.place(x = 265, y=310)

    img = Image.open('images/btnD.png')
    img = ImageTk.PhotoImage(img)
    btnD = Button(roott, image=img, borderwidth=0, bg="#EDF0F2", command =lambda: selectPacient(tablaT)  )
    btnD.place(x = 225, y=310)

    imgC = Image.open('images/btnInfo.png')
    imgC = ImageTk.PhotoImage(imgC)
    btnC = Button(roott, image=imgC, borderwidth=0, bg="#EDF0F2", command =lambda: [info(tablaT)]  )
    btnC.place(x = 185, y=310)

    #botones Neurologia
    
    imgamN= Image.open('images/btnAM.png')
    imgamN = ImageTk.PhotoImage(imgamN)
    btnAMN = Button(roott, image=imgamN, borderwidth=0, bg="#EDF0F2", command =lambda: [altaMedica(tablaN), showInfo()]  )
    btnAMN.place(x = 620, y=310)

    imgdn = Image.open('images/btnD.png')
    imgdn = ImageTk.PhotoImage(imgdn)
    btnDn = Button(roott, image=imgdn, borderwidth=0, bg="#EDF0F2", command =lambda: selectPacient(tablaN)  )
    btnDn.place(x = 580, y=310)

    imgmn = Image.open('images/btnInfo.png')
    imgmn = ImageTk.PhotoImage(imgmn)
    btnMn= Button(roott, image=imgmn, borderwidth=0, bg="#EDF0F2", command =lambda: [info(tablaN)]  )
    btnMn.place(x = 540, y=310)

    #botones Cradiologia
    
    imgamC= Image.open('images/btnAM.png')
    imgamC = ImageTk.PhotoImage(imgamC)
    btnAMC = Button(roott, image=imgamC, borderwidth=0, bg="#EDF0F2", command =lambda: [altaMedica(tablaC), showInfo()]  )
    btnAMC.place(x = 970, y=310)

    imgdC = Image.open('images/btnD.png')
    imgdC = ImageTk.PhotoImage(imgdC)
    btnDC = Button(roott, image=imgdC, borderwidth=0, bg="#EDF0F2", command =lambda: selectPacient(tablaC)  )
    btnDC.place(x = 930, y=310)

    imgmC = Image.open('images/btnInfo.png')
    imgmC = ImageTk.PhotoImage(imgmC)
    btnMC= Button(roott, image=imgmC, borderwidth=0, bg="#EDF0F2", command =lambda: [info(tablaC)]  )
    btnMC.place(x = 890, y=310)
    
    

    

    
    roott.mainloop()







def ActualizaTabla():

    marcoTodos = LabelFrame(root, text = "Pacientes Ingresados",bd = 4 , width = 290 , height = 325, bg = "#EDF0F2")
    marcoTodos.place(x=1100 , y = 175)
    #estilo
    style = ttk.Style()
    style.configure('Treeview', background = "#C0EAF8",foreground = "black", fieldBackground = "#C0EAF8")
    style.theme_use("default")
    style.map('Treeview',background=[('selected','#DCA44C')])
    #creacion de tabla
    tablaTodos = ttk.Treeview(root , columns=(0,1, 2), show='headings', height=12)
    tablaTodos.place(x=1120, y=200)
    tablaTodos.tag_configure('oddrow',background="#26C1F4")
    tablaTodos.tag_configure('evenrow',background="#C0EAF8")
    tablaTodos.heading(0, text = "N°")
    tablaTodos.heading(1, text = "Nombre")
    tablaTodos.heading(2, text = "Rut")
    tablaTodos.column(0, width = 10, minwidth =25)
    tablaTodos.column(1, width = 120)
    tablaTodos.column(2, width = 120)



    #agregando elementos
    index = 1
    for i in range(0,listaEnlazada.contador()):

        if index % 2 == 0:
            tablaTodos.insert(parent='', index=i, iid=i, values=(index,listaEnlazada[i].getNombre(), listaEnlazada[i].getRut()), tags = ('evenrow'))
            
        else:
            tablaTodos.insert(parent='', index=i, iid=i, values=(index,listaEnlazada[i].getNombre(), listaEnlazada[i].getRut()), tags = ('oddrow'))
            
        index+=1

    
    btnC = Button(root, text="i", borderwidth=0, bg="#0026fe", fg = "white",font=("Cascadia Code PL",10,'bold') ,width=2,height=1, command =lambda: [info(tablaTodos)]  )
    btnC.place(x = 1180, y=462)

    #=================================================================
    treeInit()


   
def dashboard():
    
    

    def mayor():
        if listaTrauma.contador() > listaNeuro.contador() and listaTrauma.contador() > listaCardio.contador():
                return "(Traumatologia)"
        elif listaNeuro.contador() > listaCardio.contador() and listaNeuro.contador() > listaTrauma.contador():
                return "(Neurologia)"
        elif listaCardio.contador() > listaNeuro.contador() and listaCardio.contador() > listaTrauma.contador() :
                return "(Cardiologia)"
        else:
            return ""
    def menor():
        if listaTrauma.contador() < listaNeuro.contador() and listaTrauma.contador() < listaCardio.contador():
                return "(Traumatologia)"
        elif listaNeuro.contador() < listaCardio.contador() and listaNeuro.contador() < listaTrauma.contador():
                return "(Neurologia)"
        elif listaCardio.contador() < listaNeuro.contador() and listaCardio.contador() < listaTrauma.contador() :
                return "(Cardiologia)"
        else:
            return ""


        cont = 0
        for x in range(0,listaEnlazada.contador()):
            if listaEnlazada[x].getDiagnosticoI() == "1-Hemorragia Traumática":
                cont = cont + 1
        return cont
    
    def contDiagnostico():
        tipo1 = 0
        tipo2 = 0
        tipo3 = 0
        tipo4 = 0
        tipo5 = 0
        for x in range(0,listaEnlazada.contador()):
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
        
        result = "Hemorragia Traumatica: "+str(tipo1)
        re = "\nImpacto de bala: "+str(tipo2)+"\nFractura Osea: "+str(tipo3)+"\nInfeccion bacteriana: "+str(tipo4)+"\nOtro: "+str(tipo5)
        return result + re
        


    trauma = np.array(listaTrauma.contador()).astype(int)

    neuro = np.array(listaNeuro.contador()).astype(int)

    cardio = np.array(listaCardio.contador()).astype(int)

    totalPacientes= [listaTrauma.contador(),listaNeuro.contador(),listaCardio.contador()]


    #-------- ESTADISTICAS TODOS LOS Pacientes

    mayorTodos=np.max(totalPacientes)  # Valor máximo de los elementos del array

    menorTodos=np.min(totalPacientes)   # Valor mínimo de los elementos del array

    mediaTodos=np.mean(totalPacientes)  # Valor medio de los elementos del array

    stdTodos=np.std(totalPacientes)   # Desviación típica de los elementos del array

    sumaTodos=np.sum(totalPacientes)   # Suma de todos los elementos del array

    

        #-------- ESTADISTICAS CADA TIPO 

    mediaTrauma=trauma.mean()  

    mediaNeuro=neuro.mean()  

    mediaCardio=cardio.mean()       

    Txt_1  = StringVar()

    Txt_2  = StringVar()

    Txt_3  = StringVar()

    Txt_4  = StringVar()

    Txt_5  = StringVar()

    Txt_7  = StringVar()

    Txt_8  = StringVar()

    Txt_9  = StringVar()       

    Txt_0  = StringVar()

    txtHT = StringVar() 

    popup = Toplevel()

    popup.geometry("1150x450")

    popup.wm_title("Análitica de Pacientes")
    popup.configure(bg="#C0EAF8")
    
    
    
    Txt_0.set("Análitica De Pacientes \nPor Especialidad")
    

    Txt_1.set("Mayor: "+str(mayorTodos)+"  "+str(mayor()))

    Txt_2.set("Menor: "+str(menorTodos)+"  "+str(menor()))

    Txt_3.set("Media: "+str(mediaTodos))

    Txt_4.set("Std: "+str(stdTodos))

    Txt_5.set("Total: "+str(sumaTodos))     

    Txt_7.set("Promedio Traumatologia: "+str(mediaTrauma))     

    Txt_8.set("Promedio Neurologia: "+str(mediaNeuro))

    Txt_9.set("Promedio Cardiologia: "+str(mediaCardio)) 

    txtHT.set(contDiagnostico())  

    mayorE = Frame(popup, width=320, height=340, bg = "#00B8FF")
    mayorE.place(x=20,y=20)

    Frame(popup, width=320, height=60, bg = "light grey").place(x=20,y=20)


    Label(popup, textvariable = Txt_0,bg = "light grey", fg="black",font=("Cascadia Code PL SemiBold",12) ).place(x=30,y=30)

    Label(popup, textvariable = Txt_1,bg = "#00B8FF", fg="black",height = 1,font=("Cascadia Code PL SemiBold",10) ).place(x=30,y=90)
    Label(popup, textvariable = Txt_2,bg = "#00B8FF", fg="black",height = 1,font=("Cascadia Code PL SemiBold",10) ).place(x=30,y=110)
    Label(popup, textvariable = Txt_5,bg = "#00B8FF", fg="black",height = 1,font=("Cascadia Code PL SemiBold",10) ).place(x=30,y=130)
    Label(popup, textvariable = Txt_3,bg = "#00B8FF", fg="black",height = 1,font=("Cascadia Code PL SemiBold",10) ).place(x=30,y=150)
    Label(popup, textvariable = Txt_4,bg = "#00B8FF", fg="black",height = 1,font=("Cascadia Code PL SemiBold",10) ).place(x=30,y=170)
    Label(popup, textvariable = Txt_7,bg = "#00B8FF", fg="black",height = 1,font=("Cascadia Code PL SemiBold",10) ).place(x=30,y=190)
    Label(popup, textvariable = Txt_8,bg = "#00B8FF", fg="black",height = 1,font=("Cascadia Code PL SemiBold",10) ).place(x=30,y=210)
    Label(popup, textvariable = Txt_9,bg = "#00B8FF", fg="black",height = 1,font=("Cascadia Code PL SemiBold",10) ).place(x=30,y=230)
    #Label(popup, text =  "Pacientes Por Diag. Inicial",bg = "#00B8FF", fg="red",height = 1,font=("Cascadia Code PL SemiBold",11) ).place(x=30,y=180)
    #Label(popup, text = "Hemorragia Traumática: ",bg = "#00B8FF", fg="black",font=("Cascadia Code PL SemiBold",10) ).place(x=30,y=210)
    Label(popup, textvariable = txtHT,bg = "#00B8FF", fg="black",font=("Cascadia Code PL SemiBold",10) ).place(x=30,y=250)

    
    #imgI = Image.open('images/grafico.png')
    #imgI = ImageTk.PhotoImage(imgI)
    #listaE = Button(popup, image=imgI, bg="#C0EAF8",borderwidth=0,command=lambda: [graficarDatos()] )
    #listaE.place(x=470,y=373)

    #=======================

    marcoTodos = LabelFrame(popup, text = "Pacientes Con Alta Medica",bd = 4 , width = 290 , height = 318, bg = "#EDF0F2")
    marcoTodos.place(x=370 , y = 30)
    #estilo
    style = ttk.Style()
    style.configure('Treeview', background = "#C0EAF8",foreground = "black", fieldBackground = "#C0EAF8")
    style.theme_use("default")
    style.map('Treeview',background=[('selected','#DCA44C')])
    #creacion de tabla
    tablaTodos = ttk.Treeview(popup , columns=(0,1, 2), show='headings', height=12)
    tablaTodos.place(x=385, y=55)
    tablaTodos.tag_configure('oddrow',background="#26C1F4")
    tablaTodos.tag_configure('evenrow',background="#C0EAF8")
    tablaTodos.heading(0, text = "N°")
    tablaTodos.heading(1, text = "Nombre")
    tablaTodos.heading(2, text = "Rut")
    tablaTodos.column(0, width = 10, minwidth =25)
    tablaTodos.column(1, width = 120)
    tablaTodos.column(2, width = 120)



    #agregando elementos
    index = 1
    for i in range(0,listaPacientesAM.contador()):

        if index % 2 == 0:
            tablaTodos.insert(parent='', index=i, iid=i, values=(index,listaPacientesAM[i].getNombre(), listaPacientesAM[i].getRut()), tags = ('evenrow'))
            
        else:
            tablaTodos.insert(parent='', index=i, iid=i, values=(index,listaPacientesAM[i].getNombre(), listaPacientesAM[i].getRut()), tags = ('oddrow'))
            
        index+=1

    fig = plt.Figure(figsize=(4,4))
    a = fig.add_subplot(111)
    a.pie([listaTrauma.contador(),listaNeuro.contador(),listaCardio.contador()]) #an example data
    a.legend(["TRAUMATOLOGIA","NEUROLOGIA","CARDIOLOGIA"],prop={'size':9}, bbox_to_anchor=(1.1, 0.1))
    a.set_title("Pacientes Ingresados")
    canvas = FigureCanvasTkAgg(fig, master=popup)
    canvas.get_tk_widget().place(x=700,y=30)
    canvas.draw()

    

    popup.mainloop()

def graficarDatos() :

    tT=[]

    tT.append(listaCardio.contador())

    tT.append(listaTrauma.contador())

    tT.append(listaNeuro.contador()) 

    pl.pie(tT,labels=["Cardiologia","Traumalogia","Neurologia"])

    pl.title("PACIENTES INGRESADOS")          

    pl.show()

def analitica():
    
    def mayor():
        if listaTrauma.contador() > listaNeuro.contador() and listaTrauma.contador() > listaCardio.contador():
                return "(Traumatologia)"
        elif listaNeuro.contador() > listaCardio.contador() and listaNeuro.contador() > listaTrauma.contador():
                return "(Neurologia)"
        elif listaCardio.contador() > listaNeuro.contador() and listaCardio.contador() > listaTrauma.contador() :
                return "(Cardiologia)"
        else:
            return ""
    def menor():
        if listaTrauma.contador() < listaNeuro.contador() and listaTrauma.contador() < listaCardio.contador():
                return "(Traumatologia)"
        elif listaNeuro.contador() < listaCardio.contador() and listaNeuro.contador() < listaTrauma.contador():
                return "(Neurologia)"
        elif listaCardio.contador() < listaNeuro.contador() and listaCardio.contador() < listaTrauma.contador() :
                return "(Cardiologia)"
        else:
            return ""


        cont = 0
        for x in range(0,listaEnlazada.contador()):
            if listaEnlazada[x].getDiagnosticoI() == "1-Hemorragia Traumática":
                cont = cont + 1
        return cont
    
    def contDiagnostico():
        tipo1 = 0
        tipo2 = 0
        tipo3 = 0
        tipo4 = 0
        tipo5 = 0
        for x in range(0,listaEnlazada.contador()):
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
        
        result = "Hemorragia Traumatica: "+str(tipo1)
        re = "\nImpacto de bala: "+str(tipo2)+"\nFractura Osea: "+str(tipo3)+"\nInfeccion bacteriana: "+str(tipo4)+"\nOtro: "+str(tipo5)
        return result + re
        


    trauma = np.array(listaTrauma.contador()).astype(int)

    neuro = np.array(listaNeuro.contador()).astype(int)

    cardio = np.array(listaCardio.contador()).astype(int)

    totalPacientes= [listaTrauma.contador(),listaNeuro.contador(),listaCardio.contador()]


    #-------- ESTADISTICAS TODOS LOS Pacientes

    mayorTodos=np.max(totalPacientes)  # Valor máximo de los elementos del array

    menorTodos=np.min(totalPacientes)   # Valor mínimo de los elementos del array

    mediaTodos=np.mean(totalPacientes)  # Valor medio de los elementos del array

    stdTodos=np.std(totalPacientes)   # Desviación típica de los elementos del array

    sumaTodos=np.sum(totalPacientes)   # Suma de todos los elementos del array

    

        #-------- ESTADISTICAS CADA TIPO 

    mediaTrauma=trauma.mean()  

    mediaNeuro=neuro.mean()  

    mediaCardio=cardio.mean()       

    Txt_1  = StringVar()

    Txt_2  = StringVar()

    Txt_3  = StringVar()

    Txt_4  = StringVar()

    Txt_5  = StringVar()

    Txt_7  = StringVar()

    Txt_8  = StringVar()

    Txt_9  = StringVar()       

    Txt_0  = StringVar()

    txtHT = StringVar() 

    popup = Toplevel()

    popup.geometry("400x450")

    popup.wm_title("Análitica de Pacientes")
    popup.configure(bg="#C0EAF8")
    
    
    
    Txt_0.set("Análitica De Pacientes \nPor Especialidad")
    

    Txt_1.set("Mayor: "+str(mayorTodos)+"  "+str(mayor()))

    Txt_2.set("Menor: "+str(menorTodos)+"  "+str(menor()))

    Txt_3.set("Media: "+str(mediaTodos))

    Txt_4.set("Std: "+str(stdTodos))

    Txt_5.set("Total: "+str(sumaTodos))     

    Txt_7.set("Promedio Traumatologia: "+str(mediaTrauma))     

    Txt_8.set("Promedio Neurologia: "+str(mediaNeuro))

    Txt_9.set("Promedio Cardiologia: "+str(mediaCardio)) 

    txtHT.set(contDiagnostico())  

    mayorE = Frame(popup, width=320, height=340, bg = "#00B8FF")
    mayorE.place(x=20,y=20)

    Frame(popup, width=320, height=60, bg = "light grey").place(x=20,y=20)


    Label(popup, textvariable = Txt_0,bg = "light grey", fg="black",font=("Cascadia Code PL SemiBold",12) ).place(x=30,y=30)

    Label(popup, textvariable = Txt_1,bg = "#00B8FF", fg="black",height = 1,font=("Cascadia Code PL SemiBold",10) ).place(x=30,y=90)
    Label(popup, textvariable = Txt_2,bg = "#00B8FF", fg="black",height = 1,font=("Cascadia Code PL SemiBold",10) ).place(x=30,y=110)
    Label(popup, textvariable = Txt_5,bg = "#00B8FF", fg="black",height = 1,font=("Cascadia Code PL SemiBold",10) ).place(x=30,y=130)
    Label(popup, textvariable = Txt_3,bg = "#00B8FF", fg="black",height = 1,font=("Cascadia Code PL SemiBold",10) ).place(x=30,y=150)
    Label(popup, textvariable = Txt_4,bg = "#00B8FF", fg="black",height = 1,font=("Cascadia Code PL SemiBold",10) ).place(x=30,y=170)
    Label(popup, textvariable = Txt_7,bg = "#00B8FF", fg="black",height = 1,font=("Cascadia Code PL SemiBold",10) ).place(x=30,y=190)
    Label(popup, textvariable = Txt_8,bg = "#00B8FF", fg="black",height = 1,font=("Cascadia Code PL SemiBold",10) ).place(x=30,y=210)
    Label(popup, textvariable = Txt_9,bg = "#00B8FF", fg="black",height = 1,font=("Cascadia Code PL SemiBold",10) ).place(x=30,y=230)
    #Label(popup, text =  "Pacientes Por Diag. Inicial",bg = "#00B8FF", fg="red",height = 1,font=("Cascadia Code PL SemiBold",11) ).place(x=30,y=180)
    #Label(popup, text = "Hemorragia Traumática: ",bg = "#00B8FF", fg="black",font=("Cascadia Code PL SemiBold",10) ).place(x=30,y=210)
    Label(popup, textvariable = txtHT,bg = "#00B8FF", fg="black",font=("Cascadia Code PL SemiBold",10) ).place(x=30,y=250)

def tablaAM():

    popup = Tk()
    popup.geometry("400x400")
    popup.title("Pacientes Alta Medica")
    #=======================

    marcoTodos = LabelFrame(popup, text = "Pacientes Con Alta Medica",bd = 4 , width = 290 , height = 318, bg = "#EDF0F2")
    marcoTodos.place(x=50 , y = 30)
    #estilo
    style = ttk.Style()
    style.configure('Treeview', background = "#C0EAF8",foreground = "black", fieldBackground = "#C0EAF8")
    style.theme_use("default")
    style.map('Treeview',background=[('selected','#DCA44C')])
    #creacion de tabla
    tablaTodos = ttk.Treeview(popup , columns=(0,1, 2), show='headings', height=12)
    tablaTodos.place(x=70, y=55)
    tablaTodos.tag_configure('oddrow',background="#26C1F4")
    tablaTodos.tag_configure('evenrow',background="#C0EAF8")
    tablaTodos.heading(0, text = "N°")
    tablaTodos.heading(1, text = "Nombre")
    tablaTodos.heading(2, text = "Rut")
    tablaTodos.column(0, width = 10, minwidth =25)
    tablaTodos.column(1, width = 120)
    tablaTodos.column(2, width = 120)



    #agregando elementos
    index = 1
    for i in range(0,listaPacientesAM.contador()):

        if index % 2 == 0:
            tablaTodos.insert(parent='', index=i, iid=i, values=(index,listaPacientesAM[i].getNombre(), listaPacientesAM[i].getRut()), tags = ('evenrow'))
            
        else:
            tablaTodos.insert(parent='', index=i, iid=i, values=(index,listaPacientesAM[i].getNombre(), listaPacientesAM[i].getRut()), tags = ('oddrow'))
            
        index+=1
    popup.mainloop

root = Tk()
root.title("Emergencias Medicas")
 

root.geometry("1425x525")



#encabezado -> logo
header = Frame(root, width = 1425, height = 160, bg = "white")
header.grid(columnspan = 5, row = 0)

#cuerpo
body = Frame(root, width = 1425, height = 390, bg = "#0026fe")
body.grid(columnspan = 5, row = 1)






# Treeview
treeInit()



#============================================================================

#botones principales

#boton atencion
img = Image.open("images/solicitarA.png")
img = ImageTk.PhotoImage(img)
agregar_btn = Button(root, image=img, borderwidth=0, command=lambda: ventanaAtencion())
agregar_btn.place(x=700, y=40)

#boton medico esp
imgM = Image.open('images/diag.png')
imgM = ImageTk.PhotoImage(imgM)
agregar_medicoE = Button(root, image=imgM, borderwidth=0, command=lambda: tratarPacientes())
agregar_medicoE.place(x=950, y=40)

#boton dashboard
imgI = Image.open('images/dashboad.png')
imgI = ImageTk.PhotoImage(imgI)
listaE = Button(root, image=imgI, borderwidth=0,command=lambda: dashboard() )
listaE.place(x = 1200 , y = 40)


#Buscar Paciente

Label(root, text = "Buscar Paciente",bg="#0026fe",fg="white",height = 1,font=("Aharoni",12,'bold') ).place(x=290,y=200)
Label(root, text = "rut: ",bg="#0026fe",fg="white",height = 1,font=("Aharoni",12,'bold') ).place(x=240, y=270 )

#Buscar Paciente
buscaPaciente = StringVar()
buscaPaciente = Entry(root, width=25)
buscaPaciente.place(x=300,y=272)
#boton Datos paciente
txt = StringVar()



imgD = Image.open('images/DatosP.png')
imgD = ImageTk.PhotoImage(imgD)
buscarD = Button(root, image=imgD, borderwidth=0, bg="#0026fe", command=lambda: [ mostrarDatos(listaEnlazada.buscarPorIterar(buscaPaciente.get()), buscaPaciente.get() ) ]  )
buscarD.place(x= 240, y= 346)

#boton estado paciente
img1 = Image.open('images/EstadoP.png')
img1 = ImageTk.PhotoImage(img1)
buscarE = Button(root, image=img1, borderwidth=0, bg="#0026fe",command=lambda:  [mostrarEstado(listaEnlazada.buscarMedicoPorRut(buscaPaciente.get()), listaEnlazada.buscarDiagnosticoPorRut(buscaPaciente.get()), listaEnlazada.buscarTratamientoPorRut(buscaPaciente.get()), listaEnlazada.buscarInfoPaciente(buscaPaciente.get()) ,buscaPaciente.get() ), ''' aqui va otra funcion '''  ])
#txt.set(listaTrauma.buscar(buscaPaciente.get() )), listaTest.imprimir()
buscarE.place(x= 400, y= 346)

#muestra datos del paciente
imgLim = Image.open("images/defLimpiar.png")
imgLim = ImageTk.PhotoImage(imgLim)
img_label = tk.Label(image = imgLim , bg="#B3B6B7")
img_label.Image = imgLim
img_label.place(x=600, y=200)



#boton Limpiar
imgL = Image.open('images/Limpiar.png')
imgL = ImageTk.PhotoImage(imgL)
limpiar = Button(root, image=imgL, borderwidth=0, bg="#0026fe", command =lambda: [bLimpiar()] ).place(x= 740, y= 435)



marcoT = LabelFrame(root, text = "Pacientes Ingresados",bd = 4 , width = 290 , height = 325, bg = "#EDF0F2")
marcoT.place(x=1100 , y = 175)
#estilo
style = ttk.Style()
style.configure('Treeview', background = "#C0EAF8",foreground = "black", fieldBackground = "#C0EAF8")
style.theme_use("default")
style.map('Treeview',background=[('selected','#DCA44C')])
#creacion de tabla
tablaTo = ttk.Treeview(root , columns=(0,1, 2), show='headings', height=12)
tablaTo.place(x=1120, y=200)
tablaTo.tag_configure('oddrow',background="#26C1F4")
tablaTo.tag_configure('evenrow',background="#C0EAF8")
tablaTo.heading(0, text = "N°")
tablaTo.heading(1, text = "Nombre")
tablaTo.heading(2, text = "Rut")
tablaTo.column(0, width = 10, minwidth =25)
tablaTo.column(1, width = 120)
tablaTo.column(2, width = 120)



#agregando elementos
index = 1
for i in range(0,listaEnlazada.contador()):

    if index % 2 == 0:
        tablaTo.insert(parent='', index=i, iid=i, values=(index,listaEnlazada[i].getNombre(), listaEnlazada[i].getRut()), tags = ('evenrow'))
        
    else:
        tablaTo.insert(parent='', index=i, iid=i, values=(index,listaEnlazada[i].getNombre(), listaEnlazada[i].getRut()), tags = ('oddrow'))
        
    index+=1

btnC = Button(root, text="i", borderwidth=0, bg="#0026fe", fg = "white",font=("Cascadia Code PL",10,'bold') ,width=2,height=1, command =lambda: [info(tablaTo)]  )
btnC.place(x = 1160, y=462)




display_logo('./images/logoucen.png',230,40)







root.mainloop()





