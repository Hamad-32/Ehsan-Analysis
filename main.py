from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
import numpy as np

app = FastAPI()

@app.get("/")
def root():
    return "Welcome To Ehsan"

# Load the scaler and DBSCAN core points data from the file
scaler = joblib.load('model/scaler.joblib')
# The file is assumed to contain a dictionary with keys: 'components', 'labels', and 'eps'
dbscan_data = joblib.load('model/dbscan_core_points.joblib')
core_points = dbscan_data["components"]  # Core points (numpy array)
core_labels = dbscan_data["labels"]        # Labels for the core points
epsilon = dbscan_data["eps"]               # The epsilon value used in DBSCAN

def dbscan_predict(core_points, core_labels, epsilon, new_points):
    """
    For each new point, compute its Euclidean distance to all saved core points.
    If any distance is less than or equal to epsilon, assign the label of the closest core point.
    Otherwise, return -1 (noise).
    """
    labels = []
    for point in new_points:
        distances = np.linalg.norm(core_points - point, axis=1)
        if np.any(distances <= epsilon):
            closest_index = np.argmin(distances)
            labels.append(core_labels[closest_index])
        else:
            labels.append(-1)  # Mark as noise
    return np.array(labels)

class InputFeatures(BaseModel):
    Number_of_donations: int
    Beneficiaries: int
    Location_encoded: int
    Hijri_Month: int

def preprocessing(input_features: InputFeatures):
    data = {
        'Number of donations': input_features.Number_of_donations,  
        'Beneficiaries': input_features.Beneficiaries,  
        'Location_encoded': input_features.Location_encoded,  
        'Hijri_Month': input_features.Hijri_Month  
    }
    df = pd.DataFrame([data])
    df_scaled = scaler.transform(df)  # Apply scaling
    return df_scaled

@app.post("/predict")
def predict_cluster(input_features: InputFeatures):
    try:
        processed_data = preprocessing(input_features)  # Shape (1, n_features)
        prediction = dbscan_predict(core_points, core_labels, epsilon, processed_data)
        return {"cluster": int(prediction[0])}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

