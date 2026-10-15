# Practical 10: Docker

## Output

The root `Dockerfile` installs core dependencies, trains the demo model inside the image, and starts the prediction API. Build and run after installing Docker Desktop:

```powershell
docker build -t student-mlops-demo .
docker run --rm -p 8000:8000 student-mlops-demo
```

Check `http://localhost:8000/health`. The Docker engine is unavailable in the current environment, so image build/container output must be captured after Docker is installed.