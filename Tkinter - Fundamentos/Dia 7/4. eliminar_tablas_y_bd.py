# ELIMINAR Tablas y Bases de datos escribiendo el nombre: 

# INSERTAR datos en TABLAS USANDO TKINTER DE FORMA INTERACTIVA: 


# Crear TABLAS en BASES DE DATOS con MariaDB EN PYTHON:


import mysql.connector
import sys
import tkinter as tk

root = tk.Tk()
root.title("Ventana principal")
root.geometry("300x200")

# CONEXION A LA BASE DE DATOS USANDO MYSQL - CONNECTOR INSTALALO CON "pip install mysql"
try:
    conexion = mysql.connector.connect(
        user="root",
        password="", 
        host="127.0.0.1",
        port=3306,
        database="prueba"
    )
    cursor = conexion.cursor() # => .cursor(x), nos sirve para trabajar con la base de datos:


except mysql.connector.Error as error:
    print(f"Error al conectar con la base de datos: {error}")
    sys.exit(1)



# CREAR FUNCION QUE CREA TABLAS EN LA BASE DE DATOS CON UN BLOQUE TRY EXCEPT:
def crea_tabla():
    try:
        cursor.execute('''
                       CREATE TABLE clientes (id INT NOT NULL AUTO_INCREMENT,
                       nombre VARCHAR(32) NOT NULL,
                       apellidos VARCHAR(64) NOT NULL,
                       telefono VARCHAR(9) NOT NULL,
                       direccion VARCHAR(256),
                       PRIMARY KEY(id))
                       ''') # => USANDO .execute("xyz"), LE MANDAMOS UNA INSTRUCCION DIRECTA A NUESTRA BASE DE DATOS

# AHORA NECESITAMOS HACER UN TIPO COMMIT PARA GUARDAR LOS CAMBIOS HECHOS EN LA BASE DE DATOS EN ESTE CASO EL CURSOR.EXECUTE()
        conexion.commit()

    # AHORA PONEMOS EL EXCEPT:
    except conexion.Error as error_tabla:
        print(f"Error al crear la tabla: {error_tabla}")




# BOTON PARA CREAR LA TABLA MEIDNATE LA FUNCION:
boton = tk.Button(root, text="Crear tabla", width=20, command=crea_tabla) # => AL OPRIMIR EL BOTON EL COMANDO ACTIVA LA FUNCION PREVIAMENTE CREADA EN LA LINEA 31
boton.place(x=25, y=10)


# FUNCION PARA ELIMINAR TABLAS Y BASES DE DATOS:
def eliminar_tabla():
    tabla = entrada_tabla.get()
    try:
        cursor.execute(f"DROP TABLE {tabla}")
        cursor.commit()
    except conexion.Error as error_tabla:
        print(f"Error al eliminar la tabla: {error_tabla}")

def eliminar_bd():
    bd = entrada_bd.get()
    try:
        cursor.execute(f"DROP DATABASE {bd}")
        cursor.commit()
    except conexion.Error as error_bd:
        print(f"Error al eliminar la base de datos: {error_bd}")
        



# INTERFAZ GRAFICA:

tk.Label(root,
         text="Eliminar tablas y bases de datos",
         font="calibri 18",
         fg="red"
         ).grid(row=0, columnspan=2)

tk.Label(root,
         text="Tabla").grid(row=1, column=0, pady=10)

entrada_tabla = tk.Entry(root)
entrada_tabla.grid(row=1, column=1, pady=10)


tk.Label(root,
         text="Base de datos").grid(row=2, column=0, pady=10)

entrada_bd = tk.Entry(root)
entrada_bd.grid(row=2, column=1, pady=10)


borrar_tabla = tk.Button(root,
                         text="Eliminar tabla",
                         bg="red2",
                         fg="white",
                         command=eliminar_tabla
                         ).grid(row=5, column=0)

borrar_bd = tk.Button(root,
                      text="Borrar base de datos",
                      bg="red2",
                      fg="white",
                      command=eliminar_bd
                      ).grid(row=5, column=1)

root.mainloop()


