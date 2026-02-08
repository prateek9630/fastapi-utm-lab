from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI running in UTM Ubuntu!"}

@app.get("/health")
def health():
    return {"status": "ok"}
