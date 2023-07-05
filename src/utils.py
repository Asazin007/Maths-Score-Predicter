# Python Utils is a collection of small Python functions and classes which make common patterns shorter and easier. It is by no means a complete collection but it has served me quite a bit in the past and I will keep extending it.
import os
import sys
import dill
import numpy as np
from sklearn.metrics import r2_score
import pandas as pd
from catboost import CatBoostRegressor
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor,
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from src.exception import CustomException

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)


def evaluate_models(X_train, y_train,X_test,y_test,models):
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
                      
            
            model.fit(X_train,y_train)

            #model.fit(X_train, y_train)  # Train model

            y_train_predict=model.predict(X_train)
            y_test_predict=model.predict(X_test)
            
            train_model_score= r2_score(y_train,y_train_predict)
            test_model_score=r2_score(y_test , y_test_predict)
            report[list(models.keys())[i]]= test_model_score
        return report

    except Exception as e:
        raise CustomException(e, sys)