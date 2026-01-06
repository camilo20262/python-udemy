from tkinter import * 

#inicar tkinter

aplicacion= Tk()


#Tamaño de la ventana
aplicacion.geometry('1020x630+0+0')


# evitar maximizar 
aplicacion.resizable(False,False)


#titulo de la ventana 
aplicacion.title('Mi restaurante           Sistema de facturacion')



# evitar que la pantalla se cierre
aplicacion.mainloop()