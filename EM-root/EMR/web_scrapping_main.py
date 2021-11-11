from bs4 import BeautifulSoup
import requests
import  pandas as pd
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pandas_datareader as pdr
from datetime import datetime, timedelta
import mplfinance as mpf

url = 'https://coinmarketcap.com/es/'
page = requests.get(url)
cont = page.text

listaMonedas = []

soup = BeautifulSoup(cont, 'lxml')

box = soup.find('html' , lang = 'es')

tex = box.find('h1', class_ = 'sc-1q9q90x-0 TyVlS')
titulo= tex.get_text()

#priemr a moneda
lista_paginas = ['https://coinmarketcap.com/es/currencies/bitcoin/',
 'https://coinmarketcap.com/es/currencies/ethereum/',
 'https://coinmarketcap.com/es/currencies/binance-coin/',
'https://coinmarketcap.com/es/currencies/cardano/',
'https://coinmarketcap.com/es/currencies/tether/' ]

for x in range(5):

    url=lista_paginas[x]

    page1 = requests.get(url)
    cont1 = page1.text

    soup2 = BeautifulSoup(cont1, 'lxml')

    v = soup2.find('div' , class_= 'sc-16r8icm-0 kjciSH priceSection')
    moneda = soup2.find('small', class_='nameSymbol').get_text()
    valor = v.find('div' , class_ = 'sc-16r8icm-0 kjciSH priceTitle').get_text()
    minimo = v.find('span' , class_ = 'n78udj-5 dBJPYV').get_text()
    x = soup2.find('div' , class_= 'sc-16r8icm-0 SjVBR')
    maximo = x.find('span' , class_ = 'n78udj-5 dBJPYV').get_text()
    a = soup2.find('div', class_='sc-16r8icm-0 fggtJu statsSection')
    con = 0

    # obtencion del volumen capital de la moneda

    for volu in a.findAll('div', class_='statsBlock'):
        if con == 2:
            for q in volu:
                if con == 3:
                    volumen = q.find('div', class_='statsValue').get_text()
                    print('voulumen de moneda: ' +str(volumen))
                con = con+1
        con= con+1


    tex2 = soup2.find('h2', class_='sc-1q9q90x-0 jCInrl h1')
    titulo2 = tex2.get_text()

    # grafico de velas
    # int_date = datetime.now() - timedelta(days=30)
    # info = pdr.get_data_yahoo(moneda + '-USD', start=int_date)
    # mpf.plot(info, type='candle', title='valor '+ titulo2, style='charles')
    listaMonedas.append(titulo2)
    listaMonedas.append(valor)
    listaMonedas.append(minimo)
    listaMonedas.append(maximo)

def graficoBitcoin():
    # procedimiento de scrapping solo para bitcoin
    url = 'https://coinmarketcap.com/es/currencies/bitcoin/'
    page1 = requests.get(url)
    cont1 = page1.text
    soup2 = BeautifulSoup(cont1, 'lxml')
    moneda = soup2.find('small', class_='nameSymbol').get_text()

    # grafico de Velas
    int_date = datetime.now() - timedelta(days=30)
    info = pdr.get_data_yahoo(moneda + '-USD', start=int_date)
    mpf.plot(info, type='candle', title='valor ' + 'Bitcoin', style='charles')


def graficoEtherium():
    # procedimiento de scrapping solo para etherium
    url = 'https://coinmarketcap.com/es/currencies/ethereum/'
    page1 = requests.get(url)
    cont1 = page1.text
    soup2 = BeautifulSoup(cont1, 'lxml')
    moneda = soup2.find('small', class_='nameSymbol').get_text()

    # grafico de Velas
    int_date = datetime.now() - timedelta(days=30)
    info = pdr.get_data_yahoo(moneda + '-USD', start=int_date)
    mpf.plot(info, type='candle', title='valor ' + 'Etherium', style='charles')

def graficoBinance():
    # procedimiento de scrapping solo para binance
    url = 'https://coinmarketcap.com/es/currencies/binance-coin/'
    page1 = requests.get(url)
    cont1 = page1.text
    soup2 = BeautifulSoup(cont1, 'lxml')
    moneda = soup2.find('small', class_='nameSymbol').get_text()

    # grafico de Velas
    int_date = datetime.now() - timedelta(days=30)
    info = pdr.get_data_yahoo(moneda + '-USD', start=int_date)
    mpf.plot(info, type='candle', title='valor ' + 'Binance', style='charles')

def graficoCardano():
    # procedimiento de scrapping solo para cardano
    url = 'https://coinmarketcap.com/es/currencies/cardano/'
    page1 = requests.get(url)
    cont1 = page1.text
    soup2 = BeautifulSoup(cont1, 'lxml')
    moneda = soup2.find('small', class_='nameSymbol').get_text()

    # grafico de Velas
    int_date = datetime.now() - timedelta(days=30)
    info = pdr.get_data_yahoo(moneda + '-USD', start=int_date)
    mpf.plot(info, type='candle', title='valor ' + 'Cardano', style='charles')

def graficotether():
    # procedimiento de scrapping solo para tether
    url = 'https://coinmarketcap.com/es/currencies/tether/'
    page1 = requests.get(url)
    cont1 = page1.text
    soup2 = BeautifulSoup(cont1, 'lxml')
    moneda = soup2.find('small', class_='nameSymbol').get_text()

    # grafico de Velas
    int_date = datetime.now() - timedelta(days=30)
    info = pdr.get_data_yahoo(moneda + '-USD', start=int_date)
    mpf.plot(info, type='candle', title='valor ' + 'Tether', style='charles')

def tabla():

    def item_selected(e):

        for selected_item in tablaTodos.selection():
            # dictionary
            item = tablaTodos.item(selected_item)
            # list
            valor = item['values'][0]

            nombreOpcion = item['text']
            imagen = item['image']
            abierto = item['open']

            if valor == 1:
                graficoBitcoin()
            elif valor == 2:
                graficoEtherium()
            elif valor == 3:
                graficoBinance()
            elif valor == 4:
                graficoCardano()
            else:
                graficotether()


    # =======================
    #marcoTodos = LabelFrame(popup, text="Pacientes Con Alta Medica", bd=4, width=290, height=318, bg="#EDF0F2")
    #marcoTodos.place(x=50, y=30)
    # estilo
    style = ttk.Style()
    style.configure('Treeview', background="#C0EAF8", foreground="black", fieldBackground="#C0EAF8")
    style.theme_use("default")
    style.map('Treeview', background=[('selected', '#DCA44C')])
    # creacion de tabla
    tablaTodos = ttk.Treeview(root, columns=(0, 1, 2,3,4), show='headings', height=14)
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

    tablaTodos.bind('<Double-1>', item_selected)









root = Tk()
root.title("Scrapping Crypto")
root.geometry("600x500")
tabla()




root.mainloop()
