#Dockerfile
FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir flask openai==0.28 requests

EXPOSE 5000

ENV FLASK_APP=server.py

CMD ["flask", "run", "--host=0.0.0.0"]
