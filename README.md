# Mi-primera-app-en-la-nube
# DEMAND - Plataforma de Redirección de Video

Proyecto final para la materia de Ingeniería de Software, ITESO.

## Descripción
DEMAND es una implementación práctica de una arquitectura IaaS (Infraestructura como Servicio) en la nube pública de AWS. El sistema funciona como un orquestador de contenido que desacopla la lógica de negocio del almacenamiento de datos.

La aplicación permite listar un catálogo de películas disponibles y redirigir al usuario al contenido final de manera dinámica, utilizando instancias de computación para el procesamiento y almacenamiento de objetos para la persistencia de datos.

## Arquitectura del Sistema
El proyecto integra dos servicios principales de Amazon Web Services:

1. Amazon EC2 (Cómputo):
   - Servidor Linux corriendo la aplicación con FastAPI y Uvicorn.
   - Encargado de la lógica de ruteo, validación y comunicación con AWS.
   - Configurado manualmente con reglas de seguridad (Security Groups) para tráfico HTTP en el puerto 8080.

2. Amazon S3 (Almacenamiento):
   - Bucket 'demand-jair-links' utilizado como base de datos de enlaces.
   - Almacena objetos de texto (.txt) que contienen las URLs de destino.
   - Configurado con ACLs públicas para permitir la lectura remota desde la instancia EC2.
## Estructura del Proyecto

El funcionamiento del sistema se divide en tres archivos principales:

- **main.py**:
  Es el núcleo de la aplicación. Contiene el código en Python que inicializa el servidor con FastAPI. Aquí se definen las rutas de navegación, se configura la conexión segura con AWS mediante la librería Boto3 y se ejecuta la lógica que decide cómo listar los archivos del bucket y cómo redirigir al usuario.

- **requirements.txt**:
  Este archivo asegura que el proyecto sea reproducible en cualquier servidor. Contiene la lista exacta de las dependencias necesarias FastAPI, Uvicorn, Boto3 para que, al ejecutar el comando de instalación, el entorno virtual descargue las versiones correctas de cada librería.

- **index.html**:
  Representa la interfaz gráfica del usuario Frontend. Es la página web que consume la información del servidor para mostrar la lista de películas de forma visual y amigable, permitiendo que el usuario interactúe con el sistema sin tocar la terminal.
  
## Tecnologías
- Lenguaje: Python 3.9
- Framework: FastAPI
- SDK de Nube: Boto3
- Servidor: Uvicorn



## Autor
Jair Ernesto Aguilar Limón
Ingeniería de Software - ITESO
