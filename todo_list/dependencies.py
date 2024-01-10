from fastapi import Depends
from sqlmodel import Session

from todo_list.controllers.columns import ColumnController
from todo_list.controllers.kpi import KpiController
from todo_list.controllers.tables import TableController
from todo_list.controllers.tasks import TaskController
from todo_list.controllers.users import UserController
from todo_list.database import engine


def get_session():
    with Session(engine) as session:
        yield session


def get_user_controller(session=Depends(get_session)):
    return UserController(session)


def get_table_controller(session=Depends(get_session)):
    return TableController(session)


def get_column_controller(session=Depends(get_session)):
    return ColumnController(session)


def get_task_controller(session=Depends(get_session)):
    return TaskController(session)


def get_kpi_controller(session=Depends(get_session)):
    return KpiController(session)
