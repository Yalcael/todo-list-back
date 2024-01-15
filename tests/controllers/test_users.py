from datetime import datetime

from faker import Faker
from freezegun import freeze_time
from sqlmodel import Session, select

from todo_list.controllers.tables import TableController
from todo_list.controllers.users import UserController
from todo_list.models.tables import TableCreate
from todo_list.models.users import User, UserCreate, UserUpdate


def test_create_user(
    user_controller: UserController, session: Session, faker: Faker
) -> None:
    with freeze_time(faker.date_time()):
        now = datetime.now()
        created_user = user_controller.create_user(
            UserCreate(
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                email=faker.email(),
                password=faker.password(),
            )
        )
        users = session.exec(select(User)).all()
        assert len(users) == 1
        assert created_user.first_name == users[0].first_name
        assert created_user.last_name == users[0].last_name
        assert created_user.email == users[0].email
        assert created_user.password == users[0].password
        assert created_user.created_at == now


def test_get_user_by_id(user_controller: UserController, faker: Faker) -> None:
    created_user = user_controller.create_user(
        UserCreate(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            email=faker.email(),
            password=faker.password(),
        )
    )
    user = user_controller.get_user_by_id(created_user.id)
    assert user.id == created_user.id
    assert user.first_name == created_user.first_name
    assert user.last_name == created_user.last_name
    assert user.email == created_user.email
    assert user.password == created_user.password


def test_get_users(user_controller: UserController, faker: Faker) -> None:
    created_user_1 = user_controller.create_user(
        UserCreate(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            email=faker.email(),
            password=faker.password(),
        )
    )

    created_user_2 = user_controller.create_user(
        UserCreate(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            email=faker.email(),
            password=faker.password(),
        )
    )

    created_user_3 = user_controller.create_user(
        UserCreate(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            email=faker.email(),
            password=faker.password(),
        )
    )
    users = user_controller.get_users()
    assert users[0].first_name == created_user_1.first_name
    assert users[0].last_name == created_user_1.last_name
    assert users[0].email == created_user_1.email
    assert users[0].password == created_user_1.password
    assert users[1].first_name == created_user_2.first_name
    assert users[1].last_name == created_user_2.last_name
    assert users[1].email == created_user_2.email
    assert users[1].password == created_user_2.password
    assert users[2].first_name == created_user_3.first_name
    assert users[2].last_name == created_user_3.last_name
    assert users[2].email == created_user_3.email
    assert users[2].password == created_user_3.password


def test_delete_create_user(
    user_controller: UserController, session: Session, faker: Faker
) -> None:
    created_user = user_controller.create_user(
        UserCreate(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            email=faker.email(),
            password=faker.password(),
        )
    )
    user_controller.delete_user(created_user.id)
    user = session.exec(select(User)).all()
    assert len(user) == 0


def test_update_user(
    user_controller: UserController, session: Session, faker: Faker
) -> None:
    first_name = faker.first_name()
    last_name = faker.last_name()
    email = faker.email()
    created_user = user_controller.create_user(
        UserCreate(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            email=faker.email(),
            password=faker.password(),
        )
    )
    user_controller.update_user(
        created_user.id,
        UserUpdate(
            first_name=first_name,
            last_name=last_name,
            email=email,
        ),
    )
    user = session.exec(select(User)).all()
    assert user[0].first_name == first_name
    assert user[0].last_name == last_name
    assert user[0].email == email


def test_get_user_runs(
    user_controller: UserController, table_controller: TableController, faker: Faker
) -> None:
    created_user = user_controller.create_user(
        UserCreate(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            email=faker.email(),
            password=faker.password(),
        )
    )
    created_user_2 = user_controller.create_user(
        UserCreate(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            email=faker.email(),
            password=faker.password(),
        )
    )
    created_table_1 = table_controller.create_table(
        TableCreate(title=faker.city(), user_id=created_user.id)
    )
    created_table_2 = table_controller.create_table(
        TableCreate(title=faker.city(), user_id=created_user.id)
    )
    created_table_3 = table_controller.create_table(
        TableCreate(title=faker.city(), user_id=created_user.id)
    )
    created_table_4 = table_controller.create_table(
        TableCreate(title=faker.city(), user_id=created_user_2.id)
    )
    user1_tables = user_controller.get_user_tables(user_id=created_user.id)
    user2_tables = user_controller.get_user_tables(user_id=created_user_2.id)
    assert len(user1_tables) == 3
    assert len(user2_tables) == 1
    assert user1_tables[0].user_id == created_table_1.user_id
    assert user1_tables[0].title == created_table_1.title

    assert user1_tables[1].user_id == created_table_2.user_id
    assert user1_tables[1].title == created_table_2.title

    assert user1_tables[2].user_id == created_table_3.user_id
    assert user1_tables[2].title == created_table_3.title

    assert user2_tables[0].user_id == created_table_4.user_id
    assert user2_tables[0].title == created_table_4.title
