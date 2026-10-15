# Practical 11: Model Prediction API

## Output

Train the model, then launch the FastAPI service:

```powershell
python -m mlops_practicals.run_pipeline
uvicorn mlops_practicals.api:app --reload
```

Open `http://127.0.0.1:8000/docs` to exercise the endpoints. Example POST body for `/predict`:

```json
{
  "Marks": 85,
  "Attendance": 90,
  "Study_Hours": 5,
  "Performance_Score": 86.5
}
```

The response contains a predicted class and confidence. Measure latency with repeated requests in Postman or a load-test tool; do not interpret the confidence as calibrated without a separate calibration evaluation. The API checks basic field ranges and returns HTTP 503 if no model artifact exists.