from pydantic_settings import BaseSettings

class AppConfig(BaseSettings):
    ebony_app_port: int
    ebony_app_host: str
    app_host: str
    app_port: int
    app_env: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False

app_config = AppConfig()