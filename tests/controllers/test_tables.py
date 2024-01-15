from faker import Faker
from sqlmodel import Session, select

from todo_list.controllers.tables import TableController
from todo_list.controllers.users import UserController
from todo_list.models.tables import TableCreate, Table, TableUpdate
from todo_list.models.users import UserCreate


def test_create_table(
    user_controller: UserController,
    table_controller: TableController,
    session: Session,
    faker: Faker,
) -> None:
    created_user = user_controller.create_user(
        UserCreate(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            email=faker.email(),
            password=faker.password(),
        )
    )
    created_table = table_controller.create_table(
        TableCreate(title=faker.city(), user_id=created_user.id)
    )
    tables = session.exec(select(Table)).one()
    assert created_table.title == tables.title
    assert created_table.user_id == tables.user_id


def test_get_table_by_id(
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
    created_table_1 = table_controller.create_table(
        TableCreate(title=faker.city(), user_id=created_user.id)
    )
    _ = table_controller.create_table(
        TableCreate(title=faker.city(), user_id=created_user.id)
    )
    _ = table_controller.create_table(
        TableCreate(title=faker.city(), user_id=created_user.id)
    )
    table = table_controller.get_table_by_id(created_table_1.id)
    assert table.id == created_table_1.id
    assert table.title == created_table_1.title
    assert table.user_id == created_table_1.user_id


def test_get_tables(user_controller: UserController, table_controller: TableController, faker: Faker) -> None:
    ...
