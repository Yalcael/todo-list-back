from faker import Faker
from sqlmodel import Session, select

from todo_list.controllers.columns import ColumnController
from todo_list.controllers.tables import TableController
from todo_list.controllers.tasks import TaskController
from todo_list.controllers.users import UserController
from todo_list.models.columns import ColumnCreate, Column, ColumnUpdate
from todo_list.models.tables import TableCreate
from todo_list.models.tasks import TaskCreate
from todo_list.models.users import UserCreate


def test_create_column(
    user_controller: UserController,
    table_controller: TableController,
    column_controller: ColumnController,
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
    created_column = column_controller.create_column(
        ColumnCreate(title=faker.city(), table_id=created_table.id)
    )
    columns = session.exec(select(Column)).one()
    assert created_column.title == columns.title
    assert created_column.table_id == columns.table_id


def test_get_column_by_id(
    user_controller: UserController,
    table_controller: TableController,
    column_controller: ColumnController,
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
    created_column = column_controller.create_column(
        ColumnCreate(title=faker.city(), table_id=created_table.id)
    )
    column = column_controller.get_column_by_id(created_column.id)
    assert column.id == created_column.id
    assert column.title == created_column.title
    assert column.table_id == created_column.table_id


def test_get_columns(
    user_controller: UserController,
    table_controller: TableController,
    column_controller: ColumnController,
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
    created_user_1 = user_controller.create_user(
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
    created_table_1 = table_controller.create_table(
        TableCreate(title=faker.city(), user_id=created_user_1.id)
    )
    created_column = column_controller.create_column(
        ColumnCreate(title=faker.city(), table_id=created_table.id)
    )
    created_column_1 = column_controller.create_column(
        ColumnCreate(title=faker.city(), table_id=created_table.id)
    )
    created_column_2 = column_controller.create_column(
        ColumnCreate(title=faker.city(), table_id=created_table_1.id)
    )
    created_column_3 = column_controller.create_column(
        ColumnCreate(title=faker.city(), table_id=created_table_1.id)
    )
    columns = column_controller.get_columns()
    assert columns[0].title == created_column.title
    assert columns[0].table_id == created_column.table_id
    assert columns[1].title == created_column_1.title
    assert columns[1].table_id == created_column_1.table_id
    assert columns[2].title == created_column_2.title
    assert columns[2].table_id == created_column_2.table_id
    assert columns[3].title == created_column_3.title
    assert columns[3].table_id == created_column_3.table_id


def test_delete_create_column(
    user_controller: UserController,
    table_controller: TableController,
    column_controller: ColumnController,
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
    created_column = column_controller.create_column(
        ColumnCreate(title=faker.city(), table_id=created_table.id)
    )
    created_column_1 = column_controller.create_column(
        ColumnCreate(title=faker.city(), table_id=created_table.id)
    )
    column_controller.delete_column(created_column.id)
    column = session.exec(select(Column)).one()
    assert column.title == created_column_1.title
    assert column.table_id == created_column_1.table_id


def test_update_column(
    user_controller: UserController,
    table_controller: TableController,
    column_controller: ColumnController,
    session: Session,
    faker: Faker,
) -> None:
    title = faker.city()
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
    created_column = column_controller.create_column(
        ColumnCreate(title=faker.city(), table_id=created_table.id)
    )
    updated_column = column_controller.update_column(
        created_column.table_id, ColumnUpdate(title=title)
    )
    column = session.exec(select(Column)).all()
    assert column[0].title == updated_column.title
    assert column[0].table_id == updated_column.table_id


def test_get_column_tasks(
    user_controller: UserController,
    table_controller: TableController,
    column_controller: ColumnController,
    task_controller: TaskController,
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
    created_user_2 = user_controller.create_user(
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
    created_table_2 = table_controller.create_table(
        TableCreate(title=faker.city(), user_id=created_user_2.id)
    )
    created_column_1 = column_controller.create_column(
        ColumnCreate(title=faker.city(), table_id=created_table.id)
    )
    created_column_2 = column_controller.create_column(
        ColumnCreate(title=faker.city(), table_id=created_table_2.id)
    )
    created_task = task_controller.create_task(
        TaskCreate(
            title=faker.city(),
            description=faker.catch_phrase(),
            tags=faker.catch_phrase_noun(),
            column_id=created_column_1.id,
        )
    )
    created_task_1 = task_controller.create_task(
        TaskCreate(
            title=faker.city(),
            description=faker.catch_phrase(),
            tags=faker.catch_phrase_noun(),
            column_id=created_column_1.id,
        )
    )
    created_task_2 = task_controller.create_task(
        TaskCreate(
            title=faker.city(),
            description=faker.catch_phrase(),
            tags=faker.catch_phrase_noun(),
            column_id=created_column_2.id,
        )
    )
    created_task_3 = task_controller.create_task(
        TaskCreate(
            title=faker.city(),
            description=faker.catch_phrase(),
            tags=faker.catch_phrase_noun(),
            column_id=created_column_2.id,
        )
    )
    column_tasks = column_controller.get_column_tasks(column_id=created_column_1.id)
    column2_tasks = column_controller.get_column_tasks(column_id=created_column_2.id)
    assert len(column_tasks) == 2
    assert len(column2_tasks) == 2
    assert column_tasks[0].column_id == created_task.column_id
    assert column_tasks[0].title == created_task.title
    assert column_tasks[0].description == created_task.description
    assert column_tasks[0].tags == created_task.tags
    assert column_tasks[1].column_id == created_task_1.column_id
    assert column_tasks[1].title == created_task_1.title
    assert column_tasks[1].description == created_task_1.description
    assert column_tasks[1].tags == created_task_1.tags
    assert column2_tasks[0].column_id == created_task_2.column_id
    assert column2_tasks[0].title == created_task_2.title
    assert column2_tasks[0].description == created_task_2.description
    assert column2_tasks[0].tags == created_task_2.tags
    assert column2_tasks[1].column_id == created_task_3.column_id
    assert column2_tasks[1].title == created_task_3.title
    assert column2_tasks[1].description == created_task_3.description
    assert column2_tasks[1].tags == created_task_3.tags
