# config.py
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    SECRET_KEY: str = Field(..., description="Secret key for signing cookies")
    SESSION_MAX_AGE: int = 60

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()  # type: ignore[arg-type]
if not settings.SECRET_KEY:
    raise ValueError("SECRET_KEY must be set in .env")
