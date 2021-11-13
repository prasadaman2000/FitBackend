from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import psycopg2


app = FastAPI()

conn = psycopg2.connect(
    database="d1mgnq9t0iomjf", user='lpyvrfsbsjkszr', 
  password='abb2c7e37f871b462c9854d8e4e4c45a7153dcc00f424a6082858b2233233f8d', host='ec2-3-214-121-14.compute-1.amazonaws.com', port='5432'
)

conn.autocommit = True
cursor = conn.cursor()

try:
    sql = '''CREATE TABLE emails(email varchar);'''
    cursor.execute(sql)
    conn.commit()
except:
    pass

with open("emails", "a") as f:
    f.write("")

numBad = 0

@app.get("/")
async def root():
    global numBad
    numBad += 1
    return f"cannot get / - you are the {numBad} person to try"


@app.get("/emailCollect/{email}")
async def emailCollect(email: str):
    sql = f"INSERT INTO emails values('{email}')"
    cursor.execute(sql)
    conn.commit()
    return "good"

@app.get("/emails")
async def emails():
    sql = "SELECT email FROM emails;"
    cursor.execute(sql)
    res = cursor.fetchall()
    return res
