# Posiciones relativas y el widget button()

# POSICIONES RELATIVAS: AL USAR .grid(colum=x, row=y), SI PONEMOS UNA COLUMNA MUY ALEJADA DE LAS QUE EXISTEN POR EJEMPLO:
import tkinter as tk

root = tk.Tk()

nombre_programa = tk.Label(root, text="Posiciones relativas")
nombre_programa.grid(column=3, row=5) # AL NO EXISTIR MAS ELEMENTOS ENTONCES ESTE AUTOMATICAMENTE SE ACOMODA EN LA POSICION VACIA (0, 0)

root.mainloop()

# ESTO SON LAS POSICIONES RELATIVAS, NO SE CREARAN ESPACIOS PARA CUMPLIR CON LA POSICION REQUERIDA SINO QUE TKINTER PONDRA EL WIDGET DONDE DEBERIA IR AUTOMATICAMENTE









# WIDGET - BUTTON(): Sirve para crear un widget con funcionalidad de boton


ventana = tk.Tk()

color_1 = tk.Frame()
color_1.config(width="100", height="100")
color_1.config(bg="Orange")
color_1.grid(column=3, row=5)


# CREACION DEL WIDGET BUTTON
boton_1 = tk.Button(ventana, text="Soy un boton", bg="red", padx=20, pady=20).grid(row=1, column=2) # => CREAMOS LA VARIABLE QUE VA A GUARDAR UN BOTON Y USAMOES EL METODO ".Button(root, text="xyz")"
#                                                                            Tambien podemos anidar metodos como en este caso con ".grid()" (solo algunos widgets permiten esto)
#                                                                            Tambien el color de fondo
#                                                                            cuenta con diferentes medidas de tamaño con: pad(x o y), x: horizontal; u y: vertical


ventana.mainloop()