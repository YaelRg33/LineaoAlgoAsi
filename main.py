import customtkinter as ctk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from fractions import Fraction

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

ventana = ctk.CTk()

ventana.title("Graficadora")
ventana.geometry("600x650")

fig, ax = plt.subplots(figsize=(5, 4), dpi=100)

def graficar():
    lbl_error.configure(text="")

    try:
        m = float(Fraction(entry_m.get()))
        b = float(Fraction(entry_b.get()))
    except ValueError:
        lbl_error.configure(text="Error: Ingresa valores numericos validos", text_color="red")
        return

    x_vals = np.linspace(-10, 10, 100)

    df = pd.DataFrame({'x': x_vals})
    df['y'] = (m * df['x']) + b

    ax.clear()

    ax.plot(df['x'], df['y'], 'b-', label=f'f(x) = {m}x + {b}')
    ax.set_xlabel('Eje X')
    ax.set_ylabel('Eje Y')

    ax.set_title('Funcion Lineal')

    ax.axhline(0, color='black', linewidth=1.2)
    ax.axvline(0, color='black', linewidth=1.2)

    ax.grid(True)
    ax.legend()

    canvas.draw()

frame_controles = ctk.CTkFrame(ventana)
frame_controles.pack(pady=20, padx=20, fill="x")

lbl_m = ctk.CTkLabel(frame_controles, text="Pendiente (m):", font=("Arial", 14))
lbl_m.grid(row=0, column=0, padx=10, pady=10)

entry_m = ctk.CTkEntry(frame_controles, placeholder_text="")
entry_m.grid(row=0, column=1, padx=10, pady=10)

lbl_b = ctk.CTkLabel(frame_controles, text="Intersección en Y (b):", font=("Arial", 14))
lbl_b.grid(row=0, column=2, padx=10, pady=10)

entry_b = ctk.CTkEntry(frame_controles, placeholder_text="")
entry_b.grid(row=0, column=3, padx=10, pady=10)

btn_graficar = ctk.CTkButton(ventana, text="Graficar", command=graficar, font=("Arial", 14, "bold"))
btn_graficar.pack(pady=10)

lbl_error = ctk.CTkLabel(ventana, text="", font=("Arial", 12))
lbl_error.pack(pady=5)

frame_grafica = ctk.CTkFrame(ventana)
frame_grafica.pack(pady=10, padx=20, fill="both", expand=True)

canvas = FigureCanvasTkAgg(fig, master=frame_grafica)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(fill="both", expand=True)

ventana.mainloop()