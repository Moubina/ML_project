import mlflow
import mlflow.sklearn
import joblib
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np
import os


X = pd.read_csv("C:/Users/pharv/Documents/GitHub/MLFlow_prj/data/processed/x_balanced.csv")


y = pd.read_csv("C:/Users/pharv/Documents/GitHub/MLFlow_prj/data/processed/engineered_train_data.csv")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
rf_model = joblib.load("C:/Users/pharv/Documents/GitHub/MLFlow_prj/models/rf_model.pkl")
y_pred = rf_model.predict(X_test)



# Initialiser une nouvelle session MLFlow
with mlflow.start_run():
    # Charger le modèle enregistré avec joblib

    # Logger les paramètres du modèle
    mlflow.log_param("model_type", "Random Forest")
    
   
    # Evaluer le modèle sur les données de test
    accuracy = rf_model.score(X_test, y_test)
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_absolute_error(y_test, y_pred))

    # Logger les métriques du modèle
    mlflow.log_metric("accuracy", accuracy)
    mlflow.log_metric("r2", r2)
    mlflow.log_metric("mae", mae)
    mlflow.log_metric("rmse", rmse)






    mlflow.sklearn.log_model(rf_model, "rf_model")


   
