import tempfile
import unittest
from pathlib import Path

from mlops_practicals.data import generate_synthetic_records, read_records, validate_records, write_records


class DataTests(unittest.TestCase):
    def test_generated_data_is_reproducible_and_valid(self):
        first = generate_synthetic_records(count=20, seed=7)
        second = generate_synthetic_records(count=20, seed=7)
        self.assertEqual(first, second)
        self.assertEqual(validate_records(first)["rows"], 20)

    def test_csv_round_trip(self):
        with tempfile.TemporaryDirectory() as directory:
            path = write_records(Path(directory) / "students.csv", generate_synthetic_records(4))
            self.assertEqual(read_records(path), generate_synthetic_records(4))

    def test_missing_values_are_rejected(self):
        record = generate_synthetic_records(2)[0]
        record["Attendance"] = ""
        with self.assertRaisesRegex(ValueError, "missing values"):
            validate_records([record])


if __name__ == "__main__":
    unittest.main()