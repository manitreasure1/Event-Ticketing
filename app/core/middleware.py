from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from fastapi.middleware.trustedhost import TrustedHostMiddleware
# from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware


def add_middleware(app: FastAPI):

    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_methods=["*"],
        allow_headers=["*"],
        allow_credentials=True,
    )
    # app.add_middleware(TrustedHostMiddleware, allowed_hosts=[''])
    # ! warning: this allow only https request
    # app.add_middleware(HTTPSRedirectMiddleware)