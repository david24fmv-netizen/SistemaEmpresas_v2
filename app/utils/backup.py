import shutil
from pathlib import Path
from datetime import datetime


BASE_DIR = Path(__file__).resolve().parent.parent.parent
DB_PATH = BASE_DIR / "empresas.db"
BACKUP_DIR = BASE_DIR / "backups"


def crear_backup():

    # Crear carpeta backups si no existe
    BACKUP_DIR.mkdir(exist_ok=True)

    # Comprobar que existe la base de datos
    if not DB_PATH.exists():
        return None

    # Crear nombre con fecha y hora
    fecha = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    archivo_backup = BACKUP_DIR / f"empresas_{fecha}.db"

    # Copiar la base de datos
    shutil.copy2(DB_PATH, archivo_backup)

    return archivo_backup
