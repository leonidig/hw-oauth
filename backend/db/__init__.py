from sqlmodel import create_engine, SQLModel
from sqlalchemy.orm import sessionmaker



ENGINE = create_engine("sqlite:///mydb.db", echo=True)
SESSION = sessionmaker(bind=ENGINE)


def migrate():
    SQLModel.metadata.drop_all(ENGINE)
    SQLModel.metadata.create_all(ENGINE)




from .models import User, Token, TokenData
from .helpers import create_user, get_user, update_user, delete_user


