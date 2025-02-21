from sklearn.base import TransformerMixin, BaseEstimator
from sklearn.preprocessing import OrdinalEncoder, StandardScaler
import pandas as pd
import numpy as np

class CategoricalEncoder(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.ord_cols = ["Work_Location", "Industry", "Job_Role", "Gender"]
        self.mappings = {
            "Stress_Level": {"High": 3, "Medium":2, "Low": 0},
            "Access_to_Mental_Health_Resources": {"Yes": 1, "No": 0},
            "Productivity_Change": {"Decrease": -1, "No Change": 0, "Increase": 1},
            "Satisfaction_with_Remote_Work": {"Unsatisfied": -1, "Neutral": 0, "Satisfied": 1},
            "Physical_Activity": {"Weekly": 1, "Daily": 2},
            "Sleep_Quality": {"Poor": -1, "Average": 0, "Good": 1},
            "Region": {"Africa": -2, "South America": -1, "Asia": 0, "Oceania": 2, "North America": 1, "Europe": 2}
        }
        self.ord_encoder = OrdinalEncoder(handle_unknown="use_encoded_value", unknown_value=-1)
  
    def _custom_encoder(self, df):
        df = df.copy()
        for col in self.mappings.keys():
            df.loc[:, col] = df[col].replace(self.mappings[col])
        
        return df
    
    def fit(self, df):
        self.ord_encoder.fit(df[self.ord_cols])
    
    def transform(self, df):
        df = df.copy()
        df[self.ord_cols] = self.ord_encoder.transform(df[self.ord_cols])
        df = self._custom_encoder(df)
        return df

class FeatureScaler(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.std_scaler = StandardScaler()
    
    def fit(self, df):
        self.std_scaler.fit(df)

    def transform(self, df):
        X = self.std_scaler.transform(df)
        df = pd.DataFrame(X, columns=df.columns)
        return df