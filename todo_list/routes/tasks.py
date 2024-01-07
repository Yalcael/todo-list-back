from http import HTTPStatus

from fastapi import Depends, APIRouter

from todo_list.controllers.tasks import TaskController
from todo_list.dependencies import get_task_controller
from todo_list.models.tasks import Task, TaskCreate, TaskUpdate

router = APIRouter(
    prefix="/tasks", tags=["tasks"], responses={404: {"description": "Not found"}}
)


@router.get("/", response_model=list[Task])
def get_tasks(*, task_controller: TaskController = Depends(get_task_controller)):
    return task_controller.get_tasks()


@router.get("/{task_id}", response_model=Task)
def get_task_by_id(
    *, task_id: int, task_controller: TaskController = Depends(get_task_controller)
):
    return task_controller.get_task_by_id(task_id)


@router.post("/", response_model=Task)
def create_task(
    *,
    task_create: TaskCreate,
    task_controller: TaskController = Depends(get_task_controller)
):
    return task_controller.create_task(task_create)


@router.delete("/{task_id}", status_code=HTTPStatus.NO_CONTENT)
def delete_task(
    *, task_id: int, task_controller: TaskController = Depends(get_task_controller)
):
    task_controller.delete_task(task_id)


@router.patch("/{task_id}")
def update_task(
    *,
    task_id: int,
    task_update: TaskUpdate,
    task_controller: TaskController = Depends(get_task_controller)
):
    return task_controller.update_task(task_id, task_update)
