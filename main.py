from typing import Optional
from fastapi import FastAPI
import datetime
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    #"http://localhost.tiangolo.com",
    #"https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def now():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')