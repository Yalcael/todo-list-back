from http import HTTPStatus

from fastapi import APIRouter, Depends

from todo_list.controllers.users import UserController
from todo_list.dependencies import get_user_controller
from todo_list.models.tables import Table
from todo_list.models.users import User, UserCreate, UserUpdate


router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=list[User])
def get_users(*, user_controller: UserController = Depends(get_user_controller)):
    return user_controller.get_users()


@router.get("/{user_id}", response_model=User)
def get_user_by_id(
    *, user_id: int, user_controller: UserController = Depends(get_user_controller)
):
    return user_controller.get_user_by_id(user_id)


@router.post("/", response_model=User)
def create_user(
    *,
    user_create: UserCreate,
    user_controller: UserController = Depends(get_user_controller)
):
    return user_controller.create_user(user_create)


@router.delete("/{user_id}", status_code=HTTPStatus.NO_CONTENT)
def delete_user(
    *, user_id: int, user_controller: UserController = Depends(get_user_controller)
):
    user_controller.delete_user(user_id)


@router.patch("/{user_id}", response_model=User)
def update_user(
    *,
    user_id: int,
    user_update: UserUpdate,
    user_controller: UserController = Depends(get_user_controller)
):
    return user_controller.update_user(user_id, user_update)


@router.get("/{user_id}/tables", response_model=list[Table])
def get_user_tables(
    *, user_id: int, user_controller: UserController = Depends(get_user_controller)
):
    return user_controller.get_user_tables(user_id)
