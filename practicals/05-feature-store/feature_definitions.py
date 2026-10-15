from feast import Entity, FeatureView, Field, FileSource
from feast.types import Float32, String

student = Entity(name="student", join_keys=["student_id"])

student_source = FileSource(
    name="student_performance_source",
    path="data/student_features.parquet",
    timestamp_field="event_timestamp",
)

student_performance = FeatureView(
    name="student_performance",
    entities=[student],
    schema=[
        Field(name="Marks", dtype=Float32),
        Field(name="Attendance", dtype=Float32),
        Field(name="Study_Hours", dtype=Float32),
        Field(name="Performance_Score", dtype=Float32),
    ],
    source=student_source,
)