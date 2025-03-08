from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware




def add_middleware(app: FastAPI):

    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_methods=["*"],
        allow_headers=["*"],
        allow_credentials=True,
    )
    