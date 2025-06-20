from pydantic_settings import BaseSettings, SettingsConfigDict


class EnvConfig(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str 
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_HOURS: int
    REFRESH_TOKEN_EXPIRE_DAYS: int


    model_config = SettingsConfigDict(
        env_file = "../.env",
        extra='ignore'
    )




