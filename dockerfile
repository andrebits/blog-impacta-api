FROM python:3.13-alpine

WORKDIR /app

COPY ./requirements.txt ./

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000

RUN chmod +x /app/docker-entrypoint.sh

ENTRYPOINT ["/app/docker-entrypoint.sh"]

