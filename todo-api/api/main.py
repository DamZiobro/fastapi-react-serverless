"""Implementation of Use Cases based on the Clean Architecture principles"""

from fastapi import FastAPI
from mangum import Mangum

from api import __version__
from api.routes.todo import router as todo_router


app = FastAPI(
    title="fastapi-react-serverless",
    version=__version__,
    openapi_url="/openapi.json",
    docs_url="/docs",
)
app.include_router(todo_router)

handler = Mangum(app)  # handler for deploy FastAPI to lambdas
