import tkinter as tk # Importamos tkinter y le ponemos un alias "tk"

# Ventana principal:
root = tk.Tk()  


etiqueta = tk.Label(root, text="Hola soy un texto")
etiqueta.pack() # => SIEMPRE QUE HACEMOS USO DE UN METODO O CREAMOS UN WIDGET TENEMOS QUE EMPAQUETAR LA VARIABLE

# WIDGETS: Sirven para crear Botones, Marcos, Etiquetas, etc...

# Widget 1. .Frame(): Sirve para crear un Marco, es un contenedor de otros widgets en la ventana principal "root" en la linea 4
# .Frame(); NO MODIFICA EL TAMAÑO DE LA VENTANA EN SI, SOLO AGREGA UN MARCO DE X TAMAÑO LO CUAL OBLIGA A LA VENTANA A ENGRANDECERSE 

marco_principal = tk.Frame() # => A UNA VARIABLE LE ASIGNAMOS EL METODO .Frame(), PARA CREAR EL MARCO
marco_principal_1 = tk.Frame()
# PERSONALIZACION DEL WIDGET; SE PUEDEN PERSONALIZAR MUCHO:

# TAMAÑO
marco_principal.config(width="400", height="300")
marco_principal.pack()
# CAMBIAR EL COLOR DE FONDO:
marco_principal.config(bg="grey")


marco_principal_1.config(bg="white")
marco_principal_1.pack()
marco_principal_1.config(width="400", height="300")

# SI EXISTEN DOS MARCOS LA VENTANA SE EXPANDIRA PARA QUE QUEPAN LOS DOS SIN NECESIDAD DE SOBRESCRIBIR UNO ENCIMA DEL OTRO.





root.mainloop() 


