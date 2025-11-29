import tkinter as tk
from tkinter import ttk, messagebox
from database import WeatherDatabase

def show_weather():
    city = city_entry.get()
    db = WeatherDatabase()
    rows = db.fetch_all(city)
    db.close()

    # Limpa a tabela
    for item in tree.get_children():
        tree.delete(item)

    # Adiciona os resultados
    for row in rows:
        tree.insert("", "end", values=row)

# Janela principal
root = tk.Tk()
root.title("Weather Dashboard")
root.geometry("600x400")

# Entrada de cidade
frame_top = tk.Frame(root)
frame_top.pack(pady=10)

tk.Label(frame_top, text="Cidade:").pack(side="left")
city_entry = tk.Entry(frame_top)
city_entry.pack(side="left", padx=5)

tk.Button(frame_top, text="Buscar", command=show_weather).pack(side="left")

# Tabela de resultados
columns = ("id", "city", "temperature", "humidity", "description", "timestamp")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
tree.pack(fill="both", expand=True)

root.mainloop()
