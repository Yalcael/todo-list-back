from sqlmodel import Session, select

from todo_list.controllers.users import UserController
from todo_list.models.users import User, UserCreate


def test_create_user(user_controller: UserController, session: Session):
    created_user = user_controller.create_user(
        UserCreate(
            first_name="Sivir",
            last_name="Shurima",
            email="vincent.l@admin.com",
            password="vl93*",
        )
    )
    users = session.exec(select(User)).all()
    assert len(users) == 1
    assert created_user.first_name == users[0].first_name
    assert created_user.last_name == users[0].last_name
    assert created_user.email == users[0].email
    assert created_user.password == users[0].password
