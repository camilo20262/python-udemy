from sqlite3 import SQLITE_DBCONFIG_ENABLE_QPSG
from tkinter import * 

#inicar tkinter

aplicacion= Tk()


#Tamaño de la ventana
aplicacion.geometry('1020x630+0+0')


# evitar maximizar 
aplicacion.resizable(False,False)


#titulo de la ventana 
aplicacion.title('Mi restaurante           Sistema de facturacion')


#color de fondo de la ventana

aplicacion.config(bg='burlywood')


#panel superior 
panel_superior =Frame(aplicacion, bd =1, relief=FLAT)
panel_superior.pack(side=TOP)

#etiqueta titulo
etiqueta_titulo= Label(panel_superior,text='Sistema de Facturacion', fg='azure4',
                       font=('Dosis',58),bg='burlywood',width=27)

etiqueta_titulo.grid(row=0,column=0)


#panel izquierdo
panel_izquierdo= Frame(aplicacion, bd =1, relief=FLAT)
panel_izquierdo.pack(side=  LEFT)


#panel costos 
panel_costos=Frame(panel_izquierdo,bd=1, relief=FLAT)
panel_costos.pack(side=  BOTTOM)

#panel comidas

panel_comidas= LabelFrame(panel_izquierdo,text='Comida',font=('Dosis',19,'bold'),
                          bd=1,relief=FLAT,fg='azure4')

panel_comidas.pack(side=LEFT)


#panel bebidas
panel_bebidas= LabelFrame(panel_izquierdo,text='Bebidas',font=('Dosis',19,'bold'),
                          bd=1,relief=FLAT,fg='azure4')

panel_bebidas.pack(side=LEFT)



#panel postres
panel_postres= LabelFrame(panel_izquierdo,text='Postres',font=('Dosis',19,'bold'),
                          bd=1,relief=FLAT,fg='azure4')

panel_postres.pack(side=LEFT)

#panel derecha 
panel_derecha= Frame(aplicacion,bd=1,relief=FLAT)
panel_derecha.pack(side=RIGHT)

#panel_recibo=
panel_recibo= Frame(aplicacion,bd=1,relief=FLAT,bg='burlywood')
panel_recibo.pack()

#panel_calculadora=
panel_calculadora= Frame(aplicacion,bd=1,relief=FLAT,bg='burlywood')
panel_calculadora.pack()

#panel_botones=
panel_botones= Frame(aplicacion,bd=1,relief=FLAT,bg='burlywood')
panel_botones.pack()




# evitar que la pantalla se cierre
aplicacion.mainloop()