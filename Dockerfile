FROM python:3.11-alpine

RUN pip install --upgrade pip
RUN pip freeze > requirements.txt
RUN pip install -r requirements.txt

WORKDIR /app

COPY . /app

CMD ["python3", "main.py"]




