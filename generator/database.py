#https://docs.sqlalchemy.org/en/20/orm/session_basics.html

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import config

engine = create_engine(config.DATABASE_URL, echo=False)

Session = sessionmaker(engine)