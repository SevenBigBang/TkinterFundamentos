# FORMULARIOS CON EL WIDGET RADIOBUTTON() Y VARIABLES DE CONTROL



# importar tkinter y asignarle un alias "tk"
import tkinter as tk

# crear la ventana
root = tk.Tk()


# VARIABLES DE CONTROL: Objetos especiales para almacenar sus valores para poder trabar con los diferentes tipos de formularios

# .IntVar(): Para los enteros
# .DoubleVar(): Para los flotantes
# .StringVar(): Para los string
# .BooleanVar(): Para los booleanos




# => Las variables de control las usaremos para conectar varios widgets del mismo tipo (si tenemos varias opciones radio button, podremos relacionar las posibles opciones creando un grupo de widgets)

# Crear variables de control:
num = tk.IntVar() #=> Esta variable de control guarda el valor de la opcion que la este llamando, en este caso podria guardar el valor de "opcion_1" o "opcion_2".
num.set(value=1) # => Con esta linea de codigo, le establecemos un valor por defecto a nuestra variable de control. (Pero esto genera un problema, ya que el set siempre le dara ese valor "1", asi seleccionemos otro valor)
opcion_get = tk.Label(root, text=num.get()).grid(row=3) # => Esta linea de codigo la usamos para observar el valor que almacena nuestra variable de control con ".get()"
# PARA EVITAR ESTE ERROR QUE LA VARIABLE DE CONTROL SIEMPRE TENGA POR DEFECTO EL VALOR 1, NECESITAMOS CREAR UNA FUNCION:
def actualiza(value):
    opcion_get = tk.Label(root, text=value).grid(row=3)

titulo = tk.Label(root, text="Seleccione la respuesta correcta.").grid(row=0)






# Radio button genera opciones seleccionables 

opcion_1 = tk.Radiobutton(root, text="Esta es la primera opcion", value=1, variable=num, command=lambda : actualiza(num.get())).grid(row=1)# => .RadioButton(root, text="x", value=y, variable=z).grid(row=x, column=y)
# => "value=1": 1 es el valor que le asignamos a nuestra primera opcion y usamos la palabra reservada "variable=x", para hacer referencia a una variable de control.

opcion_2 = tk.Radiobutton(root, text="Esta es la primera opcion", value=2, variable=num, command=lambda : actualiza(num.get())).grid(row=2)
# Para incluir esta funcion creada tenemos que hacer uso de la palabra reservada "command=lambda : nombre_funcion(x)"

# LA FUNCION ACTUALIZA SE ENCARGA DE MOSTRAR UN LABEL() EL VALUE OBTENIDO EN EL GET DE LAS FUNCIONES LAMBDA PASADAS COMO EVENTO EN EL COMMAND DE LOS RADIOBUTTON()


root.mainloop()

