from fastapi import status
from app.exceptions.base_exception import BaseAppException


class BadRequestException(BaseAppException):
    def __init__(self, message: str):
        super().__init__(message, status.HTTP_400_BAD_REQUEST)

class NotFoundException(BaseAppException):
    def __init__(self, message: str):
        super().__init__(message, status.HTTP_404_NOT_FOUND)