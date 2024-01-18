from datetime import datetime
from unittest.mock import Mock

from fastapi import FastAPI
from starlette.testclient import TestClient

from todo_list.controllers.users import UserController
from todo_list.dependencies import get_user_controller
from todo_list.models.tables import Table
from todo_list.models.users import User


def test_get_users(user_controller: UserController, app: FastAPI, client: TestClient):
    def _mock_get_users():
        user_controller.get_users = Mock(
            return_value=[
                User(
                    id=1,
                    created_at=datetime(2022, 11, 4),
                    first_name="Samira",
                    last_name="Souhib",
                    email="samiras@gmail.com",
                    password="ss99",
                ),
                User(
                    id=2,
                    created_at=datetime(2022, 11, 4),
                    first_name="Poppy",
                    last_name="Iona",
                    email="poppyi@gmail.com",
                    password="pi99",
                ),
                User(
                    id=3,
                    created_at=datetime(2022, 11, 4),
                    first_name="Sivir",
                    last_name="Shurima",
                    email="sivirs@gmail.com",
                    password="ss59",
                ),
            ]
        )
        return user_controller

    app.dependency_overrides[get_user_controller] = _mock_get_users
    get_users_response = client.get("/users/")
    assert get_users_response.status_code == 200
    assert get_users_response.json() == [
        {
            "id": 1,
            "first_name": "Samira",
            "last_name": "Souhib",
            "email": "samiras@gmail.com",
            "password": "ss99",
            "created_at": "2022-11-04T00:00:00",
        },
        {
            "id": 2,
            "first_name": "Poppy",
            "last_name": "Iona",
            "email": "poppyi@gmail.com",
            "password": "pi99",
            "created_at": "2022-11-04T00:00:00",
        },
        {
            "id": 3,
            "first_name": "Sivir",
            "last_name": "Shurima",
            "email": "sivirs@gmail.com",
            "password": "ss59",
            "created_at": "2022-11-04T00:00:00",
        },
    ]


def test_get_user_by_id(user_controller: UserController, app: FastAPI, client: TestClient) -> None:
    def _mock_get_user_by_id():
        user_controller.get_user_by_id = Mock(
            return_value=User(
                id=1,
                created_at=datetime(2022, 11, 4),
                first_name="Samira",
                last_name="Souhib",
                email="samiras@gmail.com",
                password="ss99",
            ),
        )
        return user_controller

    app.dependency_overrides[get_user_controller] = _mock_get_user_by_id
    get_user_by_id_response = client.get("/users/1")
    assert get_user_by_id_response.status_code == 200
    assert get_user_by_id_response.json() == {
        "id": 1,
        "first_name": "Samira",
        "last_name": "Souhib",
        "email": "samiras@gmail.com",
        "password": "ss99",
        "created_at": "2022-11-04T00:00:00",
    }


def test_create_user(user_controller: UserController, app: FastAPI, client: TestClient) -> None:
    def _mock_create_user():
        user_controller.create_user = Mock(
            return_value=User(
                id=1,
                created_at=datetime(2022, 11, 4),
                first_name="Samira",
                last_name="Souhib",
                email="samiras@gmail.com",
                password="ss99",
            )
        )
        return user_controller

    app.dependency_overrides[get_user_controller] = _mock_create_user
    create_user_response = client.post(
        "/users/",
        json={
            "first_name": "Samira",
            "last_name": "Souhib",
            "email": "samiras@gmail.com",
            "password": "ss99",
            "created_at": "2022-11-04T00:00:00",
        },
    )
    assert create_user_response.status_code == 200
    assert create_user_response.json() == {
        "id": 1,
        "first_name": "Samira",
        "last_name": "Souhib",
        "email": "samiras@gmail.com",
        "password": "ss99",
        "created_at": "2022-11-04T00:00:00",
    }


def test_delete_user(user_controller: UserController, app: FastAPI, client: TestClient) -> None:
    def _mock_delete_user():
        user_controller.delete_user = Mock(
            return_value=User(
                id=1,
                created_at=datetime(2022, 11, 4),
                first_name="Samira",
                last_name="Souhib",
                email="samiras@gmail.com",
                password="ss99",
            )
        )
        return user_controller

    app.dependency_overrides[get_user_controller] = _mock_delete_user
    delete_user_response = client.delete("/users/1")
    assert delete_user_response.status_code == 204


def test_update_user(user_controller: UserController, app: FastAPI, client: TestClient) -> None:
    def _mock_update_user():
        user_controller.update_user = Mock(
            return_value=User(
                id=1,
                created_at=datetime(2022, 11, 4),
                first_name="Samira",
                last_name="Souhib",
                email="samiras@gmail.com",
                password="ss99",
            )
        )
        return user_controller

    app.dependency_overrides[get_user_controller] = _mock_update_user
    update_user_response = client.patch(
        "/users/1",
        json={
            "first_name": "Samira",
            "last_name": "Souhib",
            "email": "samiras@gmail.com",
            "password": "ss99",
            "created_at": "2022-11-04T00:00:00",
        }
    )
    assert update_user_response.status_code == 200
    assert update_user_response.json() == {
        "id": 1,
        "first_name": "Samira",
        "last_name": "Souhib",
        "email": "samiras@gmail.com",
        "password": "ss99",
        "created_at": "2022-11-04T00:00:00",
    }


def test_get_user_tables(user_controller: UserController, app: FastAPI, client: TestClient) -> None:
    def _mock_get_user_tables():
        user_controller.get_user_tables = Mock(
            return_value=[
                Table(id=1, title="test1", user_id=1, created_at="2022-11-4"),
                Table(id=2, title="test2", user_id=1, created_at="2022-11-4"),
                Table(id=3, title="test3", user_id=1, created_at="2022-11-4"),
            ]
        )
        return user_controller

    app.dependency_overrides[get_user_controller] = _mock_get_user_tables
    get_user_tables_response = client.get("/users/1/tables")
    assert get_user_tables_response.status_code == 200
    assert get_user_tables_response.json() == [
        {"id": 1, "title": "test1", "created_at": "2022-11-4", "user_id": 1},
        {"id": 2, "title": "test2", "created_at": "2022-11-4", "user_id": 1},
        {"id": 3, "title": "test3", "created_at": "2022-11-4", "user_id": 1},
    ]
