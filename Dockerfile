FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY mlops_practicals ./mlops_practicals
COPY experiment-08-testing ./experiment-08-testing
RUN python -m mlops_practicals.run_pipeline

EXPOSE 8000
CMD ["uvicorn", "mlops_practicals.api:app", "--host", "0.0.0.0", "--port", "8000"]