import tkinter as tk
from tkinter import ttk

def format_decimal(value):
    return "{:.2f}".format(value)  # Formato con 2 decimales

root = tk.Tk()

treeview = ttk.Treeview(root, columns=("Value"))
treeview.heading("#0", text="Item")
treeview.heading("Value", text="Value")
treeview.pack()

# Datos de ejemplo
data = [
    ("Item 1", 10.123),
    ("Item 2", 20.456),
    ("Item 3", 30.789)
]

# Agregar los datos al Treeview
for item, value in data:
    formatted_value = format_decimal(value)
    treeview.insert("", "end", text=item, values=(formatted_value))

root.mainloop()
