# TOPLEVEL(): SE USA PARA CREAR VENTANAS CON SUS PROPIAS PROPIEDADES, COMO UNA SEGUNDA ROOT


import tkinter as tk

root = tk.Tk()
root.title("Ventana principal")
root.geometry("300x400")


# CREAR NUEVA VENTANA (PODEMOS CREAR TANTAS COMO QUERAMOS Y SON TODAS MODIFICABLES)
ventana_nueva = tk.Toplevel() # SI NO LE PONEMOS EL ATRIBUTO .title, TOMARA EL TITULO DE LA PRIMER VENTANA, SE PUEDE CERRAR LA VENTANA HIJA Y LA PADRE NO SE CERRARA PERO VICEBERSA NO FUNCIONARA
# PROPIEDADES DE NUEVA VENTANA:
ventana_nueva.title("Ventana secundaria")
ventana_nueva.geometry("300x200")



# PARA HACER QUE LA VENTANA NUEVA SE CREE APARTIR DE CUANDO SE OPRIME EL BOTON ENVIA TENEMOS QUE METER VENTANA_NUEVA EN UNA FUNCION
def envia_boton():
    ventana_en_funcion = tk.Toplevel()
    ventana_en_funcion.title("Ventana en funcion")
    ventana_en_funcion.geometry("300x200")
    valor_entrada = entrada.get()
    etiqueta = tk.Label(ventana_en_funcion, text="El valor introducido en la ventana principal es: " + valor_entrada).grid(row=0)
    cerrar_ventana_funcion = tk.Button(ventana_en_funcion, text="Cerrar", command=ventana_en_funcion.destroy).grid(row=1) # => PONEMOS ESTA LINEA PARA BORRAR LA NUEVA VENTANA
                                                                                                                          #    Y ASI SE NOS FACILITE EL MANEJO DE LA MISMA


# COMUNICACION ENTRE DOS VENTANAS:
entrada = tk.Entry(root, width=20)
entrada.grid(row=0)
envia = tk.Button(root, text="Enviar", command=envia_boton).grid(row=1) # => CON COMMANDO=ENVIA_BOTON, LLAMAMOS A LA FUNCION PREVIAMENTE CREADA, LA CUAL CREARA UNA NUEVA VENTANA

cerrar_ventana_principal = tk.Button(root, text="Cerrar ventana principal", command=root.destroy).grid(row=2) # => CON ESTA LINEA CREAMOS UN BOTON PARA CERRAR LA VENTANA PRINCIPAL


# USANDO .destroy PODREMOS ELIMINAR VENTANAS :)



root.mainloop()