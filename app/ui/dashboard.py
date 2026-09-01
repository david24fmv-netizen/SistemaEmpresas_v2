import customtkinter as ctk
import sqlite3
from pathlib import Path


# =========================================================
# BASE DE DATOS
# =========================================================

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DB_PATH = BASE_DIR / "empresas.db"


class VentanaDashboard(ctk.CTkToplevel):

    def __init__(self, master):

        super().__init__(master)

        self.title("Dashboard - Resumen de Empresas")
        self.geometry("850x650")
        self.minsize(700, 500)

        # Mantener la ventana visible
        self.transient(master)
        self.lift()
        self.focus_force()

        # =================================================
        # TÍTULO
        # =================================================

        titulo = ctk.CTkLabel(
            self,
            text="RESUMEN DE EMPRESAS",
            font=("Arial", 28, "bold")
        )

        titulo.pack(
            pady=(20, 10)
        )

        # =================================================
        # CONTENEDOR SCROLL
        # =================================================

        self.contenedor = ctk.CTkScrollableFrame(
            self
        )

        self.contenedor.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=10
        )

        # =================================================
        # CONFIGURACIÓN
        # =================================================

        self.contenedor.grid_columnconfigure(
            0,
            weight=1
        )

        self.contenedor.grid_columnconfigure(
            1,
            weight=1
        )

        # =================================================
        # CREAR TARJETAS
        # =================================================

        self.tarjetas = []

        self.crear_tarjeta(
            "EMPRESAS TOTALES",
            "total",
            0,
            0
        )

        self.crear_tarjeta(
            "CON EMAIL",
            "con_email",
            0,
            1
        )

        self.crear_tarjeta(
            "SIN EMAIL",
            "sin_email",
            1,
            0
        )

        self.crear_tarjeta(
            "IMPRESO TAXES: SÍ",
            "impreso_si",
            1,
            1
        )

        self.crear_tarjeta(
            "IMPRESO TAXES: NO",
            "impreso_no",
            2,
            0
        )

        self.crear_tarjeta(
            "SUBCONTRACTORS: SÍ",
            "subcontractors_si",
            2,
            1
        )

        self.crear_tarjeta(
            "SUBCONTRACTORS: NO",
            "subcontractors_no",
            3,
            0
        )

        self.crear_tarjeta(
            "SIN FECHA DIGITADA",
            "sin_fecha_digitada",
            3,
            1
        )

        self.crear_tarjeta(
            "SIN EXTRACTOS",
            "sin_extractos",
            4,
            0
        )

        # =================================================
        # BOTONES
        # =================================================

        botones = ctk.CTkFrame(
            self
        )

        botones.pack(
            fill="x",
            padx=25,
            pady=(5, 15)
        )

        botones.grid_columnconfigure(
            0,
            weight=1
        )

        botones.grid_columnconfigure(
            1,
            weight=1
        )

        # -------------------------------------------------
        # ACTUALIZAR
        # -------------------------------------------------

        ctk.CTkButton(
            botones,
            text="🔄 Actualizar estadísticas",
            command=self.actualizar
        ).grid(
            row=0,
            column=0,
            padx=10,
            pady=5,
            sticky="e"
        )

        # -------------------------------------------------
        # CERRAR
        # -------------------------------------------------

        ctk.CTkButton(
            botones,
            text="Cerrar",
            width=150,
            command=self.destroy
        ).grid(
            row=0,
            column=1,
            padx=10,
            pady=5,
            sticky="w"
        )

    # =====================================================
    # OBTENER ESTADÍSTICAS
    # =====================================================

    def obtener_estadisticas(self):

        conexion = sqlite3.connect(
            DB_PATH
        )

        cursor = conexion.cursor()

        # -------------------------------------------------
        # TOTAL
        # -------------------------------------------------

        cursor.execute("""
            SELECT COUNT(*)
            FROM empresas
        """)

        total = cursor.fetchone()[0]

        # -------------------------------------------------
        # CON EMAIL
        # -------------------------------------------------

        cursor.execute("""
            SELECT COUNT(*)
            FROM empresas
            WHERE email IS NOT NULL
            AND TRIM(email) != ''
        """)

        con_email = cursor.fetchone()[0]

        # -------------------------------------------------
        # SIN EMAIL
        # -------------------------------------------------

        sin_email = total - con_email

        # -------------------------------------------------
        # IMPRESO TAXES - SÍ
        # -------------------------------------------------

        cursor.execute("""
            SELECT COUNT(*)
            FROM empresas
            WHERE LOWER(TRIM(impreso_taxes)) = 'sí'
            OR LOWER(TRIM(impreso_taxes)) = 'si'
        """)

        impreso_si = cursor.fetchone()[0]

        # -------------------------------------------------
        # IMPRESO TAXES - NO
        # -------------------------------------------------

        cursor.execute("""
            SELECT COUNT(*)
            FROM empresas
            WHERE LOWER(TRIM(impreso_taxes)) = 'no'
        """)

        impreso_no = cursor.fetchone()[0]

        # -------------------------------------------------
        # SUBCONTRACTORS - SÍ
        # -------------------------------------------------

        cursor.execute("""
            SELECT COUNT(*)
            FROM empresas
            WHERE LOWER(TRIM(subcontractors)) = 'sí'
            OR LOWER(TRIM(subcontractors)) = 'si'
        """)

        subcontractors_si = cursor.fetchone()[0]

        # -------------------------------------------------
        # SUBCONTRACTORS - NO
        # -------------------------------------------------

        cursor.execute("""
            SELECT COUNT(*)
            FROM empresas
            WHERE LOWER(TRIM(subcontractors)) = 'no'
        """)

        subcontractors_no = cursor.fetchone()[0]

        # -------------------------------------------------
        # SIN FECHA DIGITADA
        # -------------------------------------------------

        cursor.execute("""
            SELECT COUNT(*)
            FROM empresas
            WHERE fecha_digitada IS NULL
            OR TRIM(fecha_digitada) = ''
        """)

        sin_fecha_digitada = cursor.fetchone()[0]

        # -------------------------------------------------
        # SIN EXTRACTOS
        # -------------------------------------------------

        cursor.execute("""
            SELECT COUNT(*)
            FROM empresas
            WHERE extractos_bajados IS NULL
            OR TRIM(extractos_bajados) = ''
        """)

        sin_extractos = cursor.fetchone()[0]

        conexion.close()

        return {
            "total": total,
            "con_email": con_email,
            "sin_email": sin_email,
            "impreso_si": impreso_si,
            "impreso_no": impreso_no,
            "subcontractors_si": subcontractors_si,
            "subcontractors_no": subcontractors_no,
            "sin_fecha_digitada": sin_fecha_digitada,
            "sin_extractos": sin_extractos
        }

    # =====================================================
    # CREAR TARJETA
    # =====================================================

    def crear_tarjeta(
        self,
        titulo,
        clave,
        fila,
        columna
    ):

        tarjeta = ctk.CTkFrame(
            self.contenedor,
            height=115
        )

        tarjeta.grid(
            row=fila,
            column=columna,
            padx=12,
            pady=12,
            sticky="nsew"
        )

        tarjeta.grid_propagate(
            False
        )

        # =================================================
        # TÍTULO
        # =================================================

        ctk.CTkLabel(
            tarjeta,
            text=titulo,
            font=("Arial", 14, "bold")
        ).pack(
            pady=(18, 3)
        )

        # =================================================
        # VALOR
        # =================================================

        valor = ctk.CTkLabel(
            tarjeta,
            text="0",
            font=("Arial", 28, "bold")
        )

        valor.pack(
            pady=3
        )

        # Guardamos referencia
        self.tarjetas.append(
            (
                clave,
                valor
            )
        )

        # Mostrar valor inicial
        estadisticas = self.obtener_estadisticas()

        valor.configure(
            text=str(
                estadisticas[clave]
            )
        )

    # =====================================================
    # ACTUALIZAR ESTADÍSTICAS
    # =====================================================

    def actualizar(self):

        estadisticas = self.obtener_estadisticas()

        for clave, etiqueta in self.tarjetas:

            if clave in estadisticas:

                etiqueta.configure(
                    text=str(
                        estadisticas[clave]
                    )
                )
                