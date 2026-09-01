# Sistema de Empresas

Aplicación de escritorio desarrollada en Python para la gestión y control de empresas.

## Descripción

Sistema diseñado para registrar, consultar, actualizar y eliminar información de empresas mediante una interfaz gráfica.

La aplicación permite centralizar información empresarial, realizar búsquedas, controlar diferentes procesos administrativos y consultar estadísticas de los registros.

## Funcionalidades

- Registro de nuevas empresas.
- Consulta de empresas existentes.
- Actualización de información.
- Eliminación de empresas.
- Búsqueda por nombre, EIN o propietario.
- Gestión de información empresarial y de contacto.
- Registro de fecha de registro.
- Registro de fecha digitada.
- Registro de fecha de extractos bajados.
- Control de impresión de taxes.
- Control de subcontractors.
- Registro de actividad comercial.
- Registro de información bancaria.
- Gestión de responsables de cada empresa.

## Dashboard

El sistema incluye un dashboard con estadísticas generales de las empresas registradas.

Permite consultar:

- Total de empresas.
- Empresas con email.
- Empresas sin email.
- Empresas con taxes impresos.
- Empresas con taxes pendientes de impresión.
- Empresas con subcontractors.
- Empresas sin subcontractors.
- Empresas sin fecha digitada.
- Empresas sin extractos bajados.

Las estadísticas pueden actualizarse desde la propia aplicación.

## Control de Contabilidad

El sistema incluye un módulo de control de contabilidad que permite visualizar las empresas y consultar:

- Nombre de la empresa.
- Fecha digitada.
- Fecha de extractos bajados.

También permite buscar empresas por nombre, EIN o propietario y abrir directamente la información de una empresa desde el módulo de contabilidad.

## Gestión de Email

El sistema permite seleccionar una o varias empresas que tengan email registrado.

Incluye:

- Selección individual de empresas.
- Selección de todas las empresas.
- Contador de empresas seleccionadas.
- Visualización de los correos seleccionados.
- Copia de correos al portapapeles.
- Apertura de Gmail.
- Envío mediante destinatarios o CCO.

## Base de Datos

La aplicación utiliza SQLite para almacenar la información de las empresas.

La base de datos contiene información como:

- EIN
- Nombre
- Tipo de corporación
- Notas
- Renovación
- Propietario
- Stage
- Teléfono
- Email
- Documento
- Fecha de registro
- Responsable
- Fecha digitada
- Extractos bajados
- Impreso taxes
- Bank clave
- Subcontractors
- Actividad comercial

La estructura de la base de datos puede actualizarse para incorporar nuevos campos.

## Backup

El sistema incluye una función de copia de seguridad de la base de datos.

Las copias se almacenan en una carpeta `backups` y se generan con fecha y hora para facilitar su identificación.

## Exportación a Excel

La aplicación permite exportar la información de las empresas a un archivo Excel.

El archivo incluye:

- Todos los registros de empresas.
- Encabezados de las columnas.
- Formato de fechas.
- Filtros.
- Encabezados congelados.
- Ajuste automático del ancho de las columnas.

## Interfaz

La interfaz gráfica fue desarrollada utilizando CustomTkinter.

El sistema incluye ventanas independientes para:

- Gestión principal de empresas.
- Formulario de empresas.
- Lista y búsqueda de empresas.
- Dashboard.
- Control de contabilidad.
- Gestión de email.

## Tecnologías utilizadas

- Python
- CustomTkinter
- SQLite
- tkcalendar
- openpyxl

## Estructura del proyecto

```text
Sistema de Empresas/
│
├── app/
│   ├── controllers/
│   ├── database/
│   ├── services/
│   ├── ui/
│   └── utils/
│
├── backups/
├── empresas.db
└── main.py

Estado del proyecto

Proyecto funcional de escritorio para la gestión, organización y control de información empresarial y procesos administrativos.

Autor

David Moreno
