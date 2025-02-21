import pandas as pd
import numpy as np
import sys
import os
import joblib
import argparse
from utils import CategoricalEncoder, FeatureScaler
pd.set_option('future.no_silent_downcasting', True)

# Creating  CLI argument parser
parser = argparse.ArgumentParser()
parser.add_argument('data_path', type=str, help='Path of the test csv file')

# loading models
categorical_encoder = joblib.load('models/categorical_encoder.pkl')
feature_scaler = joblib.load('models/feature_scaler.pkl')
model = joblib.load('models/xgb_classifier.pkl')

required_cols = ['Age', 'Gender', 'Job_Role', 'Industry',
       'Years_of_Experience', 'Work_Location', 'Hours_Worked_Per_Week',
       'Number_of_Virtual_Meetings', 'Work_Life_Balance_Rating',
       'Stress_Level', 'Access_to_Mental_Health_Resources', 'Productivity_Change',
       'Social_Isolation_Rating', 'Satisfaction_with_Remote_Work',
       'Company_Support_for_Remote_Work', 'Physical_Activity', 'Sleep_Quality',
       'Region']

def read_data(path):
    return pd.read_csv(path)

def preprocess(X):
    # check if all required cols are present
    print("Validating the input data...")
    for col in required_cols:
        if col not in X.columns:
            raise Exception("Required Features not present in the data.")
    print("Validation completed.")

    print("Preparing the data...")
    # drop unneccessary columns
    X = X[required_cols]
    print("Data prepared.")

    # categorical encoding
    X = categorical_encoder.transform(X)

    # feature scaling
    X = feature_scaler.transform(X)

    return X

def predict(X):
    print("\nPredictions: ")
    target_mapping = {0: "Burnout", 1:"Depression", 2: "Anxiety"}
    pred = model.predict(X)
    pred = [target_mapping[p] for p in pred]
    return pred

if __name__ == "__main__":
    args = parser.parse_args()
    path = args.data_path
    X = read_data(path)
    X = preprocess(X)
    pred = predict(X)
    print(pred)