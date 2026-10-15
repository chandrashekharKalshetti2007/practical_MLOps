import tempfile
import unittest
from pathlib import Path

from mlops_practicals.data import generate_synthetic_records
from mlops_practicals.feature_store import materialize_features


class FeatureStoreTests(unittest.TestCase):
    def test_offline_and_online_features_are_materialized(self):
        with tempfile.TemporaryDirectory() as directory:
            result = materialize_features(generate_synthetic_records(3), Path(directory))
            self.assertEqual(result["entities_ingested"], 3)
            self.assertTrue((Path(directory) / result["offline_store"]).exists())
            self.assertTrue((Path(directory) / result["online_store"]).exists())


if __name__ == "__main__":
    unittest.main()