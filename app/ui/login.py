import customtkinter as ctk
from tkinter import messagebox

# Configuración de la apariencia
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Función que se ejecuta al presionar el botón
def iniciar_sesion():
    if usuario.get() == "admin" and contrasena.get() == "1234":
        messagebox.showinfo("Bienvenido", "Inicio de sesión correcto")
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

# Crear ventana
ventana = ctk.CTk()
ventana.title("Sistema de Empresas")
ventana.geometry("500x450")

# Título
titulo = ctk.CTkLabel(
    ventana,
    text="SISTEMA DE EMPRESAS",
    font=("Arial", 24, "bold")
)
titulo.pack(pady=20)

# Usuario
usuario = ctk.CTkEntry(
    ventana,
    placeholder_text="Usuario",
    width=250
)
usuario.pack(pady=10)

# Contraseña
contrasena = ctk.CTkEntry(
    ventana,
    placeholder_text="Contraseña",
    show="*",
    width=250
)
contrasena.pack(pady=10)

# Botón
boton = ctk.CTkButton(
    ventana,
    text="Iniciar Sesión",
    command=iniciar_sesion
)
boton.pack(pady=20)

ventana.mainloop()

