from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str 
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_HOURS: int
    REFRSH_TOKEN_EXPIRE_DAYS: int


    model_config = SettingsConfigDict(
        env_file = ".env",
        extra='ignore'
    )  


settings = Settings()

