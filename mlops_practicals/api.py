"""FastAPI prediction service for the trained demonstration model."""

from pathlib import Path

import joblib
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from mlops_practicals.data import FEATURES

PROJECT_ROOT = Path(__file__).resolve().parents[1]
MODEL_PATH = PROJECT_ROOT / "artifacts" / "student_performance.joblib"
app = FastAPI(title="Student Performance Demo API", version="1.0.0")


class PredictionRequest(BaseModel):
    Marks: float = Field(ge=0, le=100)
    Attendance: float = Field(ge=0, le=100)
    Study_Hours: float = Field(ge=0, le=24)
    Performance_Score: float = Field(ge=0, le=100)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "model_loaded": str(MODEL_PATH.exists()).lower()}


@app.post("/predict")
def predict(request: PredictionRequest) -> dict[str, object]:
    if not MODEL_PATH.exists():
        raise HTTPException(status_code=503, detail="Train the model before starting predictions")
    model = joblib.load(MODEL_PATH)
    row = [[getattr(request, feature) for feature in FEATURES]]
    label = str(model.predict(row)[0])
    probabilities = model.predict_proba(row)[0]
    confidence = float(max(probabilities))
    return {"prediction": label, "confidence": round(confidence, 4)}