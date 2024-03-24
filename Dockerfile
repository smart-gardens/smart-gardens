FROM python:3.12-alpine3.19

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev pkgconfig \
    && apk add --no-cache mariadb-dev

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE smart_garden.settings

WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

EXPOSE 8000
