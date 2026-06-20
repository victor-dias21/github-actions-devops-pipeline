from fastapi import FastAPI

app = FastAPI(
    title="DevOps Pipeline Demo",
    description="API simples para demonstrar pipeline CI/CD com GitHub Actions.",
    version="0.1.0",
)


@app.get("/")
def read_root() -> dict[str, str]:
    return {
        "service": "github-actions-devops-pipeline",
        "status": "ok",
    }


@app.get("/health")
def healthcheck() -> dict[str, str]:
    return {"status": "healthy"}
