# BUCLE FOR AUTOGENERADOR DE RADIOBUTTONS


# importar tkinter y asignarle un alias "tk"
import tkinter as tk

# crear la ventana
root = tk.Tk()


# # Crear variables de control:
# num = tk.IntVar() 
# num.set(value=1) 
# opcion_get = tk.Label(root, text=num.get()).grid(row=3) 
# def actualiza(value):
#     opcion_get = tk.Label(root, text=value).grid(row=3)

# titulo = tk.Label(root, text="Seleccione la respuesta correcta.").grid(row=0)










# # BOTON DE ENVIO: Primero hay que quitar las funciones lambda de nuestro radio button ya que estas son las que envian el valor automaticamente a nuestra
# #                 variables de control en este caso "num = tk.IntVar()", es nuestra variable de control

# opcion_1 = tk.Radiobutton(root, text="Esta es la primera opcion", value=1, variable=num).grid(row=1)

# opcion_2 = tk.Radiobutton(root, text="Esta es la primera opcion", value=2, variable=num).grid(row=2)

# boton_envia = tk.Button(root, text="Enviar", command=lambda : actualiza(num.get())).grid(row=4)
# # Creamos la variable que almacena el boton, usamos .Button(root, text="x", command=lambda : nombre_fun(x))
# #                                                                           tenemos que usar command para llamar a la funcion creada y asi cada vez que se oprima el boton mostraremos el valor de nuestra variable de control





# FORMULARIOS CON EL WIDGET RADIOBUTTON() Y VARIABLES DE CONTROL: IMAGINEMOS QUE TENEMOS QUE CREAR 40 OPCIONES DE RADIO BUTON CADA OPCION CON DIFERENTES VALORES, 
# LO PODEMOS HACER COMO LA PRIMERA FORMA QUE SERIA LA DE ARRIBA LINEA 32, OPCION POR OPCION HASTA LA 40 O CREAR UN BUCLE FOR, QUE LOS CREE:

#CREACION DE LA FUNCION PARA MOSTRAR COLORES AL PRECIONAR EL BOTON:
def mostrar_color(value):
    opcion_get = tk.Label(root, text=value).pack()

# CREACION DE LISTA DE OPCIONES: 
opciones = [["Color Rojo", "Rojo"],
            ["Color Azul", "Azul"],
            ["Color Verde", "Verde"],
            ["Color Amarillo", "Amarillo"]
            ]

colores = tk.StringVar()
colores.set("Rojo")

# BUCLE FOR
for opcion, valor in opciones:
    tk.Radiobutton(root, text=opcion, value=valor, variable=colores).pack()

enviar = tk.Button(root, text="Mostrar color", command=lambda : mostrar_color(colores.get())).pack()









root.mainloop()





























