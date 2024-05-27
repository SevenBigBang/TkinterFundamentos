import tkinter as tk # Importamos tkinter y le ponemos un alias "tk"


# HASTA EL MOMENTO HEMOS VISTO UN METODO, QUE ES ".pack()", EL CUAL DEBEMOS USAR SI QUEREMOS MOSTRAR NUESTROS WIDGETS, FUNCIONA DE LA SIGUIENTE MANERA:

root = tk.Tk() # => creamos la ventana principal
etiqueta = tk.Label(root, text="Primer etiqueta") # => creamos una etiqueta de texto con una frase usando el metodo ".Label(x, y="z")"
etiqueta.pack() # => Mostramos nuestra etiqueta con nuestro texto

marco_principal = tk.Frame() # => Creamos nuestro marco
marco_principal.config(width="400", height="400") # => configuramos nuestro marco
marco_principal.config(bg="grey")
marco_principal.pack() # => Iniciamos nuestro marco

# DEPENDIENDO DONDE ESTABLEZCAMOS EL METODO PACK, SE MUESTRA EN LA PANTALLA 
etiqueta1 = tk.Label(root, text="Segunda etiqueta")
etiqueta1.pack() # => ESTA ETIQUETA SE MOSTRARA EN LA PARTE INFERIOR (ABAJO DEL MARCO GRIS)
# USANDO EL METODO PACK IMPORTA MUCHO COMO LOS ORDENES A DIFERENCIA DEL METODO GRID CON EL QUE PODEMOS ESTABLECER EN QUE FILA Y COLUMNA QUEREMOS MOSTRAR

root.mainloop() 





# AHORA EL METODO ".grid()"

root2 = tk.Tk() # => creamos la ventana secundaria

etiqueta3 = tk.Label(root2, text="tercer etiqueta") # => creamos una etiqueta de texto con una frase usando el metodo ".Label(x, y="z")"
etiqueta3.grid(row=0, column=0) # => Mostramos nuestra etiqueta con nuestro texto, con .grid(x=x, y=y)

marco_secundario = tk.Frame() # => Creamos nuestro marco
marco_secundario.config(width="400", height="400") # => configuramos nuestro marco
marco_secundario.config(bg="blue")
marco_secundario.grid(row=1, column=1) # => Iniciamos nuestro marco

etiqueta4 = tk.Label(root2, text="cuarta etiqueta")
etiqueta4.grid(row=2, column=2) # => ESTA ETIQUETA SE MOSTRARA EN DONDE LE ESPECIFIQUEMOS EN FILAS (ROWS) Y COLUMNAS (COLUMNS)

# USANDO EL METODO GRID IMPORTA MUCHO COMO DEFINAS LA POSICION DE CADA WIDGET, POR FILAS Y COLUMNAS

root2.mainloop() 