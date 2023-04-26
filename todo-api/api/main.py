"""Main file of the FastAPI simple app."""
import os

from fastapi import APIRouter, FastAPI
from mangum import Mangum

from api import __version__

router = APIRouter()


@router.get("/hello")
def hello():
    """GET /hello endpoint."""
    return {"message": "Hello data from FastAPI"}


@router.get("/")
def root():
    """GET / endpoint."""
    return {"message": f"API version: {__version__}"}


app = FastAPI(
    title="fastapi-react-serverless",
    version=__version__,
    openapi_url="/openapi.json",
    docs_url="/docs",
)
app.include_router(router)

handler = Mangum(app)  # handler for deploy FastAPI to lambdas
