from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    client_url: str
    client_key: str

    class Config:
        env_file = ".env"

settings = Settings()