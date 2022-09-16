FROM continuumio/miniconda3

RUN mkdir /training
WORKDIR /training

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN prefect config set PREFECT_API_URL=http://host.docker.internal:4200/api
ENV MLFLOW_TRACKING_URI=http://mlflow:5000
CMD ["sh","-c","prefect orion start --host 0.0.0.0 & sleep 25 && prefect deployment apply train-deployment.yaml & sleep 15 && prefect agent start -q 'default'"]