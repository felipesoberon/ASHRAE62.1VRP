# mainGUI.py

import tkinter as tk
from tkinter import ttk, messagebox
from vrp_dictionaries import VRP_TABLE_6_1
from mainVRP import vrp_calculate  # Import your computation function

def calculate():
    try:
        occupancy = occupancy_var.get()
        area_ft2 = float(area_var.get())
        num_people_str = people_var.get().strip()
        Ez = float(ez_var.get())

        if not occupancy or occupancy not in VRP_TABLE_6_1:
            messagebox.showerror("Error", "Select a valid occupancy category.")
            return

        num_people = int(num_people_str) if num_people_str else None

        output, Voz, info = vrp_calculate(occupancy, area_ft2, num_people, Ez)

        # Clear previous results
        for row in tree.get_children():
            tree.delete(row)
        for row in output:
            tree.insert("", "end", values=row)

    except Exception as e:
        messagebox.showerror("Error", str(e))


root = tk.Tk()
root.title("ASHRAE 62.1-2022 VRP Calculator")

frm = ttk.Frame(root, padding=10)
frm.pack(fill="x")

occupancy_var = tk.StringVar(value=list(VRP_TABLE_6_1.keys())[0])
area_var = tk.StringVar(value="969")
people_var = tk.StringVar(value="")
ez_var = tk.StringVar(value="1.0")

ttk.Label(frm, text="Occupancy:").grid(row=0, column=0, sticky="w")
occ_combo = ttk.Combobox(
    frm,
    textvariable=occupancy_var,
    values=list(VRP_TABLE_6_1.keys()),
    width=35,
    height=50   # Add this line for a taller dropdown
)
occ_combo.grid(row=0, column=1, columnspan=2, sticky="ew")


ttk.Label(frm, text="Area (ft²):").grid(row=1, column=0, sticky="w")
ttk.Entry(frm, textvariable=area_var, width=12).grid(row=1, column=1, sticky="w")

ttk.Label(frm, text="People (leave blank for default):").grid(row=2, column=0, sticky="w")
ttk.Entry(frm, textvariable=people_var, width=12).grid(row=2, column=1, sticky="w")

ttk.Label(frm, text="Ez:").grid(row=3, column=0, sticky="w")
ttk.Entry(frm, textvariable=ez_var, width=12).grid(row=3, column=1, sticky="w")

ttk.Button(frm, text="Calculate", command=calculate).grid(row=4, column=0, columnspan=3, pady=6)

tree = ttk.Treeview(root, columns=("Parameter", "Value", "Units", "Notes"), show="headings", height=10)
for col in ("Parameter", "Value", "Units", "Notes"):
    tree.heading(col, text=col)
    tree.column(col, width=150 if col != "Notes" else 270, anchor="w")
tree.pack(fill="both", padx=10, pady=6, expand=True)

root.mainloop()
