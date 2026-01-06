from tkinter import *

# iniciar tkinter
aplicacion = Tk()
aplicacion.geometry('1020x630+0+0')
aplicacion.resizable(False, False)
aplicacion.title('Mi restaurante - Sistema de facturación')
aplicacion.config(bg='burlywood')

# panel superior
panel_superior = Frame(aplicacion, bd=1, relief=FLAT, bg='burlywood')
panel_superior.pack(side=TOP)

Label(
    panel_superior,
    text='Sistema de Facturación',
    fg='azure4',
    font=('Dosis', 58),
    bg='burlywood',
    width=27
).grid(row=0, column=0)

# panel izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

# panel comidas
panel_comidas = LabelFrame(panel_izquierdo, text='Comida',
                           font=('Dosis', 19, 'bold'), fg='azure4')
panel_comidas.pack(side=LEFT)

# panel bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text='Bebidas',
                           font=('Dosis', 19, 'bold'), fg='azure4')
panel_bebidas.pack(side=LEFT)

# panel postres
panel_postres = LabelFrame(panel_izquierdo, text='Postres',
                           font=('Dosis', 19, 'bold'), fg='azure4')
panel_postres.pack(side=LEFT)

# listas
lista_comidas = ['pollo', 'cordero', 'salmon', 'merluza', 'kebab', 'pizza1', 'pizza2', 'pizza3']
lista_bebidas = ['agua', 'soda', 'jugo', 'cola', 'vino1', 'vino2', 'cerveza1', 'cerveza2']
lista_postres = ['helado', 'fruta', 'brownies', 'flan', 'mousse', 'pastel1', 'pastel2', 'pastel3']

# ================= FUNCION GENERICA =================
def crear_items(panel, lista):
    variables = []
    textos = []
    entradas = []

    def activar(index):
        if variables[index].get() == 1:
            entradas[index].config(state=NORMAL)
            textos[index].set('1')
        else:
            entradas[index].config(state=DISABLED)
            textos[index].set('0')

    for i, item in enumerate(lista):
        var = IntVar()
        variables.append(var)

        Checkbutton(
            panel,
            text=item.title(),
            font=('Dosis', 19, 'bold'),
            variable=var,
            onvalue=1,
            offvalue=0,
            command=lambda i=i: activar(i)
        ).grid(row=i, column=0, sticky=W)

        texto = StringVar(value='0')
        textos.append(texto)

        entrada = Entry(
            panel,
            font=('Dosis', 18, 'bold'),
            width=6,
            state=DISABLED,
            textvariable=texto
        )
        entrada.grid(row=i, column=1)
        entradas.append(entrada)

    return variables, textos, entradas

# ================= CREAR TODO =================
variable_comida, texto_comida, cuadros_comida = crear_items(panel_comidas, lista_comidas)
variable_bebida, texto_bebida, cuadros_bebida = crear_items(panel_bebidas, lista_bebidas)
variable_postre, texto_postre, cuadros_postre = crear_items(panel_postres, lista_postres)

aplicacion.mainloop()
