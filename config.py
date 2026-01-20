import os
#конфиг взял с бота
class Config:
    def __init__(self):
        self.POSTGRES = {
            "user": os.getenv("POSTGRES_USER", "user"),
            "password": os.getenv("POSTGRES_PASSWORD", "password"),
            "host": os.getenv("POSTGRES_HOST", "localhost"),
            "port": os.getenv("POSTGRES_INNER_PORT", "5432"),
            "db": os.getenv("POSTGRES_DB", "db"),
        }

        self.DATABASE_URL = (
            f"postgresql+psycopg2://{self.POSTGRES['user']}:{self.POSTGRES['password']}"
            f"@{self.POSTGRES['host']}:{self.POSTGRES['port']}/{self.POSTGRES['db']}"
        )

config = Config()