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

version = "v1"

app = FastAPI(
    title="Event-Ticketing",
    description="Sports Events Ticketing WebApp",
    lifespan=life_span,
    version=version
    )

app.include_router(auth.router, prefix=f"/auth/{version}", tags=["Authentication"])
app.include_router(user.router, prefix=f"/users/{version}", tags=["Users"])
app.include_router(event.router, prefix=f"/event/{version}", tags=["Events"])
app.include_router(organization.router, prefix=f"/users/{version}", tags=["Organization"])
