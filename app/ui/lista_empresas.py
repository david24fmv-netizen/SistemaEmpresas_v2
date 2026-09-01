import customtkinter as ctk
from CTkListbox import CTkListbox


class ListaEmpresas(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.pack(
            fill="y",
            padx=10,
            pady=10
        )

        titulo = ctk.CTkLabel(
            self,
            text="EMPRESAS",
            font=("Arial", 20, "bold")
        )

        titulo.pack(
            pady=(10, 5)
        )

        # -------------------------------------------------
        # BUSCADOR
        # -------------------------------------------------

        self.entry_buscar = ctk.CTkEntry(
            self,
            width=280,
            placeholder_text="🔍 Buscar por nombre, EIN o dueño..."
        )

        self.entry_buscar.pack(
            padx=10,
            pady=(0, 10)
        )

        # -------------------------------------------------
        # LISTA
        # -------------------------------------------------

        self.lista = CTkListbox(
            self,
            width=280,
            height=500
        )

        self.lista.pack(
            padx=10,
            pady=10,
            fill="both",
            expand=True
        )

    # -------------------------------------------------
    # LIMPIAR
    # -------------------------------------------------

    def limpiar(self):
        self.lista.delete("all")

    # -------------------------------------------------
    # AGREGAR EMPRESA
    # -------------------------------------------------

    def agregar(self, empresa):

        texto = f"{empresa[0]} - {empresa[2]}"

        self.lista.insert(
            "END",
            texto
        )

    # -------------------------------------------------
    # OBTENER SELECCIÓN
    # -------------------------------------------------

    def obtener_seleccion(self):
        return self.lista.get()

    # -------------------------------------------------
    # EVENTO SELECCIÓN
    # -------------------------------------------------

    def evento_seleccion(self, funcion):
        self.lista.configure(
            command=funcion
        )

    # -------------------------------------------------
    # OBTENER ID
    # -------------------------------------------------

    def obtener_id_seleccionado(self):

        seleccionado = self.lista.get()

        if not seleccionado:
            return None

        return int(
            seleccionado.split(" - ")[0]
        )

    # -------------------------------------------------
    # EVENTO BUSCADOR
    # -------------------------------------------------

    def evento_busqueda(self, funcion):

        self.entry_buscar.bind(
            "<KeyRelease>",
            funcion
        )

    # -------------------------------------------------
    # OBTENER TEXTO BUSCADO
    # -------------------------------------------------

    def obtener_busqueda(self):

        return self.entry_buscar.get()

    # -------------------------------------------------
    # LIMPIAR BUSCADOR
    # -------------------------------------------------

    def limpiar_busqueda(self):

        self.entry_buscar.delete(
            0,
            "end"
        )
        