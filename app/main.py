from fastapi import FastAPI
from datetime import datetime
from app.routers import items
from app.db.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="AKS Production Demo")

VERSION = datetime.utcnow().isoformat()

@app.get("/")
def root():
    return {"message": "Production FastAPI on AKS 🚀"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/version")
def version():
    return {"deployed_at": VERSION}

app.include_router(items.router)
