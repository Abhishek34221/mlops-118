from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import joblib

app = FastAPI(title="House Price Prediction API")

model = joblib.load("models/model.pkl")

app.mount("/static", StaticFiles(directory="static"), name="static")


class PredictionRequest(BaseModel):
    sqft: float
    bedrooms: int
    bathrooms: float
    age_years: float
    garage: float
    location_score: float


@app.get("/")
def home():
    return FileResponse("static/index.html")


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/predict")
def predict(data: PredictionRequest):

    values = [[
        data.sqft,
        data.bedrooms,
        data.bathrooms,
        data.age_years,
        data.garage,
        data.location_score
    ]]

    prediction = model.predict(values)[0]

    return {
        "predicted_price": float(prediction)
    }