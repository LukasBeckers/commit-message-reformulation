#Dockerfile
FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir Flask==3.0.3 openai==0.28 requests==2.32.3

EXPOSE 5000

ENV FLASK_APP=server.py

CMD ["flask", "run", "--host=0.0.0.0"]
