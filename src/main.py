import boto3
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

# CONFIGURACIÓN
BUCKET_NAME = "demand-jair-links"
s3_client = boto3.client("s3", region_name="us-east-1")

# RUTA 1: LISTAR PELÍCULAS
# El EC2 mira dentro del bucket S3 y busca archivos de texto
@app.get("/list")
def listar_peliculas():
    try:
        response = s3_client.list_objects_v2(Bucket=BUCKET_NAME)
        archivos = response.get("Contents", [])

        lista_peliculas = []
        for obj in archivos:
            # Solo listamos los archivos .txt (que son nuestros "videos")
            if obj["Key"].endswith(".txt"):
                lista_peliculas.append(obj["Key"])

        return {"videos": lista_peliculas}
    except Exception as e:
        return {"error": str(e)}

# RUTA 2: VER PELÍCULA

@app.get("/ver/{nombre_archivo}")
def ver_pelicula(nombre_archivo: str):
    try:
        # Descargar el objeto de S3 a la memoria
        archivo = s3_client.get_object(Bucket=BUCKET_NAME, Key=nombre_archivo)

        # Leer el link que está escrito adentro
        link_youtube = archivo["Body"].read().decode('utf-8').strip()

        # Redirigir al usuario
        return RedirectResponse(url=link_youtube)

    except Exception as e:
        raise HTTPException(status_code=404, detail="Película no encontrada")

# Servir la página web
app.mount("/", StaticFiles(directory=os.path.dirname(__file__), html=True), name="static")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)