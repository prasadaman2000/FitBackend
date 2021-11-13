from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles


app = FastAPI()

@app.get("/")
async def root():
    with open("sometext", "a") as f:
        f.write("something\n")

    with open("sometext", "r") as f:
        s = f.read()
        return {"message": s}
