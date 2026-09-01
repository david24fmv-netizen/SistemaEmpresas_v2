import customtkinter as ctk
from tkinter import messagebox
import webbrowser
from urllib.parse import quote


class VentanaEmail(ctk.CTkToplevel):

    def __init__(self, master, empresas):
        super().__init__(master)

        # =================================================
        # CONFIGURACIÓN DE LA VENTANA
        # =================================================

        self.title("Enviar Email")
        self.geometry("750x780")
        self.minsize(750, 780)

        # La ventana pertenece a la ventana principal
        self.transient(master)

        # Traer al frente
        self.lift()
        self.focus_force()

        # Mantenerla visible encima del sistema
        self.attributes("-topmost", True)

        self.empresas = empresas
        self.variables = []

        # =================================================
        # TÍTULO
        # =================================================

        titulo = ctk.CTkLabel(
            self,
            text="ENVIAR EMAIL",
            font=("Arial", 24, "bold")
        )

        titulo.pack(pady=15)

        # =================================================
        # LISTA DE EMPRESAS
        # =================================================

        self.lista_frame = ctk.CTkScrollableFrame(
            self,
            width=680,
            height=280
        )

        self.lista_frame.pack(
            padx=20,
            pady=10,
            fill="x"
        )

        # =================================================
        # CREAR EMPRESAS
        # =================================================

        for empresa in empresas:

            empresa_id = empresa[0]
            nombre = empresa[1]
            email = empresa[2]
            owner = empresa[3]

            variable = ctk.BooleanVar(
                value=False
            )

            self.variables.append(
                (
                    empresa_id,
                    variable,
                    email
                )
            )

            texto = f"{nombre}  |  {email}"

            if owner:
                texto += f"  |  Owner: {owner}"

            checkbox = ctk.CTkCheckBox(
                self.lista_frame,
                text=texto,
                variable=variable
            )

            checkbox.pack(
                anchor="w",
                padx=10,
                pady=6
            )

        # =================================================
        # SELECCIONAR TODAS
        # =================================================

        self.seleccionar_todas_var = ctk.BooleanVar(
            value=False
        )

        seleccionar_todas = ctk.CTkCheckBox(
            self,
            text="Seleccionar todas",
            variable=self.seleccionar_todas_var,
            command=self.seleccionar_todas
        )

        seleccionar_todas.pack(
            pady=8
        )

        # =================================================
        # CONTADOR
        # =================================================

        self.label_contador = ctk.CTkLabel(
            self,
            text="Seleccionadas: 0"
        )

        self.label_contador.pack(
            pady=3
        )

        # =================================================
        # CORREOS SELECCIONADOS
        # =================================================

        ctk.CTkLabel(
            self,
            text="Correos seleccionados:"
        ).pack(
            pady=(8, 3)
        )

        self.texto_correos = ctk.CTkTextbox(
            self,
            width=680,
            height=70
        )

        self.texto_correos.pack(
            padx=20,
            pady=5
        )

        # =================================================
        # TIPO DE ENVÍO
        # =================================================

        self.tipo_envio = ctk.StringVar(
            value="to"
        )

        opciones = ctk.CTkFrame(
            self
        )

        opciones.pack(
            pady=8
        )

        ctk.CTkRadioButton(
            opciones,
            text="Para",
            variable=self.tipo_envio,
            value="to"
        ).pack(
            side="left",
            padx=20
        )

        ctk.CTkRadioButton(
            opciones,
            text="CCO",
            variable=self.tipo_envio,
            value="bcc"
        ).pack(
            side="left",
            padx=20
        )

        # =================================================
        # BOTONES
        # =================================================

        botones = ctk.CTkFrame(
            self
        )

        botones.pack(
            pady=15
        )

        # COPIAR

        ctk.CTkButton(
            botones,
            text="📋 Copiar correos",
            width=150,
            command=self.copiar_correos
        ).pack(
            side="left",
            padx=8
        )

        # GMAIL

        ctk.CTkButton(
            botones,
            text="📧 Abrir Gmail",
            width=150,
            command=self.abrir_gmail
        ).pack(
            side="left",
            padx=8
        )

        # ATRÁS

        ctk.CTkButton(
            botones,
            text="↩️ Atrás",
            width=120,
            command=self.cerrar
        ).pack(
            side="left",
            padx=8
        )

        # =================================================
        # ACTUALIZAR CONTADOR
        # =================================================

        for _, variable, _ in self.variables:

            variable.trace_add(
                "write",
                self.actualizar_contador
            )

    # =====================================================
    # OBTENER CORREOS
    # =====================================================

    def obtener_correos(self):

        return [
            email
            for _, variable, email in self.variables
            if variable.get()
            and email
        ]

    # =====================================================
    # SELECCIONAR TODAS
    # =====================================================

    def seleccionar_todas(self):

        estado = self.seleccionar_todas_var.get()

        for _, variable, _ in self.variables:

            variable.set(estado)

    # =====================================================
    # ACTUALIZAR CONTADOR
    # =====================================================

    def actualizar_contador(self, *args):

        correos = self.obtener_correos()

        self.label_contador.configure(
            text=f"Seleccionadas: {len(correos)}"
        )

        self.actualizar_texto_correos()

    # =====================================================
    # MOSTRAR CORREOS
    # =====================================================

    def actualizar_texto_correos(self):

        correos = self.obtener_correos()

        texto = ", ".join(correos)

        self.texto_correos.delete(
            "1.0",
            "end"
        )

        self.texto_correos.insert(
            "1.0",
            texto
        )

    # =====================================================
    # COPIAR CORREOS
    # =====================================================

    def copiar_correos(self):

        correos = self.obtener_correos()

        if not correos:

            messagebox.showwarning(
                "Atención",
                "Seleccione al menos una empresa."
            )

            return

        texto = ", ".join(correos)

        self.clipboard_clear()

        self.clipboard_append(
            texto
        )

        self.update()

        messagebox.showinfo(
            "Correos copiados",
            "Los correos fueron copiados correctamente.\n\n"
            "Ahora puedes pegarlos directamente en Gmail."
        )

    # =====================================================
    # ABRIR GMAIL
    # =====================================================

    def abrir_gmail(self):

        correos = self.obtener_correos()

        if not correos:

            messagebox.showwarning(
                "Atención",
                "Seleccione al menos una empresa."
            )

            return

        destinatarios = ",".join(
            correos
        )

        tipo = self.tipo_envio.get()

        url = (
            "https://mail.google.com/mail/"
            "?view=cm"
            "&fs=1"
            f"&{tipo}="
            + quote(destinatarios)
        )

        webbrowser.open(url)

    # =====================================================
    # CERRAR / ATRÁS
    # =====================================================

    def cerrar(self):

        self.destroy()
        

