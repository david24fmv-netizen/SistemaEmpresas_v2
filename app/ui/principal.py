import customtkinter as ctk
from tkinter import messagebox, filedialog

from app.controllers.empresa_controller import EmpresaController
from app.ui.formulario_empresa import FormularioEmpresa
from app.ui.lista_empresas import ListaEmpresas
from app.ui.email import VentanaEmail
from app.ui.contabilidad import VentanaContabilidad
from app.ui.dashboard import VentanaDashboard

from app.utils.backup import crear_backup
from app.utils.exportar_excel import exportar_empresas_excel
from app.services.empresa_service import obtener_empresas_con_email


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

controller = EmpresaController()


def iniciar_aplicacion():

    # =================================================
    # ACTUALIZAR LISTA PRINCIPAL
    # =================================================

    def actualizar_lista(busqueda=""):

        lista.limpiar()

        empresas = controller.listar(busqueda)

        for empresa in empresas:
            lista.agregar(empresa)

    # =================================================
    # BUSCAR
    # =================================================

    def buscar(evento=None):

        texto = lista.obtener_busqueda()

        actualizar_lista(texto)

    # =================================================
    # EMPRESA NUEVA
    # =================================================

    def empresa_nueva():

        formulario.limpiar()

        messagebox.showinfo(
            "Empresa nueva",
            "El formulario está listo para ingresar una empresa nueva."
        )

    # =================================================
    # GUARDAR
    # =================================================

    def guardar():

        if formulario.obtener_id() is not None:

            messagebox.showwarning(
                "Empresa existente",
                "Está viendo una empresa existente.\n\n"
                "Para modificarla utilice el botón "
                "\"Actualizar\".\n\n"
                "Para crear una empresa nueva, presione "
                "\"Empresa Nueva\"."
            )

            return

        datos = formulario.obtener_datos()

        if not datos[1].strip():

            messagebox.showwarning(
                "Datos incompletos",
                "Ingrese el nombre de la empresa."
            )

            return

        controller.guardar(datos)

        formulario.limpiar()

        actualizar_lista(
            lista.obtener_busqueda()
        )

        # Actualizar Dashboard si está abierto
        if hasattr(ventana, "ventana_dashboard"):

            try:

                if ventana.ventana_dashboard.winfo_exists():
                    ventana.ventana_dashboard.actualizar()

            except Exception:
                pass

        messagebox.showinfo(
            "Correcto",
            "La empresa fue guardada correctamente."
        )

    # =================================================
    # SELECCIONAR EMPRESA
    # =================================================

    def seleccionar(valor):

        id_empresa_seleccionada = (
            lista.obtener_id_seleccionado()
        )

        if id_empresa_seleccionada is None:
            return

        empresa = controller.obtener(
            id_empresa_seleccionada
        )

        if empresa is not None:

            formulario.cargar_datos(
                empresa
            )

    # =================================================
    # ACTUALIZAR EMPRESA
    # =================================================

    def actualizar():

        id_empresa = formulario.obtener_id()

        if id_empresa is None:

            messagebox.showwarning(
                "Atención",
                "Seleccione una empresa para actualizar."
            )

            return

        datos = formulario.obtener_datos()

        controller.actualizar(
            id_empresa,
            datos
        )

        # Actualizar lista principal
        actualizar_lista(
            lista.obtener_busqueda()
        )

        # =================================================
        # ACTUALIZAR CONTABILIDAD
        # =================================================

        if hasattr(
            ventana,
            "ventana_contabilidad"
        ):

            try:

                if ventana.ventana_contabilidad.winfo_exists():

                    ventana.ventana_contabilidad.refrescar()

            except Exception:
                pass

        # =================================================
        # ACTUALIZAR DASHBOARD
        # =================================================

        if hasattr(
            ventana,
            "ventana_dashboard"
        ):

            try:

                if ventana.ventana_dashboard.winfo_exists():

                    ventana.ventana_dashboard.actualizar()

            except Exception:
                pass

        messagebox.showinfo(
            "Correcto",
            "La empresa fue actualizada correctamente."
        )

    # =================================================
    # ELIMINAR EMPRESA
    # =================================================

    def eliminar():

        id_empresa = lista.obtener_id_seleccionado()

        if id_empresa is None:

            messagebox.showwarning(
                "Atención",
                "Seleccione una empresa para eliminar."
            )

            return

        respuesta = messagebox.askyesno(
            "Confirmar eliminación",
            "¿Está seguro de eliminar esta empresa?\n\n"
            "Esta acción no se puede deshacer."
        )

        if respuesta:

            controller.eliminar(
                id_empresa
            )

            formulario.limpiar()

            actualizar_lista(
                lista.obtener_busqueda()
            )

            # Actualizar Contabilidad
            if hasattr(
                ventana,
                "ventana_contabilidad"
            ):

                try:

                    if ventana.ventana_contabilidad.winfo_exists():

                        ventana.ventana_contabilidad.refrescar()

                except Exception:
                    pass

            # Actualizar Dashboard
            if hasattr(
                ventana,
                "ventana_dashboard"
            ):

                try:

                    if ventana.ventana_dashboard.winfo_exists():

                        ventana.ventana_dashboard.actualizar()

                except Exception:
                    pass

            messagebox.showinfo(
                "Correcto",
                "La empresa fue eliminada correctamente."
            )

    # =================================================
    # BACKUP
    # =================================================

    def hacer_backup():

        archivo = crear_backup()

        if archivo is None:

            messagebox.showerror(
                "Error",
                "No se encontró la base de datos."
            )

            return

        messagebox.showinfo(
            "Copia de seguridad",
            "Copia creada correctamente.\n\n"
            f"Archivo:\n{archivo.name}"
        )

    # =================================================
    # EXPORTAR EXCEL
    # =================================================

    def exportar_excel():

        ruta = filedialog.asksaveasfilename(
            title="Guardar empresas en Excel",
            defaultextension=".xlsx",
            filetypes=[
                ("Archivo Excel", "*.xlsx")
            ],
            initialfile="empresas.xlsx"
        )

        if not ruta:
            return

        try:

            exportar_empresas_excel(
                ruta
            )

            messagebox.showinfo(
                "Exportación correcta",
                "Las empresas fueron exportadas correctamente."
            )

        except Exception as error:

            messagebox.showerror(
                "Error",
                "No se pudo exportar el archivo.\n\n"
                f"{error}"
            )

    # =================================================
    # ENVIAR EMAIL
    # =================================================

    def enviar_email():

        empresas = obtener_empresas_con_email()

        if not empresas:

            messagebox.showwarning(
                "Sin correos",
                "No hay empresas con una dirección de email registrada."
            )

            return

        ventana.ventana_email = VentanaEmail(
            ventana,
            empresas
        )

        ventana.ventana_email.focus()

    # =================================================
    # ABRIR EMPRESA DESDE CONTABILIDAD
    # =================================================

    def abrir_empresa_desde_contabilidad(
        id_empresa
    ):

        empresa = controller.obtener(
            id_empresa
        )

        if empresa is None:
            return

        formulario.cargar_datos(
            empresa
        )

        ventana.lift()
        ventana.focus_force()

    # =================================================
    # ABRIR CONTABILIDAD
    # =================================================

    def abrir_contabilidad():

        ventana.ventana_contabilidad = (
            VentanaContabilidad(
                ventana,
                abrir_empresa=abrir_empresa_desde_contabilidad
            )
        )

        ventana.ventana_contabilidad.focus()

    # =================================================
    # ABRIR DASHBOARD
    # =================================================

    def abrir_dashboard():

        ventana.ventana_dashboard = (
            VentanaDashboard(
                ventana
            )
        )

        ventana.ventana_dashboard.focus()

    # =================================================
    # VENTANA PRINCIPAL
    # =================================================

    ventana = ctk.CTk()

    ventana.title(
        "Sistema de Empresas"
    )

    ventana.geometry(
        "1200x700"
    )

    # =================================================
    # TÍTULO
    # =================================================

    titulo = ctk.CTkLabel(
        ventana,
        text="SISTEMA DE EMPRESAS",
        font=("Arial", 28, "bold")
    )

    titulo.pack(
        pady=20
    )

    # =================================================
    # CUERPO
    # =================================================

    cuerpo = ctk.CTkFrame(
        ventana
    )

    cuerpo.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=20
    )

    # =================================================
    # PANEL IZQUIERDO
    # =================================================

    izquierda = ctk.CTkFrame(
        cuerpo
    )

    izquierda.pack(
        side="left",
        fill="y",
        padx=10
    )

    # =================================================
    # PANEL DERECHO
    # =================================================

    derecha = ctk.CTkFrame(
        cuerpo
    )

    derecha.pack(
        side="left",
        fill="both",
        expand=True,
        padx=10
    )

    # =================================================
    # LISTA DE EMPRESAS
    # =================================================

    lista = ListaEmpresas(
        izquierda
    )

    lista.evento_seleccion(
        seleccionar
    )

    lista.evento_busqueda(
        buscar
    )

    # =================================================
    # FORMULARIO
    # =================================================

    formulario = FormularioEmpresa(
        derecha
    )

    formulario.pack(
        padx=20,
        pady=20,
        fill="both",
        expand=True
    )

    # =================================================
    # BOTONES
    # =================================================

    botones = ctk.CTkFrame(
        derecha
    )

    botones.pack(
        pady=20
    )

    # -------------------------------------------------
    # EMPRESA NUEVA
    # -------------------------------------------------

    ctk.CTkButton(
        botones,
        text="Empresa Nueva",
        command=empresa_nueva
    ).pack(
        side="left",
        padx=8
    )

    # -------------------------------------------------
    # GUARDAR
    # -------------------------------------------------

    ctk.CTkButton(
        botones,
        text="Guardar",
        command=guardar
    ).pack(
        side="left",
        padx=8
    )

    # -------------------------------------------------
    # ACTUALIZAR
    # -------------------------------------------------

    ctk.CTkButton(
        botones,
        text="Actualizar",
        command=actualizar
    ).pack(
        side="left",
        padx=8
    )

    # -------------------------------------------------
    # ELIMINAR
    # -------------------------------------------------

    ctk.CTkButton(
        botones,
        text="Eliminar",
        command=eliminar
    ).pack(
        side="left",
        padx=8
    )

    # -------------------------------------------------
    # EMAIL
    # -------------------------------------------------

    ctk.CTkButton(
        botones,
        text="📧 Enviar Email",
        command=enviar_email
    ).pack(
        side="left",
        padx=8
    )

    # -------------------------------------------------
    # CONTABILIDAD
    # -------------------------------------------------

    ctk.CTkButton(
        botones,
        text="📊 Contabilidad",
        command=abrir_contabilidad
    ).pack(
        side="left",
        padx=8
    )

    # -------------------------------------------------
    # DASHBOARD
    # -------------------------------------------------

    ctk.CTkButton(
        botones,
        text="📈 Dashboard",
        command=abrir_dashboard
    ).pack(
        side="left",
        padx=8
    )

    # -------------------------------------------------
    # BACKUP
    # -------------------------------------------------

    ctk.CTkButton(
        botones,
        text="💾 Backup",
        command=hacer_backup
    ).pack(
        side="left",
        padx=8
    )

    # -------------------------------------------------
    # EXCEL
    # -------------------------------------------------

    ctk.CTkButton(
        botones,
        text="📊 Exportar Excel",
        command=exportar_excel
    ).pack(
        side="left",
        padx=8
    )

    # -------------------------------------------------
    # SALIR
    # -------------------------------------------------

    ctk.CTkButton(
        botones,
        text="Salir",
        command=ventana.destroy
    ).pack(
        side="left",
        padx=8
    )

    # =================================================
    # CARGAR EMPRESAS AL INICIAR
    # =================================================

    actualizar_lista()

    # =================================================
    # INICIAR APLICACIÓN
    # =================================================

    ventana.mainloop()
    
