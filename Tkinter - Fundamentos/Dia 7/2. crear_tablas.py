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

root.mainloop()


# DE ESTA FORMA CONECTAMOS PYTHON A UNA BASE DE DATOS Y ADEMAS CREAMOS UNA TABLA CON SINTAXIS SQL, DE ESTA FORMA USANDO UN TRY EXCEPT MANEJAMOS DE MEJOR FORMA LOS POSIBLES ERRORES AL MOMENTO 
# DE CONECTARNOS A NUESTRA BASE DE DATOS; CONTINUA EN "insertar_datos_en_tablas.py"