# CUADRO DE DIALOGO: ES UNA VENTANA CON INFORMACION EXTRA, PUEDE SER UN BOTON, UN ICONO, ALGUNA INFORMACION EXTRA ETC..

# PARA ACCEDER A ESTOS CUADROS DE DIALOGOS TENEMOS QUE IMPORTAR "messagebox"

# Importar tkinter como tk:
import tkinter as tk

# Importar messagebox como msg:
from tkinter import messagebox as msg
# .title: Se usa para poner un titulo 
# .iconbitmap: Se usa para poner una imagen (debe ser ".ico")

# Creacion de la ventana:
root = tk.Tk()

# Creacion del titulo de la ventana:
root.title("Este es el titulo de la ventana principal")

# Creacion del icono de la ventan:
root.iconbitmap("img/stackofphotos_pictures_5200.ico") # => Con esto ponemos un icono en la ventana diferente al predeterminado


# CREAR CUADRO DE DIALOGO: Una forma de hacerlo seria crear una funcion, que va a ser llamada en un eventO( pulsar un boton )
def mostrar_cuadro():
    msg.showinfo(title="En el primer paramatro es el titulo del cuadro", message="este segundo muestra el mensaje interior del cuadro de dialogo.")# usando .showinfo creamos un cuadro de texto de informacion
# ahora si usamos title="x", podremos especificar el titulo del cuadro de dialogo; y si usamos message="y", podremos especificar el mensaje de dicho cuadro de dialogo


# añadir un boton que desencadene el cuadro de dialogo
boton1 = tk.Button(root, text="Enviar",
                   command=mostrar_cuadro,
                   width=75
                   ).pack()





















# Iniciamos la ventana
root.mainloop()
