from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
# import postgresql


app = FastAPI()

# db = postgresql.open("pq://lpyvrfsbsjkszr:abb2c7e37f871b462c9854d8e4e4c45a7153dcc00f424a6082858b2233233f8d@ec2-3-214-121-14.compute-1.amazonaws.com:5432/d1mgnq9t0iomjf")

with open("emails", "a") as f:
    f.write("")

@app.get("/")
async def root():
    with open("sometext", "a") as f:
        f.write("something\n")

    with open("sometext", "r") as f:
        s = f.read()
        return {"message": s}


@app.get("/emailCollect/{email}")
async def emailCollect(email: str):
    with open("emails", "a") as f:
        f.write(email + "\n")
    return "good"

@app.get("/emails")
async def emails():
    with open("emails", "r") as f:
        emails = f.readlines()
        return {"emails": emails}
