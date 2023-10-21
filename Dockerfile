# Usa la imagen oficial de Python
FROM python:3.9

# Establece el directorio de trabajo
WORKDIR /app

# Crear un entorno virtual
RUN python -m venv venv

# Activar el entorno virtual y luego instalar las dependencias
RUN . venv/bin/activate && pip install -r requirements.txt

# Copia los archivos de la aplicación
COPY . .

# Instala las dependencias
RUN pip install -r requirements.txt

# Expón el puerto de la aplicación
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
