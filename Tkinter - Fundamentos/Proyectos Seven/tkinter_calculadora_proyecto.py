# CREACION DE UNA CALCULADORA PARTE GRAFICA:

import tkinter as tk

# Creacion de ventana
root = tk.Tk()
# Titulo
root.title("Calculadora Seven")
# Icono de ventana
root.iconbitmap("Tkinter - Fundamentos/img/Calculator_30001.ico")

# SE USA PARA NO PERMITIR REDIMENCIONAR EL TAMAÑO DE LA VENTANA CON: ".resizable(x, y)": Acepta dos parametros donde x = 0, si queremos que no se pueda agrandar horizontalemnte la ventana
#                                                                                                                    y = 0, si queremos que no se pueda agrandar verticalmente la ventana
# DE LO CONTRARIO SI QUIERES QUE SE PUEDA AGRANDAR LA VENTANA DE UN LADO U OTRO CAMBIA EL 0 POR UN 1 (SOLO SON POSIBLES ESOS DOS VALORES)
root.resizable(0, 0) # => EN ESTE CASO USAMOS .RESIZABLE(0, 0), PORQUE QUEREMOS DEJAR LA VENTANA ESTATICA

# PARA MODIFICAR EL TAMAÑO PREDETERMINADO DE LA VENTANA USAMOS "geometry("x * y")": EN LOS PARAMETROS ENTRE COMILLAS DEBES PONER LOS PIXELES EN X POR LOS PIXELES EN Y (EL TAMAÑO DE LA VENTANA)
root.geometry("292x310")








# PARTE LOGICA:


# FUNCION PARA IMPRIMIR NUMEROS EN BASE A LOS BOTONES OPRIMIDOS:
def imprimir_num(valor):
    anterior = pantalla.get()
    pantalla.delete(0, tk.END)
    pantalla.insert(0, str(anterior) + str(valor))


# FUNCION SUMA:
def suma():
    global num1
    global operacion
    num1 = pantalla.get()
    num1 = float(num1)
    pantalla.delete(0, tk.END)
    operacion = "+"

# FUNCION RESTA:
def resta():
    global num1
    global operacion
    num1 = pantalla.get()
    num1 = float(num1)
    pantalla.delete(0, tk.END)
    operacion = "-"

# FUNCION MULTIPLICACION:
def multiplicacion():
    global num1
    global operacion
    num1 = pantalla.get()
    num1 = float(num1)
    pantalla.delete(0, tk.END)
    operacion = "*"

# FUNCION DIVISION:
def division():
    global num1
    global operacion
    num1 = pantalla.get()
    num1 = float(num1)
    pantalla.delete(0, tk.END)
    operacion = "/"


# FUNCION IGUAL:
def igual():
    try:
        global num2
        num2 = pantalla.get()
        pantalla.delete(0, tk.END)

        if operacion == "+":
            pantalla.insert(0, num1 + float(num2))
        elif operacion == "-":
            pantalla.insert(0, num1 - float(num2))
        elif operacion == "*":
            pantalla.insert(0, num1 * float(num2))
        elif operacion == "/":
            pantalla.insert(0, num1 / float(num2))
        elif operacion == "%":
            pantalla.insert(0, (num1 / 100) * float(num2))
    except NameError:
        pantalla.insert(0, "Error")

    
# FUNCION BORRAR TODOs:
def borrar_todo():
    pantalla.delete(0, tk.END)



# FUNCION BORRAR DE A UNO:
def borrar_uno(pantalla):
    pantalla.delete(len(pantalla.get()) -1)

# FUNCION BOTON PORCENTAJE:

def porcentaje():
    global num1
    global operacion
    num1 = pantalla.get()
    num1 = float(num1)
    pantalla.delete(0, tk.END)
    operacion = "%"


# FUNCION PARENTESIS

def imprimir_parentesis(valor):
    anterior = pantalla.get()
    















# PARTE GRAFICA:

# CREAR UNA MINIBARRA DONDE SE MUESTRANS LOS INPUTS Y TOTALES
pantalla = tk.Entry(root, 
                    width= 22, 
                    bg="grey", 
                    fg="white", 
                    borderwidth=0, 
                    font=('arial', 18, 'bold')
                    )


# FORMA EN DONDE SE VA A MOSTRAR NUESTRA MINIBARRA
pantalla.grid(row=0, 
              padx=2, # MARGEN EN X
              pady=2, # MARGEN EN Y
              columnspan=4 
              )

# BOTONES DEL 1 AL 9:
boton_1 = tk.Button(root, 
                    text="1", 
                    width=9, 
                    height=3, 
                    bg="white", 
                    borderwidth=0, 
                    cursor="hand2",
                    command=lambda : imprimir_num(1)
                    ).grid(row=2, column=0, padx=1, pady=1)

boton_2 = tk.Button(root, 
                    text="2", 
                    height=3, 
                    width=9, 
                    bg="white", 
                    borderwidth=0, 
                    cursor="hand2",
                    command=lambda : imprimir_num(2)
                    ).grid(row=2, column=1, padx=1, pady=1)

boton_3 = tk.Button(root, 
                    text="3", 
                    height=3, 
                    width=9, 
                    bg="white", 
                    borderwidth=0,
                    cursor="hand2",
                    command=lambda : imprimir_num(3)
                    ).grid(row=2, column=2, padx=1, pady=1)

boton_4 = tk.Button(root, 
                    text="4", 
                    height=3, 
                    width=9, 
                    bg="white", 
                    borderwidth=0,
                    cursor="hand2",
                    command=lambda : imprimir_num(4)
                    ).grid(row=3, column=0, padx=1, pady=1)

boton_5 = tk.Button(root, 
                    text="5", 
                    height=3,
                    width=9, 
                    bg="white", 
                    borderwidth=0,
                    cursor="hand2",
                    command=lambda : imprimir_num(5)
                    ).grid(row=3, column=1, padx=1, pady=1)

boton_6 = tk.Button(root, 
                    text="6", 
                    width=9,
                    height=3, 
                    bg="white", 
                    borderwidth=0,
                    cursor="hand2",
                    command=lambda : imprimir_num(6)
                    ).grid(row=3, column=2, padx=1, pady=1)

boton_7 = tk.Button(root,
                    text="7",
                    height=3,
                    width=9,
                    bg="white",
                    borderwidth=0,
                    cursor="hand2",
                    command=lambda : imprimir_num(7)
                    ).grid(row=4, column=0, padx=1, pady=1)

boton_8 = tk.Button(root,
                    text="8",
                    height=3,
                    width=9,
                    bg="white",
                    borderwidth=0,
                    cursor="hand2",
                    command=lambda : imprimir_num(8)
                    ).grid(row=4, column=1, padx=1, pady=1)

boton_9 = tk.Button(root, 
                    text="9",
                    height=3,
                    width=9,
                    bg="white",
                    borderwidth=0,
                    cursor="hand2",
                    command=lambda : imprimir_num(9)
                    ).grid(row=4, column=2, padx=1, pady=1)

boton_0 = tk.Button(root,
                    text="0",
                    height=3,
                    width=9,
                    bg="white",
                    borderwidth=0,
                    cursor="hand2",
                    command=lambda : imprimir_num(0)
                    ).grid(row=5, column=1, padx=1, pady=1)



# BOTONES DE OPERACIONES:

boton_mas = tk.Button(root, 
                      text="+",
                      height=3,
                      width=9,
                      bg="white",
                      borderwidth=0,
                      cursor="hand2",
                      command=suma
                      ).grid(row=1, column=3, padx=1, pady=1)

boton_menos = tk.Button(root, 
                        text="-",
                        height=3,
                        width=9,
                        bg="white",
                        borderwidth=0,
                        cursor="hand2",
                        command=resta
                        ).grid(row=2, column=3, padx=1, pady=1)

boton_multiplicacion = tk.Button(root, 
                                 text="*",
                                 height=3,
                                 width=9,
                                 bg="white",
                                 borderwidth=0,
                                 cursor="hand2",
                                 command=multiplicacion
                                 ).grid(row=3, column=3, padx=1, pady=1)

boton_division = tk.Button(root,
                           text="/",
                           height=3,
                           width=9,
                           bg="white",
                           borderwidth=0,
                           cursor="hand2",
                           command=division
                           ).grid(row=4, column=3, padx=1, pady=1)

boton_igual = tk.Button(root,
                        text="=",
                        height=3,
                        width=9,
                        bg="white",
                        borderwidth=0,
                        cursor="hand2",
                        command=igual
                        ).grid(row=5, column=3, padx=1, pady=1)


# BOTONES DE OPERACIONES ADICIONALES:

boton_borrartodo = tk.Button(root,
                             text="AC",
                             height=3,
                             width=9,
                             bg="white",
                             borderwidth=0,
                             cursor="hand2",
                             command=borrar_todo
                             ).grid(row=1, column=0, padx=1, pady=1)

boton_parentesis = tk.Button(root,
                             text="(  )",
                             height=3,
                             width=9,
                             bg="white",
                             borderwidth=0,
                             cursor="hand2",
                             command=lambda: imprimir_parentesis("(")
                             ).grid(row=1, column=1, padx=1, pady=1)

boton_porcentaje = tk.Button(root,
                             text="%",
                             height=3,
                             width=9,
                             bg="white",
                             borderwidth=0,
                             cursor="hand2",
                             command=porcentaje
                             ).grid(row=1, column=2, padx=1, pady=1)

boton_punto_decimal = tk.Button(root,
                                text=".",
                                height=3,
                                width=9,
                                bg="white",
                                borderwidth=0,
                                cursor="hand2",
                                command=lambda : imprimir_num(".")
                                ).grid(row=5, column=0, padx=1, pady=1)

boton_borrar = tk.Button(root,
                         text="C",
                         height=3,
                         width=9,
                         bg="white",
                         borderwidth=0,
                         cursor="hand2",
                         command=lambda : borrar_uno(pantalla)
                         ).grid(row=5, column=2, padx=1, pady=1)





root.mainloop()