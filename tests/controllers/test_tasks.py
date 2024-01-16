from faker import Faker
from sqlmodel import Session, select

from todo_list.controllers.columns import ColumnController
from todo_list.controllers.tables import TableController
from todo_list.controllers.tasks import TaskController
from todo_list.controllers.users import UserController
from todo_list.models.columns import ColumnCreate
from todo_list.models.tables import TableCreate
from todo_list.models.tasks import TaskCreate, Task, TaskUpdate
from todo_list.models.users import UserCreate


def test_create_task(user_controller: UserController, table_controller: TableController, column_controller: ColumnController, task_controller: TaskController, session: Session, faker: Faker) -> None:
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
    created_column = column_controller.create_column(
        ColumnCreate(
            title=faker.city(),
            table_id=created_table.id
        )
    )
    created_task = task_controller.create_task(
        TaskCreate(
            title=faker.city(),
            description=faker.catch_phrase(),
            tags=faker.catch_phrase_noun(),
            column_id=created_column.id
        )
    )
    tasks = session.exec(select(Task)).one()
    assert created_task.title == tasks.title
    assert created_task.column_id == tasks.column_id
    assert created_task.description == tasks.description
    assert created_task.tags == tasks.tags


def test_get_task_by_id(user_controller: UserController, table_controller: TableController, column_controller: ColumnController, task_controller: TaskController, faker: Faker) -> None:
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
    created_column = column_controller.create_column(
        ColumnCreate(
            title=faker.city(),
            table_id=created_table.id
        )
    )
    created_task = task_controller.create_task(
        TaskCreate(
            title=faker.city(),
            description=faker.catch_phrase(),
            tags=faker.catch_phrase_noun(),
            column_id=created_column.id
        )
    )
    task = task_controller.get_task_by_id(created_task.id)
    assert task.id == created_task.id
    assert task.title == created_task.title
    assert task.description == created_task.description
    assert task.tags == created_task.tags
    assert task.column_id == created_task.column_id


def test_get_tasks(user_controller: UserController, table_controller: TableController, column_controller: ColumnController, task_controller: TaskController, faker: Faker) -> None:
    created_user = user_controller.create_user(
        UserCreate(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            email=faker.email(),
            password=faker.password()
        )
    )
    created_user_1 = user_controller.create_user(
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
    created_table_1 = table_controller.create_table(
        TableCreate(
            title=faker.city(),
            user_id=created_user_1.id
        )
    )
    created_column = column_controller.create_column(
        ColumnCreate(
            title=faker.city(),
            table_id=created_table.id
        )
    )
    created_column_1 = column_controller.create_column(
        ColumnCreate(
            title=faker.city(),
            table_id=created_table_1.id
        )
    )
    created_task = task_controller.create_task(
        TaskCreate(
            title=faker.city(),
            description=faker.catch_phrase(),
            tags=faker.catch_phrase_noun(),
            column_id=created_column.id
        )
    )
    created_task_1 = task_controller.create_task(
        TaskCreate(
            title=faker.city(),
            description=faker.catch_phrase(),
            tags=faker.catch_phrase_noun(),
            column_id=created_column.id
        )
    )
    created_task_2 = task_controller.create_task(
        TaskCreate(
            title=faker.city(),
            description=faker.catch_phrase(),
            tags=faker.catch_phrase_noun(),
            column_id=created_column_1.id
        )
    )
    created_task_3 = task_controller.create_task(
        TaskCreate(
            title=faker.city(),
            description=faker.catch_phrase(),
            tags=faker.catch_phrase_noun(),
            column_id=created_column_1.id
        )
    )
    tasks = task_controller.get_tasks()
    assert tasks[0].title == created_task.title
    assert tasks[0].column_id == created_task.column_id
    assert tasks[0].description == created_task.description
    assert tasks[0].tags == created_task.tags
    assert tasks[1].title == created_task_1.title
    assert tasks[1].column_id == created_task_1.column_id
    assert tasks[1].description == created_task_1.description
    assert tasks[1].tags == created_task_1.tags
    assert tasks[2].title == created_task_2.title
    assert tasks[2].column_id == created_task_2.column_id
    assert tasks[2].description == created_task_2.description
    assert tasks[2].tags == created_task_2.tags
    assert tasks[3].title == created_task_3.title
    assert tasks[3].column_id == created_task_3.column_id
    assert tasks[3].description == created_task_3.description
    assert tasks[3].tags == created_task_3.tags


def test_delete_create_task(user_controller: UserController, table_controller: TableController, column_controller: ColumnController, task_controller: TaskController, session: Session, faker: Faker) -> None:
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
    created_column = column_controller.create_column(
        ColumnCreate(
            title=faker.city(),
            table_id=created_table.id
        )
    )
    created_task = task_controller.create_task(
        TaskCreate(
            title=faker.city(),
            description=faker.catch_phrase(),
            tags=faker.catch_phrase_noun(),
            column_id=created_column.id
        )
    )
    created_task_1 = task_controller.create_task(
        TaskCreate(
            title=faker.city(),
            description=faker.catch_phrase(),
            tags=faker.catch_phrase_noun(),
            column_id=created_column.id
        )
    )
    task_controller.delete_task(created_task.id)
    task = session.exec(select(Task)).one()
    assert task.title == created_task_1.title
    assert task.description == created_task_1.description
    assert task.tags == created_task_1.tags
    assert task.column_id == created_task_1.column_id


def test_update_task(user_controller: UserController, table_controller: TableController, column_controller: ColumnController, task_controller: TaskController, session: Session, faker: Faker) -> None:
    title = faker.city()
    description = faker.catch_phrase()
    tags = faker.catch_phrase_noun()

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
    created_column = column_controller.create_column(
        ColumnCreate(
            title=faker.city(),
            table_id=created_table.id
        )
    )
    created_task = task_controller.create_task(
        TaskCreate(
            title=faker.city(),
            description=faker.catch_phrase(),
            tags=faker.catch_phrase_noun(),
            column_id=created_column.id
        )
    )
    updated_task = task_controller.update_task(
        created_task.column_id, TaskUpdate(title=title, description=description, tags=tags)
    )
    task = session.exec(select(Task)).all()
    assert task[0].title == updated_task.title
    assert task[0].description == updated_task.description
    assert task[0].tags == updated_task.tags
    assert task[0].column_id == updated_task.column_id
