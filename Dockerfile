FROM python:slim

WORKDIR /app

COPY requirements.txt /app

RUN apt update && apt install ffmpeg libsm6 libxext6  -y
RUN pip install -r requirements.txt

COPY . /app

CMD ["python3", "main.py"]
