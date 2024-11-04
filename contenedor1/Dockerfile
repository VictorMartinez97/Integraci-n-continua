# Usa una imagen base, como Python para un servidor web simple
FROM python:3.9-slim

# Instalando dependencias
RUN pip install flask

# Copiar el código de la aplicación
COPY app.py /app/app.py

# Establecer el directorio de trabajo
WORKDIR /app

# Exponer el puerto que va a utilizar este contenedor
EXPOSE 5000

# Ejecutar la aplicación
CMD ["python", "app.py"]
