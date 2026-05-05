# Smart AI Chatbot DevOps Project

## Features
- FastAPI chatbot
- Beautiful full-screen UI
- Docker containerization
- Prometheus metrics
- Grafana monitoring
- GitHub Actions CI
- Kubernetes deployment files

## Run locally
```bash
python -m uvicorn app.main:app --reload
```

## Run with Docker Compose
```bash
docker compose up --build
```

## URLs
- App: http://localhost:8000
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000
- Health: http://localhost:8000/health
- Metrics: http://localhost:8000/metrics