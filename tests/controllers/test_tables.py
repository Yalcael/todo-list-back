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
    created_user_1 = user_controller.create_user(
        UserCreate(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            email=faker.email(),
            password=faker.password()
        )
    )

    created_user_2 = user_controller.create_user(
        UserCreate(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            email=faker.email(),
            password=faker.password()
        )
    )
    created_table_1 = table_controller.create_table(
        TableCreate(
            title=faker.city(),
            user_id=created_user_1.id
        )
    )
    created_table_2 = table_controller.create_table(
        TableCreate(
            title=faker.city(),
            user_id=created_user_1.id
        )
    )
    created_table_3 = table_controller.create_table(
        TableCreate(
            title=faker.city(),
            user_id=created_user_1.id
        )
    )
    created_table_4 = table_controller.create_table(
        TableCreate(
            title=faker.city(),
            user_id=created_user_2.id
        )
    )
    created_table_5 = table_controller.create_table(
        TableCreate(
            title=faker.city(),
            user_id=created_user_2.id
        )
    )
    tables = table_controller.get_tables()
    assert tables[0].title == created_table_1.title
    assert tables[0].user_id == created_table_1.user_id
    assert tables[1].title == created_table_2.title
    assert tables[1].user_id == created_table_2.user_id
    assert tables[2].title == created_table_3.title
    assert tables[2].user_id == created_table_3.user_id
    assert tables[3].title == created_table_4.title
    assert tables[3].user_id == created_table_4.user_id
    assert tables[4].title == created_table_5.title
    assert tables[4].user_id == created_table_5.user_id


def test_delete_table(user_controller: UserController, table_controller: TableController, session: Session, faker: Faker) -> None:
    created_user = user_controller.create_user(
        UserCreate(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            email=faker.email(),
            password=faker.password()
        )
    )
    created_table_1 = table_controller.create_table(
        TableCreate(
            title=faker.city(),
            user_id=created_user.id
        )
    )
    created_table_2 = table_controller.create_table(
        TableCreate(
            title=faker.city(),
            user_id=created_user.id
        )
    )
    table_controller.delete_table(created_table_1.id)
    table = session.exec(select(Table)).one()
    assert table.title == created_table_2.title
    assert table.user_id == created_table_2.user_id


def test_update_table(user_controller: UserController, table_controller: TableController, session: Session, faker: Faker) -> None:
    title = faker.city()
    created_user = user_controller.create_user(
        UserCreate(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            email=faker.email(),
            password=faker.password()
        )
    )
    created_table = table_controller.create_table(
        TableCreate(
            title=faker.city(),
            user_id=created_user.id
        )
    )
    updated_table = table_controller.update_table(
        created_table.user_id, TableUpdate(title=title)
    )
    table = session.exec(select(Table)).all()
    assert table[0].title == updated_table.title
    assert table[0].user_id == updated_table.user_id
