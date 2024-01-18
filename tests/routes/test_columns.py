from unittest.mock import Mock

from fastapi import FastAPI
from starlette.testclient import TestClient

from todo_list.controllers.columns import ColumnController
from todo_list.dependencies import get_column_controller
from todo_list.models.columns import Column
from todo_list.models.tasks import Task


def test_get_columns(
    column_controller: ColumnController, app: FastAPI, client: TestClient
) -> None:
    def _mock_get_columns():
        column_controller.get_columns = Mock(
            return_value=[
                Column(id=1, title="test1", table_id=1, created_at="2022-11-4"),
                Column(id=2, title="test2", table_id=1, created_at="2022-11-4"),
                Column(id=3, title="test3", table_id=1, created_at="2022-11-4"),
            ]
        )
        return column_controller

    app.dependency_overrides[get_column_controller] = _mock_get_columns
    get_columns_response = client.get("/columns/")
    assert get_columns_response.status_code == 200
    assert get_columns_response.json() == [
        {"id": 1, "title": "test1", "created_at": "2022-11-4", "table_id": 1},
        {"id": 2, "title": "test2", "created_at": "2022-11-4", "table_id": 1},
        {"id": 3, "title": "test3", "created_at": "2022-11-4", "table_id": 1},
    ]


def test_get_column_by_id(
    column_controller: ColumnController, app: FastAPI, client: TestClient
) -> None:
    def _mock_get_column_by_id():
        column_controller.get_column_by_id = Mock(
            return_value=Column(id=1, title="test1", table_id=1, created_at="2022-11-4")
        )
        return column_controller

    app.dependency_overrides[get_column_controller] = _mock_get_column_by_id
    get_column_by_id_response = client.get("/columns/1")
    assert get_column_by_id_response.status_code == 200
    assert get_column_by_id_response.json() == {
        "id": 1,
        "title": "test1",
        "created_at": "2022-11-4",
        "table_id": 1,
    }


def test_create_column(
    column_controller: ColumnController, app: FastAPI, client: TestClient
) -> None:
    def _mock_create_column():
        column_controller.create_column = Mock(
            return_value=Column(id=1, title="test1", table_id=1, created_at="2022-11-4")
        )
        return column_controller

    app.dependency_overrides[get_column_controller] = _mock_create_column
    create_column_response = client.post(
        "/columns/",
        json={"title": "test1", "created_at": "2022-11-4", "table_id": 1},
    )
    assert create_column_response.status_code == 200
    assert create_column_response.json() == {
        "id": 1,
        "title": "test1",
        "created_at": "2022-11-4",
        "table_id": 1,
    }


def test_delete_column(
    column_controller: ColumnController, app: FastAPI, client: TestClient
) -> None:
    def _mock_delete_column():
        column_controller.delete_column = Mock(
            return_value=Column(id=1, title="test1", table_id=1, created_at="2022-11-4")
        )
        return column_controller

    app.dependency_overrides[get_column_controller] = _mock_delete_column
    delete_column_response = client.delete("/columns/1")
    assert delete_column_response.status_code == 204


def test_update_column(
    column_controller: ColumnController, app: FastAPI, client: TestClient
) -> None:
    def _mock_update_column():
        column_controller.update_column = Mock(
            return_value=Column(id=1, title="test1", table_id=1, created_at="2022-11-4")
        )
        return column_controller

    app.dependency_overrides[get_column_controller] = _mock_update_column
    update_column_response = client.patch("/columns/1", json={"title": "test1"})
    assert update_column_response.status_code == 200
    assert update_column_response.json() == {
        "id": 1,
        "title": "test1",
        "created_at": "2022-11-4",
        "table_id": 1,
    }


def test_get_column_tasks(
    column_controller: ColumnController, app: FastAPI, client: TestClient
) -> None:
    def _mock_get_column_tasks():
        column_controller.get_column_tasks = Mock(
            return_value=[
                Task(
                    id=1,
                    title="test1",
                    created_at="2022-11-4",
                    column_id=1,
                    description="test1",
                    tags=["tag1", "tag2"],
                )
            ]
        )
        return column_controller

    app.dependency_overrides[get_column_controller] = _mock_get_column_tasks
    get_column_tasks_response = client.get("/columns/1/tasks")
    assert get_column_tasks_response.status_code == 200
    assert get_column_tasks_response.json() == [
        {
            "id": 1,
            "title": "test1",
            "description": "test1",
            "tags": ["tag1", "tag2"],
            "column_id": 1,
            "created_at": "2022-11-4",
        }
    ]
