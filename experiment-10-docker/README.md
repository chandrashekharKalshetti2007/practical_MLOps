# Experiment 10 - Containerization with Docker

## Aim
Package the trained model and prediction service into a reproducible container image.

## Requirements
- Docker Desktop/Engine installed and running
- Core dependencies from `requirements.txt`

## Procedure
1. From the repository root, build with `docker build -t student-mlops-demo .`.
2. Run with `docker run --rm -p 8000:8000 student-mlops-demo`.
3. Check `http://localhost:8000/health` and exercise `/predict`.

## Captured result
Docker was not available in the captured environment. The Dockerfile and commands are included, but no image build, startup, or health check is claimed; see [`OUTPUT.txt`](./OUTPUT.txt).

## Viva questions
1. What belongs in a Docker image, and what should be mounted or externalized?
2. Why pin and minimize runtime dependencies?
3. How would you reduce image size and address model artifact updates?

## Concept summary
Containers make the application runtime and its dependencies portable across environments.

## Outcome summary
The container build definition is prepared; runtime validation requires Docker Engine.