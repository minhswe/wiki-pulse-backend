from fastapi import FastAPI

app = FastAPI(title = "WikiPulse API")

@app.get("/")
async def root():
    return {
        "message": "Welcome to WikiPulse API"
    }

@app.get("/health")
async def health():
    return {
        "status": "UP"
    }