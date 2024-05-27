import tkinter as tk


# creacion de ventana

root = tk.Tk()


# Creacion de funcion
def imprimir_hola():
    hola = tk.Label(root, text="Hola!", bg="white").grid(column=0, row=0)


# Creacion de boton:
boton_1 = tk.Button(root, text="¿Hola?", bg="brown", padx=40, pady=20, command=imprimir_hola). grid(row=0, column=1) # => La funcion se agrega al boton usando el nuevo atributo
#                                                                                                                         "command=nombre_funcion"



root.mainloop()