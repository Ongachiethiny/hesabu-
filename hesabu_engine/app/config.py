from pydantic import BaseSettings


class Settings(BaseSettings):
    project_name: str = "hesabu_engine"
    database_url: str = "sqlite:///./hesabu_engine.db"

    class Config:
        env_file = ".env"


settings = Settings()
