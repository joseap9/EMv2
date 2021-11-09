from tkinter import *
from tkinter import ttk
from tkinter import messagebox

listaMonedas = ['bitvoin',12132,1232131,123123,'bitvoin',12132,1232131,123123,'bitvoin',12132,1232131,123123,'bitvoin',12132,1232131,123123,'bitvoin',12132,1232131,123123]

def tabla():
    # =======================
    #marcoTodos = LabelFrame(popup, text="Pacientes Con Alta Medica", bd=4, width=290, height=318, bg="#EDF0F2")
    #marcoTodos.place(x=50, y=30)
    # estilo
    style = ttk.Style()
    style.configure('Treeview', background="#C0EAF8", foreground="black", fieldBackground="#C0EAF8")
    style.theme_use("default")
    style.map('Treeview', background=[('selected', '#DCA44C')])
    # creacion de tabla
    tablaTodos = ttk.Treeview(root, columns=(0, 1, 2,3,4), show='headings', height=12)
    tablaTodos.place(x=30, y=10)
    tablaTodos.tag_configure('oddrow', background="#26C1F4")
    tablaTodos.tag_configure('evenrow', background="#C0EAF8")
    tablaTodos.heading(0, text="N°")
    tablaTodos.heading(1, text="Nombre")
    tablaTodos.heading(2, text="valor")
    tablaTodos.heading(3, text="Precio Min 24h ")
    tablaTodos.heading(4, text="Precio Max 24h" )
    tablaTodos.column(0, width=10, minwidth=25)
    tablaTodos.column(1, width=120)
    tablaTodos.column(2, width=120)
    tablaTodos.column(3, width=120)
    tablaTodos.column(4, width=120)

    # agregando elementos
    tablaTodos.insert(parent='', index=1, iid=1,
                                  values=(1, listaMonedas[0] ,listaMonedas[1], listaMonedas[2], listaMonedas[3]),
                                  tags=('evenrow'))
    tablaTodos.insert(parent='', index=2, iid=2,
                      values=(2, listaMonedas[4], listaMonedas[5], listaMonedas[6], listaMonedas[7]),
                      tags=('oddrow'))
    tablaTodos.insert(parent='', index=3, iid=3,
                      values=(3, listaMonedas[8], listaMonedas[9], listaMonedas[10], listaMonedas[11]),
                      tags=('evenrow'))
    tablaTodos.insert(parent='', index=4, iid=4,
                      values=(4, listaMonedas[12], listaMonedas[13], listaMonedas[14], listaMonedas[15]),
                      tags=('oddrow'))
    tablaTodos.insert(parent='', index=5, iid=5,
                      values=(5, listaMonedas[16], listaMonedas[17], listaMonedas[18], listaMonedas[19]),
                      tags=('evenrow'))









root = Tk()
root.title("Scrapping Crypto")
root.geometry("600x500")
tabla()

root.mainloop()

