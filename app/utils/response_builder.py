from typing import Optional, Any
from fastapi import Request
from pydantic import BaseModel


class ResponseBuilder(BaseModel):
    status_code: int
    status_message: str
    error_message: Optional[str] = ""
    response_data: Optional[Any] = None
    request_id: Optional[str] = None

def build_response(status_code: int, status_message: str,error_message: Optional[str] = "",
                   response_data: Optional[Any] = None, request: Optional[Request] = None) -> ResponseBuilder:
    request_id = getattr(request.state, "request_id", None) if request else None
    return ResponseBuilder(
        status_code=status_code,
        status_message=status_message,
        error_message=error_message,
        response_data=response_data,
        request_id=request_id
    )