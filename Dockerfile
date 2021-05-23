FROM python:3.8-alpine

COPY . /src/

WORKDIR /src

RUN pip install -r requirements.txt && python manage.py migrate

EXPOSE 8000

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]

