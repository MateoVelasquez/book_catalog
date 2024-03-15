# Usa la imagen base de Python
FROM python:3.12-slim

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el contenido del directorio actual al contenedor en /app
COPY . /app

# Instala las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto 8000 en el contenedor
EXPOSE 8000

# Define la variable de entorno para la URL de MongoDB
ENV MONGO_URL="mongodb://mongo:27017/"
ENV MONGO_DATABASE_NAME="local"

# Define el comando para ejecutar la aplicación
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
