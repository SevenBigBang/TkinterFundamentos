# ANCLAJES(ANCHORS) EN TKINTER: SIRVEN PARA DEFINIR DONDE SE COLOCA EL TEXTO DE LOS WIDGETS 

import tkinter as tk

# crear la ventana
root = tk.Tk()



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
    tk.Radiobutton(root, text=opcion, value=valor, variable=colores).pack(anchor="nw") # => con .pack(anchor="x"), DEFINIMOS EN QUE POSICION QUEREMOS IMPRIMIR EL VALOR

enviar = tk.Button(root, text="Mostrar color", command=lambda : mostrar_color(colores.get())).pack()


# COMO SE PUEDE OBSERVAR EN EL FORMULARIO DE ARRIBA, SE VE QUE TODAS LAS OPCIONES SE DIBUJAN DE UNA FORMA NO MUY ESTETICA, DIGAMOS UNA FORMA DE ARCO:
# NO ESTA JUSTIFICADO NI A LA IZQUIERDA NI A LA DERECHA, PARA JUSTIFICAR ESTO EXISTEN 9 POSICIONES:

posicion_1 = tk.Label(root, text="Noroeste").pack(anchor="nw")
posicion_2 = tk.Label(root, text="Norte").pack(anchor="n")
posicion_3 = tk.Label(root, text="Noreste").pack(anchor="ne")
posicion_4 = tk.Label(root, text="Oeste").pack(anchor="w")
posicion_5 = tk.Label(root, text="Centro").pack(anchor="center")
posicion_6 = tk.Label(root, text="Este").pack(anchor="e")
posicion_7 = tk.Label(root, text="Sudoeste").pack(anchor="sw")
posicion_8 = tk.Label(root, text="sud").pack(anchor="s")
posicion_9 = tk.Label(root, text="Sudeste").pack(anchor="se")









root.mainloop()

