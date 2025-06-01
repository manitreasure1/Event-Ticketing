from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.middleware import add_middleware

class DummyApp(FastAPI):
    def __init__(self):
        super().__init__()
        self._middlewares = []
    def add_middleware(self, middleware_class, **options):
        self._middlewares.append((middleware_class, options))


def test_add_middleware_adds_cors():
    app = DummyApp()
    add_middleware(app)
    cors = [m for m in app._middlewares if m[0] == CORSMiddleware]
    assert cors, "CORS middleware not added"
    cors_opts = cors[0][1]
    assert cors_opts["allow_origins"] == ["http://localhost:5173"]
    assert cors_opts["allow_methods"] == ["*"]
    assert cors_opts["allow_headers"] == ["*"]
    assert cors_opts["allow_credentials"] is True
