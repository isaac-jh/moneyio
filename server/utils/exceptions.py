from fastapi import FastAPI, Request, status
from fastapi.exceptions import HTTPException, RequestValidationError
from fastapi.responses import JSONResponse


class BaseException(HTTPException):
    def __init__(self, status_code: str, detail: str):
        self.status_code = status_code
        self.detail = detail


class InternalServerException(BaseException):
    def __init__(self, detail: str):
        super().__init__(status_code=500, detail=detail)


class BadRequestException(BaseException):
    def __init__(self, detail: str):
        super().__init__(status_code=400, detail=detail)


class UnauthorizedException(BaseException):
    def __init__(self, detail: str):
        super().__init__(status_code=401, detail=detail)


class ForbiddenException(BaseException):
    def __init__(self, detail: str):
        super().__init__(status_code=403, detail=detail)


class NoDataException(BaseException):
    def __init__(self, detail: str):
        super().__init__(status_code=404, detail=detail)


class DuplicatedException(BaseException):
    def __init__(self, name: str):
        super().__init__(status_code=409, detail=f"{name} is duplicated")


def register_exception(app: FastAPI):
    @app.exception_handler(RequestValidationError)
    async def validation_error_handler(request: Request, exc: RequestValidationError):
        exc_str = f"{exc}".replace("\n", " ").replace("   ", " ")
        return JSONResponse(
            content={"status_code": 422, "detail": exc_str},
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        )
