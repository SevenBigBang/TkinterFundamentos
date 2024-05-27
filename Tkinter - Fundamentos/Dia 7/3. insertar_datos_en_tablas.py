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


# FUNCION PARA REGISTRAR USUARIOS NUEVOS:
def registro_cliente():
    nombre = entrada_nombre.get() # => CON entrada_nombre.get(), OBTENEMOS LOS DATOS QUE INGRESA EL USUARIO Y LOS ALMACENAMOS EN LOS CAMPOS RESPECTIVOS DE LA TABLA
    apellidos = entrada_apellidos.get()
    telefono = entrada_telefono.get()
    direccion = entrada_direccion.get()
    try:
        cursor.execute("INSERT INTO clientes (nombre, apellidos, telefono, direccion) VALUES (?,?,?,?)", (nombre, apellidos, telefono, direccion)) # => CON UNA CONSULTA SQL INSERTAMOS
        #                                                                           => Y LE DAMOS UN VALOR DE COMODIN "?", YA Q SEGUIDAMENTE LE DAREMOS EL VALOR DE LAS VARIABLES "nombre, apellidos, telefono, direccion".
        conexion.commit() # GUARDAMOS LOS CAMBIOS
    except conexion.Error as error_registro:
        print(f"Error en el registro: {error_registro}")


# INTERFAZ GRAFICA:

# CABECERA DE REGISTRO
tk.Label(root,
         text="Registro de nuevos clientes",
         font="calibri 18",
         fg="red"
         ).grid(row=0, columnspan=2)

# NOMBRE:
tk.Label(root,
         text="Nombre"
         ).grid(row=1, column=0, pady=10)

entrada_nombre =tk.Entry(root)
entrada_nombre.grid(row=1, column=1)


# APELLIDOS:
tk.Label(root,
         text="Apellidos"
         ).grid(row=2, column=1)

entrada_apellidos = tk.Entry(root)
entrada_apellidos.grid(row=2, column=1)


# TELEFONO:
tk.Label(root,
         text="Telefono"
         ).grid(row=3, column=1)

entrada_telefono = tk.Entry(root)
entrada_telefono.grid(row=3, column=1)


# DIRECCION:
tk.Label(root,
         text="Direccion"
         ).grid(row=4, column=1)
entrada_direccion = tk.Entry(root)
entrada_direccion.grid(row=4, column=1)




root.mainloop()


