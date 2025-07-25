import tkinter as tk
from tkinter import messagebox, ttk
import requests

API_URL = "http://127.0.0.1:8000/cars"


def registrar_auto():
    data = {
        "plate": entry_patente.get(),
        "owner": entry_duenio.get(),
        "hours": int(entry_horas.get()),
        "price_per_hour": float(entry_precio.get())
    }

    response = requests.post(API_URL + "/", json=data)
    if response.status_code == 200:
        messagebox.showinfo("Éxito", "Auto registrado correctamente.")
        limpiar_campos()
        cargar_tabla()
    else:
        messagebox.showerror("Error", f"No se pudo registrar. {response.text}")


def cargar_tabla():
    for i in tabla.get_children():
        tabla.delete(i)

    response = requests.get(API_URL + "/")
    if response.status_code == 200:
        for car in response.json():
            total = car["hours"] * car["price_per_hour"]
            tabla.insert("", "end", values=(
                car["plate"],
                car["owner"],
                car["hours"],
                car["price_per_hour"],
                round(total, 2)
            ))


def eliminar_auto():
    patente = entry_eliminar.get()
    response = requests.delete(f"{API_URL}/{patente}")
    if response.status_code == 200:
        messagebox.showinfo("Listo", "Auto eliminado correctamente.")
        entry_eliminar.delete(0, tk.END)
        cargar_tabla()
    else:
        messagebox.showerror("Error", "No se pudo eliminar el auto.")


def limpiar_campos():
    entry_patente.delete(0, tk.END)
    entry_duenio.delete(0, tk.END)
    entry_horas.delete(0, tk.END)
    entry_precio.delete(0, tk.END)


# GUI
root = tk.Tk()
root.title("Gestor de Estacionamiento")

frame_form = tk.Frame(root)
frame_form.pack(pady=10)

tk.Label(frame_form, text="Patente:").grid(row=0, column=0)
entry_patente = tk.Entry(frame_form)
entry_patente.grid(row=0, column=1)

tk.Label(frame_form, text="Dueño:").grid(row=1, column=0)
entry_duenio = tk.Entry(frame_form)
entry_duenio.grid(row=1, column=1)

tk.Label(frame_form, text="Horas:").grid(row=2, column=0)
entry_horas = tk.Entry(frame_form)
entry_horas.grid(row=2, column=1)

tk.Label(frame_form, text="Precio x hora:").grid(row=3, column=0)
entry_precio = tk.Entry(frame_form)
entry_precio.grid(row=3, column=1)

btn_registrar = tk.Button(
    frame_form, text="Registrar Auto", command=registrar_auto)
btn_registrar.grid(row=4, column=0, columnspan=2, pady=10)

# Tabla
cols = ("Patente", "Dueño", "Horas", "Precio x Hora", "Total Estimado")
tabla = ttk.Treeview(root, columns=cols, show="headings")
for col in cols:
    tabla.heading(col, text=col)
tabla.pack(pady=10)

# Eliminar
frame_delete = tk.Frame(root)
frame_delete.pack()

tk.Label(frame_delete, text="Eliminar por patente:").grid(row=0, column=0)
entry_eliminar = tk.Entry(frame_delete)
entry_eliminar.grid(row=0, column=1)
tk.Button(frame_delete, text="Eliminar",
          command=eliminar_auto).grid(row=0, column=2)

cargar_tabla()
root.mainloop()
