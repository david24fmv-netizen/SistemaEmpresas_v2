from app.services.empresa_service import (
    guardar_empresa,
    obtener_empresas,
    obtener_empresa_por_id,
    actualizar_empresa,
    eliminar_empresa,
    buscar_empresas
)


class EmpresaController:

    def guardar(self, datos):
        guardar_empresa(datos)

    def listar(self, busqueda=""):
        return obtener_empresas(busqueda)

    def buscar(self, texto):
        return buscar_empresas(texto)

    def obtener(self, id_empresa):
        return obtener_empresa_por_id(id_empresa)

    def actualizar(self, id_empresa, datos):
        actualizar_empresa(id_empresa, datos)

    def eliminar(self, id_empresa):
        eliminar_empresa(id_empresa)
        
        
