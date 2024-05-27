# FORMULARIOS CON EL WIDGET ENTRY() Y CONTRASEÑAS PROTEGIDAS

# importar tkinter y asignarle un alias "tk"
import tkinter as tk

# crear la ventana
root = tk.Tk()

# definir una funcion simple
def hola():
    saludo = tk.Label(root, text=F"Se envio {entrada_texto.get()} correctamente!", padx=50, pady=50).grid(column=0, row=1) # => se puede usar mostrar el contenido de la variable
#                                                                                                                          => para imprimirla usando un f string, y hacer dinamico el uso de .entry()



# crear un boton
boton = tk.Button(root, text="Enviar", bg="grey", fg="white", command=hola, padx=50, pady=50).grid(column=0, row=0)

# fg="x": sirve para cambiar el color del texto



# ENTRY(), ES COMO EL INPUTTEXT DE HTML, SE CREA COMO CUALQUIER OTRO WIDGET: nombre_variable = tk.Entry(root)
entrada_texto = tk.Entry(root, width=20, bg="grey", fg="white", show="*") # => A .Entry(root, x, y, z, ...), puede tener varios atributos como cualquier otro widget
entrada_texto.grid(column=0, row=2)                           # => se usa "show="*"", para "transformar" visiblemente los datos ingresados, con un caracter, en este caso "*"
                                                              #    sirve para no mostrar contraseñas por ejemplo





# Iniciar la ventana
root.mainloop()


