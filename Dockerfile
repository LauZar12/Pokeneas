# Usa la imagen base de Python
FROM python:3.8-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia todos los archivos del proyecto al contenedor
COPY . /app

# Instala las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Define el comando por defecto para ejecutar la aplicación
CMD ["flask", "run", "--host=0.0.0.0"]
