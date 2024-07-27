
FROM python:3.11-slim

RUN mkdir /bot_app

WORKDIR /bot_app

COPY requirements.txt .

RUN pip install -v -r requirements.txt

COPY . .

CMD ["python", "main.py"]