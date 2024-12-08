from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    MONGODB_URL: str = "mongodb://root:rootpassword@localhost:27017"
    DATABASE_NAME: str = "forms_db"

    class Config:
        env_file = ".env"


settings = Settings()
