from fastapi import FastAPI

app = FastAPI()


@app.get("/health/live")
def health_live():
    return {"status": "ok"}