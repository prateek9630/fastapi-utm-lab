from fastapi import FastAPI
from app.routers import items

app = FastAPI(title="FastAPI UTM App")

app.include_router(items.router)

@app.get("/")
def root():
    return {
        "message": "CI/CD cycle verified — v6 🚀",
        "timestamp": "test-run-3"
    }

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/version")
def version():
    return {
        "app": "fastapi-utm",
        "version": "v3",
        "ci_cd": "verified"
    }
