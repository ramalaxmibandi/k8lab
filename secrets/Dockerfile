FROM python:3.8-slim-buster

WORKDIR /app

ADD app.py app.py

COPY requirements.txt requirements.txt
RUN apt-get install python3-dev default-libmysqlclient-dev build-essential
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]
