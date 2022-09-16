from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import mlflow
from prefect import flow

mlflow.set_experiment("Test2")

@flow
def train():
    mlflow.sklearn.autolog()

    iris = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

    features = ["sepal_length","sepal_width", "petal_length", "petal_width"]
    target = ["species"]

    X_train, X_test, y_train, y_test = train_test_split(iris[features], iris[target].values, test_size=0.33)

    forest = RandomForestClassifier()

    with mlflow.start_run() as run:
        forest.fit(X_train, y_train)

if __name__ == "__main__":
    train()