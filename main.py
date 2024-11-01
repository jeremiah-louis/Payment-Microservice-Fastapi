from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from redis_om import get_redis_connection, HashModel

app = FastAPI()
redis_connection = get_redis_connection(
    host="localhost",
    port=6379,
    decode_responses=True,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_headers=["*"],
    allow_methods=["*"],
)
