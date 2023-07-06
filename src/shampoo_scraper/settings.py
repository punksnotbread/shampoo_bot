from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    BOT_TOKEN: str = ""
    CHAT_ID: str = ""
    SEARCH_TYPES: str = '["camelia", "eurovaistine", "gintarinevaistine"]'
    QUERIES: str = "[]"
    ENVIRONMENT: str = "local"
    PARALEL_JOB_COUNT: int = 3

    class Config:
        env_prefix = ""
        case_sentive = False
        env_file = ".env"
        env_file_encoding = "utf-8"
