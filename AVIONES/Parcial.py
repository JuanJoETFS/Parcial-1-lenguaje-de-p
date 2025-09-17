import tkinter as tk
from tkinter import messagebox
import sys
RUTA_DEL_LOGO = "Avion.ico"
# Clase Avion para almacenar nombre y tipo de avión
class Avion:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

# Clase GestorAviones para gestionar los aviones
class GestorAviones:
    def __init__(self):
        self.aviones = []

    def agregar_avion(self, nombre, tipo):
        avion = Avion(nombre, tipo)
        self.aviones.append(avion)

    def eliminar_avion(self, indice):
        try:
            avion_eliminado = self.aviones.pop(indice)
            return avion_eliminado.nombre
        except IndexError:
            return None

# Función para agregar un nuevo avión
def agregar_avion():
    nombre = entry_nombre.get()
    tipo = entry_tipo.get()
    
    if nombre and tipo:
        gestor.agregar_avion(nombre, tipo)
        listbox_aviones.insert(tk.END, f"{nombre} - {tipo}")
        entry_nombre.delete(0, tk.END)
        entry_tipo.delete(0, tk.END)
        messagebox.showinfo("Avión agregado", f"El avión '{nombre}' ha sido agregado.")
    else:
        messagebox.showwarning("Error", "Por favor, ingrese un nombre y un tipo de avión.")

# Función para mostrar el tipo de un avión seleccionado
def ver_tipo():
    seleccion = listbox_aviones.curselection()
    if seleccion:
        indice = seleccion[0]
        avion = gestor.aviones[indice]
        messagebox.showinfo(f"Tipo de {avion.nombre}", f"Tipo: {avion.tipo}")
    else:
        messagebox.showwarning("Error", "Seleccione un avión para ver su tipo.")

# Función para eliminar un avión seleccionado
def eliminar_avion():
    seleccion = listbox_aviones.curselection()
    if seleccion:
        indice = seleccion[0]
        nombre = gestor.eliminar_avion(indice)
        if nombre:
            listbox_aviones.delete(indice)
            messagebox.showinfo("Avión eliminado", f"El avión '{nombre}' ha sido eliminado.")
        else:
            messagebox.showerror("Error", "No se pudo eliminar el avión.")
    else:
        messagebox.showwarning("Error", "Seleccione un avión para eliminar.")

# Función para mostrar la ventana "Acerca de"
def mostrar_acerca_de():
    """Muestra información sobre la aplicación."""
    messagebox.showinfo(
        "Acerca del Gestor de Aviones",
        f"creado por: Juan Jose Restrepo Alvarez\n"
        f"Versión de Python: {sys.version}"
    )

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Aviones")

# Instancia del gestor de aviones
gestor = GestorAviones()

# --- Menú ---
barra_menu = tk.Menu(ventana)

# Menú Archivo (opcional, para coherencia)
menu_archivo = tk.Menu(barra_menu, tearoff=0)
menu_archivo.add_command(label="Salir", command=ventana.quit)
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)

# Menú Ayuda
menu_ayuda = tk.Menu(barra_menu, tearoff=0)
menu_ayuda.add_command(label="Acerca de...", command=mostrar_acerca_de)
barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)

ventana.config(menu=barra_menu)

# Etiquetas y entradas para el nombre y el tipo de avión
label_nombre = tk.Label(ventana, text="Nombre del avión:")
label_nombre.pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

label_tipo = tk.Label(ventana, text="Tipo de avión:")
label_tipo.pack()
entry_tipo = tk.Entry(ventana)
entry_tipo.pack()

# Botón para agregar avión
btn_agregar = tk.Button(ventana, text="Agregar avión", command=agregar_avion)
btn_agregar.pack()

# Listbox para mostrar los aviones guardados
listbox_aviones = tk.Listbox(ventana)
listbox_aviones.pack()

# Botones para ver y eliminar aviones
btn_ver = tk.Button(ventana, text="Ver tipo", command=ver_tipo)
btn_ver.pack()

btn_eliminar = tk.Button(ventana, text="Eliminar avión", command=eliminar_avion)
btn_eliminar.pack()

# Iniciar el bucle principal de la ventana
ventana.mainloop()