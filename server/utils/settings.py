import os
from functools import cache

from pydantic import BaseSettings


class PostgresDBSettings(BaseSettings):
    db_url: str
    db_port: int
    db_username: str
    db_password: str
    db_database: str


class Settings(PostgresDBSettings):
    appname: str = "moneyio"
    loglevel: str = "INFO"
    logfmt: str = "%(asctime)s %(levelname)-8s %(name)-12s: %(message)s"
    logfmt_access: str = "%(asctime)s %(levelname)-8s %(name)-12s: %(message)s"
    uvicorn_reload: bool = False


# settings 값을 여러번 반환해주기 때문에 cache 사용
@cache
def get_settings():
    envfile = os.environ.get("ENVFILE")
    if envfile is not None:
        return Settings(_env_file=envfile)

    return Settings()
