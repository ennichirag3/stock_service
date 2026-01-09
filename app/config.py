from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_PATH: str = "market.db"
    DEFAULT_INTERVAL: str = "1d"

settings = Settings()