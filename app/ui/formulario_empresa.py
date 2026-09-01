import customtkinter as ctk
from tkcalendar import DateEntry


class FormularioEmpresa(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.id_empresa = None

        # =================================================
        # CONTENEDOR PRINCIPAL
        # =================================================

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # =================================================
        # SCROLL
        # =================================================

        self.scroll = ctk.CTkScrollableFrame(
            self,
            width=760,
            height=560
        )

        self.scroll.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=10,
            pady=10
        )

        self.scroll.grid_columnconfigure(1, weight=1)
        self.scroll.grid_columnconfigure(3, weight=1)

        # =================================================
        # COLUMNA IZQUIERDA
        # =================================================

        # EIN
        ctk.CTkLabel(
            self.scroll,
            text="EIN"
        ).grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.entry_ein = ctk.CTkEntry(
            self.scroll,
            width=300
        )
        self.entry_ein.grid(row=0, column=1, padx=10, pady=10)

        # NAME
        ctk.CTkLabel(
            self.scroll,
            text="NAME"
        ).grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.entry_name = ctk.CTkEntry(
            self.scroll,
            width=300
        )
        self.entry_name.grid(row=1, column=1, padx=10, pady=10)

        # CORP TYPE
        ctk.CTkLabel(
            self.scroll,
            text="CORP TYPE"
        ).grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.entry_corp = ctk.CTkEntry(
            self.scroll,
            width=300
        )
        self.entry_corp.grid(row=2, column=1, padx=10, pady=10)

        # OWNER
        ctk.CTkLabel(
            self.scroll,
            text="OWNER"
        ).grid(row=3, column=0, padx=10, pady=10, sticky="w")

        self.entry_owner = ctk.CTkEntry(
            self.scroll,
            width=300
        )
        self.entry_owner.grid(row=3, column=1, padx=10, pady=10)

        # STAGE
        ctk.CTkLabel(
            self.scroll,
            text="STAGE"
        ).grid(row=4, column=0, padx=10, pady=10, sticky="w")

        self.entry_stage = ctk.CTkEntry(
            self.scroll,
            width=300
        )
        self.entry_stage.grid(row=4, column=1, padx=10, pady=10)

        # PHONE
        ctk.CTkLabel(
            self.scroll,
            text="PHONE"
        ).grid(row=5, column=0, padx=10, pady=10, sticky="w")

        self.entry_phone = ctk.CTkEntry(
            self.scroll,
            width=300
        )
        self.entry_phone.grid(row=5, column=1, padx=10, pady=10)

        # EMAIL
        ctk.CTkLabel(
            self.scroll,
            text="EMAIL"
        ).grid(row=6, column=0, padx=10, pady=10, sticky="w")

        self.entry_email = ctk.CTkEntry(
            self.scroll,
            width=300
        )
        self.entry_email.grid(row=6, column=1, padx=10, pady=10)

        # DOCUMENT
        ctk.CTkLabel(
            self.scroll,
            text="DOCUMENT"
        ).grid(row=7, column=0, padx=10, pady=10, sticky="w")

        self.entry_document = ctk.CTkEntry(
            self.scroll,
            width=300
        )
        self.entry_document.grid(row=7, column=1, padx=10, pady=10)

        # =================================================
        # COLUMNA DERECHA
        # =================================================

        # DATE REG
        ctk.CTkLabel(
            self.scroll,
            text="DATE REG"
        ).grid(row=0, column=2, padx=10, pady=10, sticky="w")

        self.entry_date_reg = ctk.CTkEntry(
            self.scroll,
            width=300
        )
        self.entry_date_reg.grid(row=0, column=3, padx=10, pady=10)

        # ASSIGNED TO
        ctk.CTkLabel(
            self.scroll,
            text="ASSIGNED TO"
        ).grid(row=1, column=2, padx=10, pady=10, sticky="w")

        self.entry_assigned = ctk.CTkEntry(
            self.scroll,
            width=300
        )
        self.entry_assigned.grid(row=1, column=3, padx=10, pady=10)

        # =================================================
        # FECHA DIGITADA - CALENDARIO
        # =================================================

        ctk.CTkLabel(
            self.scroll,
            text="FECHA DIGITADA"
        ).grid(row=2, column=2, padx=10, pady=10, sticky="w")

        self.entry_fecha_digitada = DateEntry(
            self.scroll,
            width=28,
            date_pattern="yyyy-mm-dd",
            background="darkblue",
            foreground="white",
            borderwidth=2,
            state="readonly"
        )

        self.entry_fecha_digitada.grid(
            row=2,
            column=3,
            padx=10,
            pady=10
        )

        # =================================================
        # EXTRACTOS BAJADOS - CALENDARIO
        # =================================================

        ctk.CTkLabel(
            self.scroll,
            text="EXTRACTOS BAJADOS"
        ).grid(row=3, column=2, padx=10, pady=10, sticky="w")

        self.entry_extractos = DateEntry(
            self.scroll,
            width=28,
            date_pattern="yyyy-mm-dd",
            background="darkblue",
            foreground="white",
            borderwidth=2,
            state="readonly"
        )

        self.entry_extractos.grid(
            row=3,
            column=3,
            padx=10,
            pady=10
        )

        # =================================================
        # NOTES
        # =================================================

        ctk.CTkLabel(
            self.scroll,
            text="NOTES"
        ).grid(row=4, column=2, padx=10, pady=10, sticky="w")

        self.entry_notes = ctk.CTkEntry(
            self.scroll,
            width=300
        )
        self.entry_notes.grid(row=4, column=3, padx=10, pady=10)

        # =================================================
        # RENOVACIÓN
        # =================================================

        ctk.CTkLabel(
            self.scroll,
            text="RENOVACIÓN"
        ).grid(row=5, column=2, padx=10, pady=10, sticky="w")

        self.entry_renovacion = ctk.CTkEntry(
            self.scroll,
            width=300
        )
        self.entry_renovacion.grid(row=5, column=3, padx=10, pady=10)

        # =================================================
        # IMPRESO TAXES
        # =================================================

        ctk.CTkLabel(
            self.scroll,
            text="IMPRESO TAXES"
        ).grid(row=6, column=2, padx=10, pady=10, sticky="w")

        self.entry_impreso = ctk.CTkComboBox(
            self.scroll,
            width=300,
            values=["Sí", "No"]
        )

        self.entry_impreso.grid(
            row=6,
            column=3,
            padx=10,
            pady=10
        )

        self.entry_impreso.set("No")

        # =================================================
        # BANK CLAVE
        # =================================================

        ctk.CTkLabel(
            self.scroll,
            text="BANK CLAVE"
        ).grid(row=7, column=2, padx=10, pady=10, sticky="w")

        self.entry_bank = ctk.CTkEntry(
            self.scroll,
            width=300
        )

        self.entry_bank.grid(
            row=7,
            column=3,
            padx=10,
            pady=10
        )

        # =================================================
        # SUBCONTRACTORS
        # =================================================

        ctk.CTkLabel(
            self.scroll,
            text="SUBCONTRACTORS"
        ).grid(row=8, column=2, padx=10, pady=10, sticky="w")

        self.entry_subcontractors = ctk.CTkComboBox(
            self.scroll,
            width=300,
            values=["Sí", "No"]
        )

        self.entry_subcontractors.grid(
            row=8,
            column=3,
            padx=10,
            pady=10
        )

        self.entry_subcontractors.set("No")

        # =================================================
        # ACTIVIDAD COMERCIAL
        # =================================================

        ctk.CTkLabel(
            self.scroll,
            text="ACTIVIDAD COMERCIAL"
        ).grid(row=9, column=2, padx=10, pady=10, sticky="w")

        self.entry_actividad = ctk.CTkEntry(
            self.scroll,
            width=300
        )

        self.entry_actividad.grid(
            row=9,
            column=3,
            padx=10,
            pady=10
        )

    # =================================================
    # OBTENER DATOS
    # =================================================

    def obtener_datos(self):

        return (
            self.entry_ein.get(),
            self.entry_name.get(),
            self.entry_corp.get(),
            self.entry_notes.get(),
            self.entry_renovacion.get(),
            self.entry_owner.get(),
            self.entry_stage.get(),
            self.entry_phone.get(),
            self.entry_email.get(),
            self.entry_document.get(),
            self.entry_date_reg.get(),
            self.entry_assigned.get(),
            self.entry_fecha_digitada.get(),
            self.entry_extractos.get(),
            self.entry_impreso.get(),
            self.entry_bank.get(),
            self.entry_subcontractors.get(),
            self.entry_actividad.get()
        )

    # =================================================
    # LIMPIAR
    # =================================================

    def limpiar(self):

        self.id_empresa = None

        self.entry_ein.delete(0, "end")
        self.entry_name.delete(0, "end")
        self.entry_corp.delete(0, "end")
        self.entry_notes.delete(0, "end")
        self.entry_renovacion.delete(0, "end")
        self.entry_owner.delete(0, "end")
        self.entry_stage.delete(0, "end")
        self.entry_phone.delete(0, "end")
        self.entry_email.delete(0, "end")
        self.entry_document.delete(0, "end")
        self.entry_date_reg.delete(0, "end")
        self.entry_assigned.delete(0, "end")

        # Limpiar fechas
        self.entry_fecha_digitada.set_date(None)
        self.entry_extractos.set_date(None)

        self.entry_impreso.set("No")
        self.entry_bank.delete(0, "end")

        self.entry_subcontractors.set("No")
        self.entry_actividad.delete(0, "end")

    # =================================================
    # CARGAR EMPRESA
    # =================================================

    def cargar_datos(self, empresa):

        self.limpiar()

        self.id_empresa = empresa[0]

        self.entry_ein.insert(
            0,
            empresa[1] or ""
        )

        self.entry_name.insert(
            0,
            empresa[2] or ""
        )

        self.entry_corp.insert(
            0,
            empresa[3] or ""
        )

        self.entry_notes.insert(
            0,
            empresa[4] or ""
        )

        self.entry_renovacion.insert(
            0,
            empresa[5] or ""
        )

        self.entry_owner.insert(
            0,
            empresa[6] or ""
        )

        self.entry_stage.insert(
            0,
            empresa[7] or ""
        )

        self.entry_phone.insert(
            0,
            empresa[8] or ""
        )

        self.entry_email.insert(
            0,
            empresa[9] or ""
        )

        self.entry_document.insert(
            0,
            empresa[10] or ""
        )

        self.entry_date_reg.insert(
            0,
            empresa[11] or ""
        )

        self.entry_assigned.insert(
            0,
            empresa[12] or ""
        )

        # =================================================
        # FECHAS
        # =================================================

        if empresa[13]:

            try:
                self.entry_fecha_digitada.set_date(
                    empresa[13]
                )
            except Exception:
                pass

        if empresa[14]:

            try:
                self.entry_extractos.set_date(
                    empresa[14]
                )
            except Exception:
                pass

        # =================================================
        # IMPRESO TAXES
        # =================================================

        self.entry_impreso.set(
            empresa[15] if empresa[15] else "No"
        )

        # =================================================
        # BANK CLAVE
        # =================================================

        self.entry_bank.insert(
            0,
            empresa[16] or ""
        )

        # =================================================
        # SUBCONTRACTORS
        # =================================================

        self.entry_subcontractors.set(
            empresa[17] if empresa[17] else "No"
        )

        # =================================================
        # ACTIVIDAD COMERCIAL
        # =================================================

        self.entry_actividad.insert(
            0,
            empresa[18] if empresa[18] else ""
        )

    # =================================================
    # OBTENER ID
    # =================================================

    def obtener_id(self):

        return self.id_empresa
    
    
    
    
