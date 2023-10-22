# Usa la imagen oficial de Python
FROM python:3.6-slim-buster

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de los requerimientos
COPY requirements.txt ./

# Crear un entorno virtual
RUN pip install -r requirements.txt

# Copia los archivos de la aplicación
COPY . .

# Expón el puerto de la aplicación
EXPOSE 4000

# Comando para ejecutar la aplicación
CMD [ "flask", "run", "--host=0.0.0.0", "--port=4000"]