from fastapi import Depends, FastAPI
from app.api.endpoints import auth, user, organization, event, admin, ticket
from contextlib import asynccontextmanager
from app.db.sessions import init_db
from app.api.dependencies import AccessTokenBearer, RoleChecker
from typing import Final
from app.core.middleware import add_middleware


access_token_bearer = AccessTokenBearer()
role_checker = RoleChecker(['admin'])


@asynccontextmanager
async def life_span(app: FastAPI):
    print("Starting Application")
    await init_db()
    yield
    print("Ending Application")

VERSION: Final = "v1"

app = FastAPI(
    title="Event-Ticketing",
    description="Sports Events Ticketing WebApp",
    version=VERSION, 
    )

add_middleware(app)

app.include_router(auth.router, prefix=f"/auth/{VERSION}", tags=["Authentication"])
app.include_router(user.router, prefix=f"/users/{VERSION}", tags=["Users"])
app.include_router(event.router, prefix=f"/events/{VERSION}", tags=["Events"])
app.include_router(ticket.router, prefix=f"/tickets/{VERSION}", tags=["Tickets"])
app.include_router(organization.router, prefix=f"/organizations/{VERSION}", tags=["Organization"])
app.include_router(admin.router, prefix=f"/admin/{VERSION}", tags=["Admin"])
# app.include_router(admin.router, prefix=f"/admin/{VERSION}", tags=["Admin"], dependencies=[Depends(access_token_bearer), Depends(role_checker)])
