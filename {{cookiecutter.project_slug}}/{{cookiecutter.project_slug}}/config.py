from functools import lru_cache
from typing import Literal

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

ENV_FILE_PATH = "config/.env"


class Settings(BaseSettings):
    input_connector: Literal["python", "{{cookiecutter.prod_input}}"]
    autocommit_duration_ms: int
    pathway_threads: int

    {{cookiecutter.prod_input}}_bootstrap_servers: str
    {{cookiecutter.prod_input}}_group_id: str
    {{cookiecutter.prod_input}}_session_timeout_ms: str
    {{cookiecutter.prod_input}}_topic: str

    class Config:
        case_sensitive = False
        env_file = ENV_FILE_PATH


@lru_cache()
def get_settings():
    load_dotenv(ENV_FILE_PATH)  # make sure variables in .env file are propagated to environment
    return Settings()
