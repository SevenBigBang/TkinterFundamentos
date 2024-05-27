# El widget Checkbutton(): SON MUY PARECIDOS A LOS RADIO BUTTONS SOLO QUE ESTOS NOS PERMITEN ESCOGER ENTRE NINGUNA OPCION, UNA OPCION O MUCHAS OPCIONES

import tkinter as tk



root = tk.Tk()
root.title("Ventana principal")
root.geometry("250x200")





# PARA PODER RELACIONAR VARIOS CHECKBUTTONS NECESITAMOS UNA VARIABLE DE CONTROL:
variable_control1 = tk.StringVar()
variable_control2 = tk.StringVar()






# PARA CREAR UN CHECKBUTTON USAREMOS .Checkbutton()
opcion_1 = tk.Checkbutton(root, 
                          text="Opcion 1", 
                          variable=variable_control1,
                          onvalue="Opcion 1 seleccionada",    # => SE USA "onvalue", PARA ASIGNARLE UN VALOR AL CHEKCBUTTON CUANDO LO SELECCIONAN
                          offvalue="Opcion 1 no seleccionada" # => SE USA "offvalue", PARA ASIGNARLE UN VALOR AL CHECKBUTTON CUANDO NO LO SELECCIONAN
                          )
opcion_1.pack()
opcion_1.deselect() # => SE USA ".deselect()" PARA DEJAR DESMARCADA EL CHECKBUTTON POR DEFECTO

opcion_2 = tk.Checkbutton(root,
                          text="Opcion 2",
                          variable=variable_control2,
                          onvalue="Opcion 2 seleccionada",
                          offvalue="Opcion 2 no seleccionada")
opcion_2.pack()
opcion_2.deselect()  # => SE USA ".deselect()" PARA DEJAR DESMARCADA EL CHECKBUTTON POR DEFECTO






# FUNCION QUE ME DEVUELVA EL VALOR QUE NOS DE EL CHECK BUTTON
def seleccion():
    etiqueta1 = tk.Label(root, text=variable_control1.get()).pack() # CREAMOS UNA ETIQUETA QUE NOS MUESTRE EL VALOR POR DEFECTO AL SER O NO SER SELECCIONADO NUESTRO CHECKBUTTON
    etiqueta2 = tk.Label(root, text=variable_control2.get()).pack()






# AL FINAL CREAREMOS UN BOTON PARA ENVIAR EL VALOR DEL CHECKBUTON
ver_seleccion = tk.Button(root, text="Ver seleccion", command=seleccion).pack()



root.mainloop()