from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()

model = joblib.load("models/model.pkl")

@app.get("/")
def root():
    return {"message": "House Price Prediction API is running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/predict")
def predict(
    sqft: float,
    bedrooms: int,
    bathrooms: float,
    age_years: float,
    garage: float,
    location_score: float
):
    data = np.array([[
        sqft,
        bedrooms,
        bathrooms,
        age_years,
        garage,
        location_score
    ]])

    prediction = model.predict(data)[0]

    return {"predicted_price": float(prediction)}