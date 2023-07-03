from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    BOT_TOKEN: str = ""
    CHAT_ID: str = ""

    class Config:
        env_prefix = ""
        case_sentive = False
        env_file = ".env"
        env_file_encoding = "utf-8"
