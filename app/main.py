from sys import version
from fastapi import FastAPI
from api.endpoints import auth, user, organization, event
from contextlib import asynccontextmanager
from db.sessions import init_db


@asynccontextmanager
async def life_span(app: FastAPI):
    print("Starting Application")
    await init_db()
    yield
    print("Ending Application")

version = "0.0.1"

app = FastAPI(
    title="Event-Ticketing",
    description="Sports Events Ticketing WebApp",
    lifespan=life_span,
    version=version
    )

app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(event.router, prefix="/auth", tags=["Events"])
app.include_router(organization.router, prefix="/users", tags=["Organization"])
