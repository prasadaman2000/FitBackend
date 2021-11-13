from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "hello"}
