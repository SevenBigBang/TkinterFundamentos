import tkinter as tk # Importamos tkinter y le ponemos un alias "tk"

# Ventana principal:
root = tk.Tk()  # => Por convencion se utiliza "root" como nombre de variable de ventana


# Texo que aparezca en la ventana con metodo ".Label(root, text="")"
etiqueta = tk.Label(root, text="Hola soy un texto")

# Empaquetar etiqueta:
etiqueta.pack() # se utiliza .pack(), para poder mostrar widgets




root.mainloop() # => .mainloop(): es el bucle que hace que la ventana se refresque infinitas veces (obligatorio)


