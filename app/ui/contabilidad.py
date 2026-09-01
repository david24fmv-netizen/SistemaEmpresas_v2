import customtkinter as ctk
import sqlite3
from pathlib import Path


# =========================================================
# BASE DE DATOS
# =========================================================

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DB_PATH = BASE_DIR / "empresas.db"


class VentanaContabilidad(ctk.CTkToplevel):

    def __init__(self, master, abrir_empresa=None):

        super().__init__(master)

        self.master_principal = master
        self.abrir_empresa_callback = abrir_empresa

        self.title("Control de Contabilidad")
        self.geometry("1050x650")
        self.minsize(850, 500)

        # Mantener la ventana visible
        self.transient(master)
        self.lift()
        self.focus_force()

        # =================================================
        # TÍTULO
        # =================================================

        titulo = ctk.CTkLabel(
            self,
            text="CONTROL DE CONTABILIDAD",
            font=("Arial", 26, "bold")
        )

        titulo.pack(
            pady=(20, 10)
        )

        # =================================================
        # BUSCADOR
        # =================================================

        buscador_frame = ctk.CTkFrame(
            self
        )

        buscador_frame.pack(
            fill="x",
            padx=20,
            pady=(0, 10)
        )

        ctk.CTkLabel(
            buscador_frame,
            text="Buscar:"
        ).pack(
            side="left",
            padx=(10, 5)
        )

        self.entry_busqueda = ctk.CTkEntry(
            buscador_frame,
            placeholder_text="Empresa, EIN o dueño...",
            width=350
        )

        self.entry_busqueda.pack(
            side="left",
            padx=5
        )

        self.entry_busqueda.bind(
            "<KeyRelease>",
            self.buscar
        )

        ctk.CTkButton(
            buscador_frame,
            text="Limpiar",
            width=100,
            command=self.limpiar_busqueda
        ).pack(
            side="left",
            padx=10
        )

        # =================================================
        # CONTENEDOR
        # =================================================

        contenedor = ctk.CTkFrame(
            self
        )

        contenedor.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        # =================================================
        # ENCABEZADOS
        # =================================================

        encabezados = ctk.CTkFrame(
            contenedor
        )

        encabezados.pack(
            fill="x",
            padx=10,
            pady=(10, 0)
        )

        encabezados.grid_columnconfigure(
            0,
            weight=4
        )

        encabezados.grid_columnconfigure(
            1,
            weight=2
        )

        encabezados.grid_columnconfigure(
            2,
            weight=2
        )

        ctk.CTkLabel(
            encabezados,
            text="EMPRESA",
            font=("Arial", 14, "bold")
        ).grid(
            row=0,
            column=0,
            padx=15,
            pady=10,
            sticky="w"
        )

        ctk.CTkLabel(
            encabezados,
            text="FECHA DIGITADA",
            font=("Arial", 14, "bold")
        ).grid(
            row=0,
            column=1,
            padx=15,
            pady=10,
            sticky="w"
        )

        ctk.CTkLabel(
            encabezados,
            text="EXTRACTOS BAJADOS",
            font=("Arial", 14, "bold")
        ).grid(
            row=0,
            column=2,
            padx=15,
            pady=10,
            sticky="w"
        )

        # =================================================
        # LISTA
        # =================================================

        self.lista = ctk.CTkScrollableFrame(
            contenedor
        )

        self.lista.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=5
        )

        self.lista.grid_columnconfigure(
            0,
            weight=4
        )

        self.lista.grid_columnconfigure(
            1,
            weight=2
        )

        self.lista.grid_columnconfigure(
            2,
            weight=2
        )

        # =================================================
        # CARGAR EMPRESAS
        # =================================================

        self.cargar_empresas()

        # =================================================
        # BOTÓN CERRAR
        # =================================================

        ctk.CTkButton(
            self,
            text="Cerrar",
            width=150,
            command=self.destroy
        ).pack(
            pady=15
        )

    # =====================================================
    # OBTENER EMPRESAS
    # =====================================================

    def obtener_empresas(self, busqueda=""):

        conexion = sqlite3.connect(
            DB_PATH
        )

        cursor = conexion.cursor()

        if busqueda:

            texto = f"%{busqueda}%"

            cursor.execute("""
                SELECT
                    id,
                    name,
                    ein,
                    owner,
                    fecha_digitada,
                    extractos_bajados
                FROM empresas
                WHERE
                    name LIKE ?
                    OR ein LIKE ?
                    OR owner LIKE ?
                ORDER BY name COLLATE NOCASE ASC
            """, (
                texto,
                texto,
                texto
            ))

        else:

            cursor.execute("""
                SELECT
                    id,
                    name,
                    ein,
                    owner,
                    fecha_digitada,
                    extractos_bajados
                FROM empresas
                ORDER BY name COLLATE NOCASE ASC
            """)

        empresas = cursor.fetchall()

        conexion.close()

        return empresas

    # =====================================================
    # CARGAR EMPRESAS
    # =====================================================

    def cargar_empresas(self, busqueda=""):

        # Borrar lista anterior
        for widget in self.lista.winfo_children():
            widget.destroy()

        empresas = self.obtener_empresas(
            busqueda
        )

        # =================================================
        # SIN RESULTADOS
        # =================================================

        if not empresas:

            ctk.CTkLabel(
                self.lista,
                text="No se encontraron empresas.",
                font=("Arial", 16)
            ).grid(
                row=0,
                column=0,
                columnspan=3,
                pady=30
            )

            return

        # =================================================
        # MOSTRAR EMPRESAS
        # =================================================

        for fila, empresa in enumerate(empresas):

            id_empresa = empresa[0]
            nombre = empresa[1] or ""
            fecha_digitada = empresa[4] or ""
            extractos = empresa[5] or ""

            fecha_digitada = self.formatear_fecha(
                fecha_digitada
            )

            extractos = self.formatear_fecha(
                extractos
            )

            # =================================================
            # FILA
            # =================================================

            fila_frame = ctk.CTkFrame(
                self.lista,
                cursor="hand2"
            )

            fila_frame.grid(
                row=fila,
                column=0,
                columnspan=3,
                sticky="ew",
                padx=5,
                pady=3
            )

            fila_frame.grid_columnconfigure(
                0,
                weight=4
            )

            fila_frame.grid_columnconfigure(
                1,
                weight=2
            )

            fila_frame.grid_columnconfigure(
                2,
                weight=2
            )

            # =================================================
            # EMPRESA
            # =================================================

            etiqueta_empresa = ctk.CTkLabel(
                fila_frame,
                text=nombre,
                anchor="w",
                font=("Arial", 13),
                cursor="hand2"
            )

            etiqueta_empresa.grid(
                row=0,
                column=0,
                padx=15,
                pady=12,
                sticky="w"
            )

            # =================================================
            # FECHA DIGITADA
            # =================================================

            etiqueta_digitada = ctk.CTkLabel(
                fila_frame,
                text=fecha_digitada,
                anchor="w",
                font=("Arial", 13),
                cursor="hand2"
            )

            etiqueta_digitada.grid(
                row=0,
                column=1,
                padx=15,
                pady=12,
                sticky="w"
            )

            # =================================================
            # EXTRACTOS BAJADOS
            # =================================================

            etiqueta_extractos = ctk.CTkLabel(
                fila_frame,
                text=extractos,
                anchor="w",
                font=("Arial", 13),
                cursor="hand2"
            )

            etiqueta_extractos.grid(
                row=0,
                column=2,
                padx=15,
                pady=12,
                sticky="w"
            )

            # =================================================
            # DOBLE CLIC EN TODA LA FILA
            # =================================================

            self.configurar_doble_clic(
                fila_frame,
                id_empresa
            )

            self.configurar_doble_clic(
                etiqueta_empresa,
                id_empresa
            )

            self.configurar_doble_clic(
                etiqueta_digitada,
                id_empresa
            )

            self.configurar_doble_clic(
                etiqueta_extractos,
                id_empresa
            )

    # =====================================================
    # CONFIGURAR DOBLE CLIC
    # =====================================================

    def configurar_doble_clic(
        self,
        widget,
        id_empresa
    ):

        widget.bind(
            "<Double-Button-1>",
            lambda evento,
            id_empresa=id_empresa:
            self.seleccionar_empresa(
                id_empresa
            )
        )

    # =====================================================
    # SELECCIONAR EMPRESA
    # =====================================================

    def seleccionar_empresa(
        self,
        id_empresa
    ):

        if self.abrir_empresa_callback is None:
            return

        self.abrir_empresa_callback(
            id_empresa
        )

    # =====================================================
    # BUSCAR
    # =====================================================

    def buscar(self, evento=None):

        texto = self.entry_busqueda.get().strip()

        self.cargar_empresas(
            texto
        )

    # =====================================================
    # LIMPIAR BUSQUEDA
    # =====================================================

    def limpiar_busqueda(self):

        self.entry_busqueda.delete(
            0,
            "end"
        )

        self.cargar_empresas()

    # =====================================================
    # REFRESCAR
    # =====================================================

    def refrescar(self):

        texto = self.entry_busqueda.get().strip()

        self.cargar_empresas(
            texto
        )

    # =====================================================
    # FORMATO DE FECHA USA
    # =====================================================

    def formatear_fecha(
        self,
        fecha
    ):

        if not fecha:
            return ""

        fecha = str(fecha).strip()

        try:

            partes = fecha.split("-")

            if len(partes) == 3:

                año = partes[0]
                mes = partes[1]
                dia = partes[2]

                return f"{mes}/{dia}/{año}"

        except Exception:
            pass

        return fecha
    
    
    