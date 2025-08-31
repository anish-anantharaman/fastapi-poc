from fastapi import Request, FastAPI
from fastapi.responses import JSONResponse

from app.configs.logging_config import logger
from app.exceptions.base_exception import BaseAppException
from app.utils.constants import StatusMessage
from app.utils.project_util import get_request_id


# Exception handler for all exceptions
def register_exception_handlers(app: FastAPI):
    @app.exception_handler(BaseAppException)
    async def app_exception_handler(request: Request, exc: BaseAppException):
        logger.error(f"Request ID: {get_request_id(request)} | Unexpected error: {exc}")
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "statusCode": exc.status_code,
                "statusMessage": StatusMessage.FAILURE,
                "errorMessage": exc.message,
                "request_id": get_request_id(request)
            }
        )

    @app.exception_handler(Exception)
    async def general_exception_handler(request: Request, exc: Exception):
        logger.error(f"Request ID: {get_request_id(request)} | Unexpected error: {exc}")
        return JSONResponse(
            status_code=500,
            content={
                "statusCode": 500,
                "statusMessage": StatusMessage.FAILURE,
                "errorMessage": f"Internal Server Error: {str(exc)}",
                "request_id": get_request_id(request)
            }
        )