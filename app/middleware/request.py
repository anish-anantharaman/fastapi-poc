import uuid
from fastapi import Request

async def add_request_id(request: Request, call_next):
    """
    Middleware to attach a unique request ID to each request.
    The ID is available via `request.state.request_id`.
    """
    request.state.request_id = str(uuid.uuid4())
    response = await call_next(request)
    response.headers["X-Request-ID"] = request.state.request_id
    return response
