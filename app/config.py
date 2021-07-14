import os

from pydantic import BaseSettings
from dotenv import load_dotenv

from pathlib import Path
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


class Config(BaseSettings):
    API_NAME: str = os.getenv("API_NAME")
    API_DESCRIPTION: str = os.getenv("API_DESCRIPTION")
    API_VERSION: str = os.getenv("API_VERSION")
    DEBUG: bool = os.getenv("API_DEBUG_MODE")
    APP_HOST: str = os.getenv("APP_HOST")
    APP_PORT: int = os.getenv("APP_PORT")
    ENV: str = os.getenv("ENV_STATE")


class DevelopmentConfig(Config):
    """Development configurations."""

    # Database environment
    POSTGRES_USER : str = os.getenv("DEV_POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("DEV_POSTGRES_PASSWORD")
    POSTGRES_DB : str = os.getenv("DEV_POSTGRES_DB","tdd")
    POSTGRES_PORT : str = os.getenv("DEV_POSTGRES_PORT",5432) # default postgres port is 5432
    POSTGRES_SERVER : str = os.getenv("DEV_POSTGRES_SERVER","localhost")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

class ProductionConfig(Config):
    """Production configurations."""

    POSTGRES_USER : str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_DB : str = os.getenv("POSTGRES_DB","tdd")
    POSTGRES_PORT : str = os.getenv("POSTGRES_PORT",5432) # default postgres port is 5432
    POSTGRES_SERVER : str = os.getenv("POSTGRES_SERVER","localhost")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"


def get_config():
    env = os.getenv("ENV_STATE")
    config_type = {
        "dev": DevelopmentConfig(),
        "prod": ProductionConfig(),
    }
    return config_type[env]


config = get_config()
