from pydantic import EmailStr
from .. import SESSION
from ..models import User


def get_user(email: EmailStr) -> User:
    with SESSION.begin() as session:
        return User(**session.get_one(User, email).model_dump())
    

def create_user(item: User):
    with SESSION.begin() as session:
        session.add(item)


def update_user(item: User):
    user = get_user(item.email)
    user.sqlmodel_update(item.model_dump(exclude_unset=True))
    create_user(user)


def delete_user(item: User):
    with SESSION.begin() as session:
        session.delete(get_user(item.email))
