from tkinter import *

# iniciar tkinter
aplicacion = Tk()

# Tamaño de la ventana
aplicacion.geometry('1020x630+0+0')

# evitar maximizar
aplicacion.resizable(False, False)

# título
aplicacion.title('Mi restaurante - Sistema de facturación')

# color de fondo
aplicacion.config(bg='burlywood')

# panel superior
panel_superior = Frame(aplicacion, bd=1, relief=FLAT, bg='burlywood')
panel_superior.pack(side=TOP)

etiqueta_titulo = Label(
    panel_superior,
    text='Sistema de Facturación',
    fg='azure4',
    font=('Dosis', 58),
    bg='burlywood',
    width=27
)
etiqueta_titulo.grid(row=0, column=0)

# panel izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

# panel costos
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT)
panel_costos.pack(side=BOTTOM)

# panel comidas
panel_comidas = LabelFrame(
    panel_izquierdo,
    text='Comida',
    font=('Dosis', 19, 'bold'),
    bd=1,
    relief=FLAT,
    fg='azure4'
)
panel_comidas.pack(side=LEFT)

# panel bebidas
panel_bebidas = LabelFrame(
    panel_izquierdo,
    text='Bebidas',
    font=('Dosis', 19, 'bold'),
    bd=1,
    relief=FLAT,
    fg='azure4'
)
panel_bebidas.pack(side=LEFT)

# panel postres
panel_postres = LabelFrame(
    panel_izquierdo,
    text='Postres',
    font=('Dosis', 19, 'bold'),
    bd=1,
    relief=FLAT,
    fg='azure4'
)
panel_postres.pack(side=LEFT)

# listas de productos
lista_comidas = ['pollo', 'cordero', 'salmon', 'merluza', 'kebab', 'pizza1', 'pizza2', 'pizza3']
lista_bebidas = ['agua', 'soda', 'jugo', 'cola', 'vino1', 'vino2', 'cerveza1', 'cerveza2']
lista_postres = ['helado', 'fruta', 'brownies', 'flan', 'mousse', 'pastel1', 'pastel2', 'pastel3']

# ---- COMIDAS ----
variable_comida = []

for i, comida in enumerate(lista_comidas):
    var = IntVar()
    variable_comida.append(var)
    Checkbutton(
        panel_comidas,
        text=comida.title(),
        font=('Dosis', 19, 'bold'),
        onvalue=1,
        offvalue=0,
        variable=var
    ).grid(row=i, column=0, sticky=W)

# ---- BEBIDAS ----
variable_bebida = []

for i, bebida in enumerate(lista_bebidas):
    var = IntVar()
    variable_bebida.append(var)
    Checkbutton(
        panel_bebidas,
        text=bebida.title(),
        font=('Dosis', 19, 'bold'),
        onvalue=1,
        offvalue=0,
        variable=var
    ).grid(row=i, column=0, sticky=W)

# ---- POSTRES ----
variable_postre = []

for i, postre in enumerate(lista_postres):
    var = IntVar()
    variable_postre.append(var)
    Checkbutton(
        panel_postres,
        text=postre.title(),
        font=('Dosis', 19, 'bold'),
        onvalue=1,
        offvalue=0,
        variable=var
    ).grid(row=i, column=0, sticky=W)

# evitar que la ventana se cierre
aplicacion.mainloop()
