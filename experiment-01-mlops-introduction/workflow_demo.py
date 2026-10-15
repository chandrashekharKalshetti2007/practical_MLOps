STAGES = (
    "Problem definition",
    "Data collection and validation",
    "Preprocessing and feature engineering",
    "Model training and evaluation",
    "Versioning and deployment",
    "Monitoring and retraining",
)


def main() -> None:
    for number, stage in enumerate(STAGES, start=1):
        print(f"{number}. {stage}")
    print("Workflow diagram: mlops-lifecycle.mmd")


if __name__ == "__main__":
    main()