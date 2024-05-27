# AÑADIR CODIGO A LAS OPCIONES DE MESSAGEBOx: EN ESTE CASO ESTAMOS USANDO ".askquestion(title="x", message="y")", Y ESTE NOS GENERA UN CUADRO DE DIALOGO CON DOS OPCIONES PREDETERMINADAS
#                                             SI O NO, PARA INTERACTUAR CON ELLOS PODEMOS PONER UN CONDICIONAL.

import tkinter as tk
from tkinter import messagebox as msg

root = tk.Tk()
root.title("Este es el titulo de la ventana principal")
root.iconbitmap("img/stackofphotos_pictures_5200.ico")

def mostrar_ventana():
    respuesta = msg.askquestion(title="Pregunta seria", message="¿Deberia dejar de programar y salir a la calle?")

    # PODEMOS PONER EL IF DENTRO DE LA FUNCION YA QUE ES LA QUE INVOCA EL CUADRO DE DIALOGO:
    if respuesta == "no":
        msg.showinfo(title="Eleccion correcta", message="Muy bien nunca hay que descansar :)")
    elif respuesta == "yes":
        reintentar = msg.askretrycancel(title="Eleccion incorrecta", message="Muy mal no vas a mejorar :c")
        if reintentar:
            msg.showerror(title="Noooo", message="NO APRENDERAS NUNCA >:/")
            
        else:
            msg.showinfo(title="Buena eleccion", message="Buena eleccion nunca es tarde para arrepentirse")

boton_1 = tk.Button(root, text="Enviar", command=mostrar_ventana, width=75).pack()



root.mainloop()