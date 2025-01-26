
from httpx import ASGITransport, AsyncClient
from app.main import app
from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import  SQLModel
from sqlmodel.pool import StaticPool
from app.db.sessions import get_session
import pytest_asyncio

@pytest_asyncio.fixture
async def test_app():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        yield ac

@pytest_asyncio.fixture(name='session')
async def session_fixture():
    engine = create_async_engine(
          "sqlite+aiosqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
    )
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

    async with AsyncSession(engine) as session:
        yield session
        

@pytest_asyncio.fixture(name='client')
async def client_fixture(session: AsyncSession):
    def get_session_overide():
        return session
    app.dependency_overrides[get_session] = get_session_overide
    
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        yield ac
    app.dependency_overrides.clear()
    
