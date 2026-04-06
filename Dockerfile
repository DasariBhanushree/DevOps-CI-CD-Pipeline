FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src/ .

RUN cat app.py

CMD ["python", "app.py"]
