from http import HTTPStatus

from fastapi import Depends, APIRouter

from todo_list.controllers.tables import TableController
from todo_list.dependencies import get_table_controller
from todo_list.models.tables import Table, TableCreate, TableUpdate

router = APIRouter(
    prefix="/tables", tags=["tables"], responses={404: {"description": "Not found"}}
)


@router.get("/", response_model=list[Table])
def get_tables(*, table_controller: TableController = Depends(get_table_controller)):
    return table_controller.get_tables()


@router.get("/{table_id}", response_model=Table)
def get_table_by_id(
    *, table_id: int, table_controller: TableController = Depends(get_table_controller)
):
    return table_controller.get_table_by_id(table_id)


@router.post("/", response_model=Table)
def create_table(
    *,
    table_create: TableCreate,
    table_controller: TableController = Depends(get_table_controller)
):
    return table_controller.create_table(table_create)


@router.delete("/{table_id}", status_code=HTTPStatus.NO_CONTENT)
def delete_table(
    *, table_id: int, table_controller: TableController = Depends(get_table_controller)
):
    table_controller.delete_table(table_id)


@router.patch("/{table_id}")
def update_table(
    *,
    table_id: int,
    table_update: TableUpdate,
    table_controller: TableController = Depends(get_table_controller)
):
    return table_controller.update_table(table_id, table_update)
