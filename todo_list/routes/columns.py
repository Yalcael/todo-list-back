from http import HTTPStatus

from fastapi import Depends, APIRouter

from todo_list.controllers.columns import ColumnController
from todo_list.dependencies import get_column_controller
from todo_list.models.columns import Column, ColumnCreate, ColumnUpdate
from todo_list.models.tasks import Task

router = APIRouter(
    prefix="/columns", tags=["columns"], responses={404: {"description": "Not found"}}
)


@router.get("/", response_model=list[Column])
def get_columns(
    *, column_controller: ColumnController = Depends(get_column_controller)
):
    return column_controller.get_columns()


@router.get("/{column_id}", response_model=Column)
def get_column_by_id(
    *,
    column_id: int,
    column_controller: ColumnController = Depends(get_column_controller)
):
    return column_controller.get_column_by_id(column_id)


@router.post("/", response_model=Column)
def create_column(
    *,
    column_create: ColumnCreate,
    column_controller: ColumnController = Depends(get_column_controller)
):
    return column_controller.create_column(column_create)


@router.delete("/{column_id}", status_code=HTTPStatus.NO_CONTENT)
def delete_column(
    *,
    column_id: int,
    column_controller: ColumnController = Depends(get_column_controller)
):
    column_controller.delete_column(column_id)


@router.patch("/{column_id}")
def update_column(
    *,
    column_id: int,
    column_update: ColumnUpdate,
    column_controller: ColumnController = Depends(get_column_controller)
):
    return column_controller.update_column(column_id, column_update)


@router.get("/{column_id}/tasks", response_model=list[Task])
def get_column_tasks(
    *,
    column_id: int,
    column_controller: ColumnController = Depends(get_column_controller)
):
    return column_controller.get_column_tasks(column_id)
