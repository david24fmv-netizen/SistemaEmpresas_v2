import sqlite3
from pathlib import Path


# =========================================================
# UBICACIÓN DE LA BASE DE DATOS
# =========================================================

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DB_PATH = BASE_DIR / "empresas.db"


# =========================================================
# ACTUALIZAR ESTRUCTURA DE LA BASE DE DATOS
# =========================================================

def actualizar_estructura_base_datos():

    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()

    # -------------------------------------------------
    # SUBCONTRACTORS
    # -------------------------------------------------

    try:

        cursor.execute("""
            ALTER TABLE empresas
            ADD COLUMN subcontractors TEXT DEFAULT 'No'
        """)

    except sqlite3.OperationalError:
        pass

    # -------------------------------------------------
    # ACTIVIDAD COMERCIAL
    # -------------------------------------------------

    try:

        cursor.execute("""
            ALTER TABLE empresas
            ADD COLUMN actividad_comercial TEXT DEFAULT ''
        """)

    except sqlite3.OperationalError:
        pass

    conexion.commit()
    conexion.close()


# Ejecutar actualización de la estructura
actualizar_estructura_base_datos()


# =========================================================
# GUARDAR EMPRESA
# =========================================================

def guardar_empresa(datos):

    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO empresas (
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
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, datos)

    conexion.commit()
    conexion.close()


# =========================================================
# OBTENER EMPRESAS
# =========================================================

def obtener_empresas(busqueda=""):

    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()

    if busqueda:

        busqueda = f"%{busqueda}%"

        cursor.execute("""
            SELECT
                id,
                ein,
                name,
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
            busqueda,
            busqueda,
            busqueda
        ))

    else:

        cursor.execute("""
            SELECT
                id,
                ein,
                name,
                owner,
                fecha_digitada,
                extractos_bajados
            FROM empresas
            ORDER BY name COLLATE NOCASE ASC
        """)

    empresas = cursor.fetchall()

    conexion.close()

    return empresas


# =========================================================
# OBTENER EMPRESA POR ID
# =========================================================

def obtener_empresa_por_id(id_empresa):

    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT *
        FROM empresas
        WHERE id = ?
    """, (id_empresa,))

    empresa = cursor.fetchone()

    conexion.close()

    return empresa


# =========================================================
# ACTUALIZAR EMPRESA
# =========================================================

def actualizar_empresa(id_empresa, datos):

    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE empresas
        SET
            ein=?,
            name=?,
            corp_type=?,
            notes=?,
            renovacion=?,
            owner=?,
            stage=?,
            phone=?,
            email=?,
            document=?,
            date_reg=?,
            assigned_to=?,
            fecha_digitada=?,
            extractos_bajados=?,
            impreso_taxes=?,
            bank_clave=?,
            subcontractors=?,
            actividad_comercial=?
        WHERE id=?
    """, (
        datos[0],
        datos[1],
        datos[2],
        datos[3],
        datos[4],
        datos[5],
        datos[6],
        datos[7],
        datos[8],
        datos[9],
        datos[10],
        datos[11],
        datos[12],
        datos[13],
        datos[14],
        datos[15],
        datos[16],
        datos[17],
        id_empresa
    ))

    conexion.commit()
    conexion.close()


# =========================================================
# ELIMINAR EMPRESA
# =========================================================

def eliminar_empresa(id_empresa):

    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()

    cursor.execute("""
        DELETE FROM empresas
        WHERE id = ?
    """, (id_empresa,))

    conexion.commit()
    conexion.close()


# =========================================================
# BUSCAR EMPRESAS
# =========================================================

def buscar_empresas(texto):

    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT
            id,
            ein,
            name
        FROM empresas
        WHERE
            name LIKE ?
            OR ein LIKE ?
        ORDER BY name COLLATE NOCASE ASC
    """, (
        f"%{texto}%",
        f"%{texto}%"
    ))

    empresas = cursor.fetchall()

    conexion.close()

    return empresas


# =========================================================
# EMPRESAS CON EMAIL
# =========================================================

def obtener_empresas_con_email():

    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT
            id,
            name,
            email,
            owner
        FROM empresas
        WHERE email IS NOT NULL
        AND TRIM(email) != ''
        ORDER BY name COLLATE NOCASE ASC
    """)

    empresas = cursor.fetchall()

    conexion.close()

    return empresas



