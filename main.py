from fastapi import FastAPI
from dotenv import load_dotenv
import os
from services.parseBook import fetch_parse_book

app = FastAPI()
load_dotenv()

@app.get("/")
async def root():
    book_uri = os.getenv("BOOK_URI")
    fetch_parse_book(book_uri)


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}