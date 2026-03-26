FROM python:3.8-slim

WORKDIR /app

ADD . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]