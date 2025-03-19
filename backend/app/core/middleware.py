from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware




def add_middleware(app: FastAPI):
    origin = [
        "http://localhost:5173",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origin,
        allow_methods=["*"],
        allow_headers=["*"],
        allow_credentials=True,
    )
    