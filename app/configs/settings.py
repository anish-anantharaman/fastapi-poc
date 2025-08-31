from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # MySQL database config
    MYSQL_USER: str = ...
    MYSQL_PASSWORD: str = ...
    MYSQL_HOST: str = ...
    MYSQL_PORT: int = ...
    MYSQL_DB: str = ...

    class Config:
        env_file = ".env" # Load variables from .env file
        env_file_encoding = "utf-8"

settings = Settings()

