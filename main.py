from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles


app = FastAPI()

@app.get("/")
async def root():
    with open("sometext", "a") as f:
        f.write("something\n")

    return {"message": "hello"}
