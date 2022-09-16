FROM continuumio/miniconda3

WORKDIR /mlruns

COPY requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["sh", "-c", "mlflow server --backend-store-uri sqlite:////mlruns/mlflow.db --default-artifact-root file:///mlruns --host=0.0.0.0"]