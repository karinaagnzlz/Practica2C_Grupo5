# Usa la imagen oficial de Python
FROM python:3.9

# Establece el directorio de trabajo
WORKDIR /app

COPY requirements.txt ./

# Instala las dependencias
RUN pip install -r requirements.txt

# Copia los archivos de la aplicación, incluyendo el archivo requirements.txt
COPY . .

# Expón el puerto de la aplicación
EXPOSE 4000

# Comando para ejecutar la aplicación
CMD [ "flask", "run", "--host=0.0.0.0","--port=4000"]
