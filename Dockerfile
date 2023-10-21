FROM python:3.12-slim as build

RUN apt-get update -y \
    && apt-get install -y build-essential libpq-dev git \
    && pip install virtualenv \
    && virtualenv /opt/Practica2C_Grupo5/venv \
    && . /opt/Practica2C_Grupo5/venv/bin/activate \
    && pip install gunicorn

COPY . /Practica2C_Grupo5

WORKDIR /Practica2C_Grupo5

RUN . /opt/Practica2C_Grupo5/venv/bin/activate \
    && pip install .

FROM python:3.12-slim

COPY --from=build /opt/Practica2C_Grupo5 /opt/Practica2C_Grupo5
COPY entrypoint.sh /bin/entrypoint.sh

RUN apt-get update -y \
    && apt-get install -y libpq5\
    && apt-get clean \
    && groupadd -g 5000 -r wsuser \
    && useradd -r -M -u 5000 -g wsuser wsuser \
    && chown -R wsuser:wsuser /opt/Practica2C_Grupo5 \
    && chmod +x /bin/entrypoint.sh
    

WORKDIR /opt/Practica2C_Grupo5
USER wsuser:wsuser

EXPOSE 8000

ENTRYPOINT ["entrypoint.sh"]
