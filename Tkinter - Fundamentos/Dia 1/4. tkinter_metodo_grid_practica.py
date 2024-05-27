# CONSTRUIR LA BANDERA DE COLOMBIA USANDO EL METODO GRID

# importar la libreria tkinter
import tkinter as tk


# creacion de la ventana 
root = tk.Tk()

# titulo de la ventana
nombre_bandera = tk.Label(root, text="BANDERA DE COLOMBIA")
nombre_bandera.grid(column=0, row=0)

# Creacion del primer color
color_1 = tk.Frame()
# configuracion del primer color
color_1.config(width="1000", height="300")
color_1.config(bg="yellow")
# Iniciamos nuestro color en la posicion indicada
color_1.grid(column=0, row=1,  sticky="nsew")


# Creacion del segundo color
color_2 = tk.Frame()
color_2.config(width="1000", height="100")
color_2.config(bg="blue")
color_2.grid(column=0, row=2, sticky="nsew")


# Creacion del tercer color
color_3 = tk.Frame()
color_3.config(width="1000", height="150")
color_3.config(bg="red")
color_3.grid(column=0, row=3,  sticky="nsew")


# Creacion de baston que sostiene la bandera
baston = tk.Frame()
baston.config(width="20", height="600")
baston.config(bg="brown")
baston.grid(column=1, row=1, rowspan=4, sticky="ns")


root.mainloop()