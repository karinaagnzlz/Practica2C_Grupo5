FROM python:3.12-slim as build

RUN apt-get update -y \
    && apt-get install -y build-essential libpq-dev git \
    && pip install virtualenv \
    && virtualenv /opt/practica2c_grupo5/venv \
    && . /opt/practica2c_grupo5/venv/bin/activate \
    && pip install gunicorn

COPY . /practica2c_grupo5

WORKDIR /practica2c_grupo5

RUN . /opt/practica2c_grupo5/venv/bin/activate \
    && pip install .

FROM python:3.12-slim

COPY --from=build /opt/practica2c_grupo5 /opt/practica2c_grupo5
COPY entrypoint.sh /bin/entrypoint.sh

RUN apt-get update -y \
    && apt-get install -y libpq5\
    && apt-get clean \
    && groupadd -g 5000 -r wsuser \
    && useradd -r -M -u 5000 -g wsuser wsuser \
    && chown -R wsuser:wsuser /opt/practica2c_grupo5 \
    && chmod +x /bin/entrypoint.sh
    

WORKDIR /opt/practica2c_grupo5
USER wsuser:wsuser

EXPOSE 8000

ENTRYPOINT ["entrypoint.sh"]
