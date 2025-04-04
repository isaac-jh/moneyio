import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import api_gateway
from utils.exceptions import register_exception
from utils.settings import get_settings

from uvicorn.config import LOGGING_CONFIG

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_gateway.router)
register_exception(app)

if __name__ == "__main__":

    # LOG FORMATTING
    LOGGING_CONFIG["formatters"]["default"]["fmt"] = get_settings().logfmt
    LOGGING_CONFIG["formatters"]["access"]["fmt"] = get_settings().logfmt_access

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=get_settings().uvicorn_reload,
    )