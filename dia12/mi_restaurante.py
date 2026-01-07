from tkinter import *
import random
import datetime

# ================== CONFIGURACIÓN PRINCIPAL ==================
aplicacion = Tk()
aplicacion.geometry('1020x630+0+0')
aplicacion.resizable(False, False)
aplicacion.title('Mi Restaurante - Sistema de Facturación')
aplicacion.config(bg='burlywood')

# ================== PANEL SUPERIOR ==================
panel_superior = Frame(aplicacion, bg='burlywood')
panel_superior.pack(side=TOP)

Label(
    panel_superior,
    text='Sistema de Facturación',
    font=('Dosis', 58),
    fg='azure4',
    bg='burlywood',
    width=27
).grid(row=0, column=0)

# ================== PANEL IZQUIERDO ==================
panel_izquierdo = Frame(aplicacion)
panel_izquierdo.pack(side=LEFT)

panel_comidas = LabelFrame(panel_izquierdo, text='Comida', font=('Dosis', 19, 'bold'))
panel_comidas.pack(side=LEFT)

panel_bebidas = LabelFrame(panel_izquierdo, text='Bebidas', font=('Dosis', 19, 'bold'))
panel_bebidas.pack(side=LEFT)

panel_postres = LabelFrame(panel_izquierdo, text='Postres', font=('Dosis', 19, 'bold'))
panel_postres.pack(side=LEFT)

# ================== LISTAS Y PRECIOS ==================
lista_comidas = ['Pollo', 'Cordero', 'Salmón', 'Merluza', 'Kebab', 'Pizza1', 'Pizza2', 'Pizza3']
lista_bebidas = ['Agua', 'Soda', 'Jugo', 'Cola', 'Vino1', 'Vino2', 'Cerveza1', 'Cerveza2']
lista_postres = ['Helado', 'Fruta', 'Brownies', 'Flan', 'Mousse', 'Pastel1', 'Pastel2', 'Pastel3']

precios_comida = [15, 18, 20, 17, 16, 14, 14, 14]
precios_bebida = [4, 5, 6, 6, 12, 12, 8, 8]
precios_postre = [6, 5, 7, 6, 7, 6, 6, 6]

# ================== FUNCIÓN GENÉRICA ==================
def crear_items(panel, lista):
    variables, textos, entradas = [], [], []

    def activar(i):
        if variables[i].get():
            entradas[i].config(state=NORMAL)
            textos[i].set('1')
        else:
            entradas[i].config(state=DISABLED)
            textos[i].set('0')

    for i, item in enumerate(lista):
        var = IntVar()
        variables.append(var)

        Checkbutton(
            panel, text=item, font=('Dosis', 18),
            variable=var, command=lambda i=i: activar(i)
        ).grid(row=i, column=0, sticky=W)

        texto = StringVar(value='0')
        textos.append(texto)

        entrada = Entry(panel, width=6, state=DISABLED, textvariable=texto)
        entrada.grid(row=i, column=1)
        entradas.append(entrada)

    return variables, textos, entradas

# ================== CREAR PRODUCTOS ==================
variable_comida, texto_comida, cuadros_comida = crear_items(panel_comidas, lista_comidas)
variable_bebida, texto_bebida, cuadros_bebida = crear_items(panel_bebidas, lista_bebidas)
variable_postre, texto_postre, cuadros_postre = crear_items(panel_postres, lista_postres)

# ================== PANEL COSTOS ==================
panel_costos = Frame(aplicacion)
panel_costos.pack(side=BOTTOM)

costo_comida = StringVar(value='0')
costo_bebida = StringVar(value='0')
costo_postre = StringVar(value='0')
subtotal = StringVar(value='0')
impuestos = StringVar(value='0')
total = StringVar(value='0')

Label(panel_costos, text='Costo Comida').grid(row=0, column=0)
Entry(panel_costos, textvariable=costo_comida, state='readonly').grid(row=0, column=1)

Label(panel_costos, text='Costo Bebida').grid(row=1, column=0)
Entry(panel_costos, textvariable=costo_bebida, state='readonly').grid(row=1, column=1)

Label(panel_costos, text='Costo Postres').grid(row=2, column=0)
Entry(panel_costos, textvariable=costo_postre, state='readonly').grid(row=2, column=1)

Label(panel_costos, text='Subtotal').grid(row=0, column=2)
Entry(panel_costos, textvariable=subtotal, state='readonly').grid(row=0, column=3)

Label(panel_costos, text='Impuestos (19%)').grid(row=1, column=2)
Entry(panel_costos, textvariable=impuestos, state='readonly').grid(row=1, column=3)

Label(panel_costos, text='Total').grid(row=2, column=2)
Entry(panel_costos, textvariable=total, state='readonly').grid(row=2, column=3)

# ================== RECIBO ==================
panel_recibo = Frame(aplicacion)
panel_recibo.pack(side=RIGHT)

texto_recibo = Text(panel_recibo, width=40, height=20)
texto_recibo.pack()

# ================== FUNCIONES ==================
def calcular_total():
    tc = sum(int(texto_comida[i].get()) * precios_comida[i] for i in range(len(texto_comida)))
    tb = sum(int(texto_bebida[i].get()) * precios_bebida[i] for i in range(len(texto_bebida)))
    tp = sum(int(texto_postre[i].get()) * precios_postre[i] for i in range(len(texto_postre)))

    costo_comida.set(tc)
    costo_bebida.set(tb)
    costo_postre.set(tp)

    sub = tc + tb + tp
    subtotal.set(sub)

    iva = sub * 0.19
    impuestos.set(f'{iva:.2f}')
    total.set(f'{sub + iva:.2f}')

def generar_recibo():
    texto_recibo.delete(1.0, END)
    factura = random.randint(1000, 9999)
    fecha = datetime.datetime.now().strftime('%d/%m/%Y %H:%M')

    texto_recibo.insert(END, f'Factura #{factura}\n{fecha}\n')
    texto_recibo.insert(END, '-'*30 + '\n')

    for i in range(len(lista_comidas)):
        if int(texto_comida[i].get()) > 0:
            texto_recibo.insert(END, f'{lista_comidas[i]} x{texto_comida[i].get()}\n')

    for i in range(len(lista_bebidas)):
        if int(texto_bebida[i].get()) > 0:
            texto_recibo.insert(END, f'{lista_bebidas[i]} x{texto_bebida[i].get()}\n')

    for i in range(len(lista_postres)):
        if int(texto_postre[i].get()) > 0:
            texto_recibo.insert(END, f'{lista_postres[i]} x{texto_postre[i].get()}\n')

    texto_recibo.insert(END, '-'*30 + f'\nTOTAL: ${total.get()}')

def guardar_recibo():
    with open('recibo.txt', 'w') as f:
        f.write(texto_recibo.get(1.0, END))

def resetear():
    for lista in [texto_comida, texto_bebida, texto_postre]:
        for t in lista:
            t.set('0')

    for lista in [cuadros_comida, cuadros_bebida, cuadros_postre]:
        for e in lista:
            e.config(state=DISABLED)

    for v in variable_comida + variable_bebida + variable_postre:
        v.set(0)

    for var in [costo_comida, costo_bebida, costo_postre, subtotal, impuestos, total]:
        var.set('0')

    texto_recibo.delete(1.0, END)

# ================== BOTONES ==================
panel_botones = Frame(aplicacion)
panel_botones.pack(side=BOTTOM)

Button(panel_botones, text='Total', width=10, command=calcular_total).grid(row=0, column=0)
Button(panel_botones, text='Recibo', width=10, command=generar_recibo).grid(row=0, column=1)
Button(panel_botones, text='Guardar', width=10, command=guardar_recibo).grid(row=0, column=2)
Button(panel_botones, text='Resetear', width=10, command=resetear).grid(row=0, column=3)

# ================== LOOP ==================
aplicacion.mainloop()
