print("Estoy en main")

from app.database.database import crear_base_datos
from app.ui.principal import iniciar_aplicacion

print("Imports correctos")

crear_base_datos()

print("Voy a abrir la ventana")

iniciar_aplicacion()

print("La ventana se cerró")
