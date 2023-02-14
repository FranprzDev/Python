from tkinter import *
# importa todos los modulos

#luego de esto inicializo el objeto de la ventana

ventana = Tk()

# imagen =  PhotoImage(file= laruta)

etiqueta = Label(ventana, 
                 text = "Holaa", 
                 font=('sans-serif', 50, 'bold',), 
                 fg="#334aab",
                 padx=50, pady=30)
#con el atributo image= imagen se puede poner una imagen...
# el label posee infinitos parametros para cambiar todo lo que es nuestra consola.

etiqueta.pack()

#etiqueta.place(x,y)
# se agrege x & y para situarlo.
# y (Eje Vertical) 
# x (Eje horizontal)
# cuenta en x así --> (Hacia el positivo)

#con esto lo hago aparecer
# se centra en el medio

ventana.mainloop()

# todo antes del mainloop y antes de la ventana