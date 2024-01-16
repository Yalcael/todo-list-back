from sqlmodel import select

from todo_list.models.tables import Table
from todo_list.models.users import User, UserCreate, UserUpdate


class UserController:
    def __init__(self, session):
        self.session = session

    def get_users(self) -> list[User]:
        return self.session.exec(select(User)).all()

    def get_user_by_id(self, user_id: int) -> User:
        return self.session.exec(select(User).where(User.id == user_id)).one()

    def create_user(self, user_create: UserCreate) -> User:
        new_user = User(
            first_name=user_create.first_name,
            last_name=user_create.last_name,
            email=user_create.email,
            password=user_create.password,
        )
        self.session.add(new_user)
        self.session.commit()
        self.session.refresh(new_user)
        return new_user

    def delete_user(self, user_id: int) -> None:
        user = self.session.exec(select(User).where(User.id == user_id)).one()
        self.session.delete(user)
        self.session.commit()

    def update_user(self, user_id: int, user_update: UserUpdate) -> User:
        user = self.session.exec(select(User).where(User.id == user_id)).one()
        for key, val in user_update.dict(exclude_unset=True).items():
            setattr(user, key, val)
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def get_user_tables(self, user_id) -> list[Table]:
        return self.session.exec(
            select(Table).join(User).where(User.id == user_id)
        ).all()
