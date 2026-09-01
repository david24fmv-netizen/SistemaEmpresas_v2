import sqlite3
from pathlib import Path

# Ruta de la base de datos
BASE_DIR = Path(__file__).resolve().parent.parent.parent
DB_PATH = BASE_DIR / "empresas.db"


def crear_base_datos():
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS empresas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ein TEXT,
            name TEXT,
            corp_type TEXT,
            notes TEXT,
            renovacion TEXT,
            owner TEXT,
            stage TEXT,
            phone TEXT,
            email TEXT,
            document TEXT,
            date_reg TEXT,
            assigned_to TEXT,
            fecha_digitada TEXT,
            extractos_bajados TEXT,
            impreso_taxes TEXT,
            bank_clave TEXT
        )
    """)

    conexion.commit()
    conexion.close()

    print("Base de datos creada correctamente.")


if __name__ == "__main__":
    crear_base_datos()
