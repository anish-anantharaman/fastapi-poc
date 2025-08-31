class BaseAppException(Exception):
    def __init__(self, message: str, status_code: int):
        self.status_code = status_code
        self.message = message
        super().__init__(message)