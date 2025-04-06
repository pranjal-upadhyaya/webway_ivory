from pydantic_settings import BaseSettings

class AppConfig(BaseSettings):
    ebony_base_url: str
    app_host: str
    app_port: int
    app_env: str
    log_level: str = "INFO"  # Default log level

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False

app_config = AppConfig()