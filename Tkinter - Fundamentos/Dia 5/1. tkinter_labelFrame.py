# El widget LabelFrame: SE USA PARA AÑADIR UN MARCO, EN ESTE EJEMPLO SE CREA UN BUSCADOR Y LA MEJOR PRACTICA EN TKINTER ES USAR UN MARCO(FRAME), COMO CONTENEDOR DE WIDGETS

import tkinter as tk

root = tk.Tk()
root.title("Frames/Marcos")


# BUSCADOR 1
# SE CREA UN MARCO EN LA VENTANA ROOT, SE LE ASIGNA TEXTO Y PADDINGS
buscador = tk.LabelFrame(root, text="Buscador...", padx=30, pady=30)
buscador.grid(row=0, column=0, padx=5, pady=5) # => ESTOS POSICIONAMIENTOS SOLO AFECTAN DENTRO DE LA VENTANA PRINCIPAL "root"

# A ESTE MARCO PREVIAMENTE CREADO LE PONEMOS DENTRO LA BARRA Y EL BOTON, ASI DANDOLE SUS PROPIAS REGLAS 
barra = tk.Entry(buscador, text="¿Buscas algo?").grid(row=0, column=1) # => ESTOS POSICIONAMIENTOS SOLO APLICAN DENTRO DEL MARCO "buscador"
boton = tk.Button(buscador, text="Buscar").grid(row=0, column=0)






# BUSCADOR 2
buscador2 = tk.LabelFrame(root, text="Buscador...2", padx=30, pady=30)
buscador2.grid(row=1, column=0, padx=5, pady=5)

barra2 = tk.Entry(buscador2, text="¿Buscas algo?").grid(row=0, column=0)
boton2 = tk.Button(buscador2, text="Buscar").grid(row=0, column=1)






root.mainloop()