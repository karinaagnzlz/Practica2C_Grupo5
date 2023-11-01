# Usa la imagen oficial de Python
FROM python:3.9

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

COPY requirements.txt ./

# Instala las dependencias necesarias
RUN pip install -r requirements.txt

# Copia los archivos de la aplicación al directorio de trabajo
COPY . .

# Expone el puerto 5000 para acceder a la aplicación
EXPOSE 4000

# Comando para ejecutar la aplicación Flask
CMD [ "flask", "run", "--host=0.0.0.0","--port=4000"]
