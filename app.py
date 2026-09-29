from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import joblib

app = FastAPI(title="House Price Prediction API")

model = joblib.load("models/model.pkl")

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def home():
    return FileResponse("static/index.html")


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
    data = [[
        sqft,
        bedrooms,
        bathrooms,
        age_years,
        garage,
        location_score
    ]]

    prediction = model.predict(data)[0]

    return {
        "predicted_price": float(prediction)
    }