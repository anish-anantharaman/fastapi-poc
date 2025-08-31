from fastapi import FastAPI

from app.exceptions.handler import register_exception_handlers
from app.middleware.request import add_request_id
from app.routers.v1.api import router as v1_router

app = FastAPI()

# Register middleware
app.middleware("http")(add_request_id)

# Register exception handler
register_exception_handlers(app)

app.include_router(v1_router)