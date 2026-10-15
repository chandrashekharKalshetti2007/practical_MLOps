import asyncio
import unittest
from pathlib import Path

import httpx

from mlops_practicals.api import app
from mlops_practicals.data import generate_synthetic_records
from mlops_practicals.training import train_and_evaluate

PROJECT_ROOT = Path(__file__).resolve().parents[2]


class TrainingAndApiTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = train_and_evaluate(generate_synthetic_records(), PROJECT_ROOT)

    @staticmethod
    async def request(path, body):
        transport = httpx.ASGITransport(app=app)
        async with httpx.AsyncClient(transport=transport, base_url="http://test") as client:
            return await client.post(path, json=body)

    def test_model_comparison_and_artifact(self):
        self.assertEqual(self.result["test_records"], 60)
        self.assertEqual(len(self.result["models"]), 3)
        self.assertTrue((PROJECT_ROOT / self.result["artifact"]).exists())

    def test_prediction_api(self):
        response = asyncio.run(self.request("/predict", {
            "Marks": 85,
            "Attendance": 90,
            "Study_Hours": 5,
            "Performance_Score": 86.5,
        }))
        self.assertEqual(response.status_code, 200)
        self.assertIn(response.json()["prediction"], {"Good", "Needs Improvement"})
        self.assertGreaterEqual(response.json()["confidence"], 0)

    def test_invalid_prediction_input_is_rejected(self):
        response = asyncio.run(self.request("/predict", {
            "Marks": 150,
            "Attendance": 90,
            "Study_Hours": 5,
            "Performance_Score": 86.5,
        }))
        self.assertEqual(response.status_code, 422)


if __name__ == "__main__":
    unittest.main()