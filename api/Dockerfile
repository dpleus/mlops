FROM continuumio/miniconda3

RUN mkdir /api
WORKDIR /api

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV MLFLOW_TRACKING_URI=http://mlflow:5000

EXPOSE 8000
CMD ["sh", "-c", "uvicorn api:app --port 8086 --host 0.0.0.0"]