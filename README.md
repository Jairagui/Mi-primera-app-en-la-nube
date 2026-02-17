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

## Tecnologías
- Lenguaje: Python 3.9
- Framework: FastAPI
- SDK de Nube: Boto3
- Servidor: Uvicorn



## Autor
Jair Ernesto Aguilar Limón
Ingeniería de Software - ITESO
