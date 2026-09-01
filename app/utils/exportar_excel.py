import sqlite3
from pathlib import Path
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment


# =========================================================
# BASE DE DATOS
# =========================================================

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DB_PATH = BASE_DIR / "empresas.db"


# =========================================================
# FORMATO DE FECHA
# =========================================================

def formatear_fecha(fecha):

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


# =========================================================
# EXPORTAR EMPRESAS A EXCEL
# =========================================================

def exportar_empresas_excel(ruta_archivo):

    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT
            id,
            ein,
            name,
            corp_type,
            notes,
            renovacion,
            owner,
            stage,
            phone,
            email,
            document,
            date_reg,
            assigned_to,
            fecha_digitada,
            extractos_bajados,
            impreso_taxes,
            bank_clave,
            subcontractors,
            actividad_comercial
        FROM empresas
        ORDER BY name COLLATE NOCASE ASC
    """)

    empresas = cursor.fetchall()

    conexion.close()

    # =====================================================
    # CREAR ARCHIVO EXCEL
    # =====================================================

    libro = Workbook()

    hoja = libro.active

    hoja.title = "Empresas"

    # =====================================================
    # ENCABEZADOS
    # =====================================================

    encabezados = [
        "ID",
        "EIN",
        "NAME",
        "CORP TYPE",
        "NOTES",
        "RENOVACION",
        "OWNER",
        "STAGE",
        "PHONE",
        "EMAIL",
        "DOCUMENT",
        "DATE REG",
        "ASSIGNED TO",
        "FECHA DIGITADA",
        "EXTRACTOS BAJADOS",
        "IMPRESO TAXES",
        "BANK CLAVE",
        "SUBCONTRACTORS",
        "ACTIVIDAD COMERCIAL"
    ]

    hoja.append(encabezados)

    # =====================================================
    # FORMATO DE ENCABEZADOS
    # =====================================================

    for celda in hoja[1]:

        celda.font = Font(
            bold=True
        )

        celda.alignment = Alignment(
            horizontal="center",
            vertical="center"
        )

    # =====================================================
    # DATOS
    # =====================================================

    for empresa in empresas:

        datos = list(empresa)

        # -------------------------------------------------
        # FECHA DIGITADA
        # -------------------------------------------------

        datos[13] = formatear_fecha(
            datos[13]
        )

        # -------------------------------------------------
        # EXTRACTOS BAJADOS
        # -------------------------------------------------

        datos[14] = formatear_fecha(
            datos[14]
        )

        hoja.append(
            datos
        )

    # =====================================================
    # CONGELAR ENCABEZADOS
    # =====================================================

    hoja.freeze_panes = "A2"

    # =====================================================
    # FILTRO
    # =====================================================

    hoja.auto_filter.ref = hoja.dimensions

    # =====================================================
    # AJUSTAR ANCHO DE COLUMNAS
    # =====================================================

    for columna in hoja.columns:

        longitud = 0

        letra = columna[0].column_letter

        for celda in columna:

            if celda.value is not None:

                longitud = max(
                    longitud,
                    len(str(celda.value))
                )

        hoja.column_dimensions[letra].width = min(
            longitud + 2,
            40
        )

    # =====================================================
    # GUARDAR
    # =====================================================

    libro.save(
        ruta_archivo
    )
    