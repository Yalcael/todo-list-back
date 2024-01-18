from unittest.mock import Mock

from fastapi import FastAPI
from starlette.testclient import TestClient

from todo_list.controllers.tables import TableController
from todo_list.dependencies import get_table_controller
from todo_list.models.columns import Column
from todo_list.models.tables import Table


def test_get_tables(
    table_controller: TableController, app: FastAPI, client: TestClient
) -> None:
    def _mock_get_tables():
        table_controller.get_tables = Mock(
            return_value=[
                Table(id=1, title="test1", user_id=1, created_at="2022-11-4"),
                Table(id=2, title="test2", user_id=1, created_at="2022-11-4"),
                Table(id=3, title="test3", user_id=1, created_at="2022-11-4"),
            ]
        )
        return table_controller

    app.dependency_overrides[get_table_controller] = _mock_get_tables
    get_tables_response = client.get("/tables/")
    assert get_tables_response.status_code == 200
    assert get_tables_response.json() == [
        {"id": 1, "title": "test1", "created_at": "2022-11-4", "user_id": 1},
        {"id": 2, "title": "test2", "created_at": "2022-11-4", "user_id": 1},
        {"id": 3, "title": "test3", "created_at": "2022-11-4", "user_id": 1},
    ]


def test_get_table_by_id(
    table_controller: TableController, app: FastAPI, client: TestClient
) -> None:
    def _mock_get_table_by_id():
        table_controller.get_table_by_id = Mock(
            return_value=Table(id=1, title="test1", user_id=1, created_at="2022-11-4")
        )
        return table_controller

    app.dependency_overrides[get_table_controller] = _mock_get_table_by_id
    get_table_by_id_response = client.get("/tables/1")
    assert get_table_by_id_response.status_code == 200
    assert get_table_by_id_response.json() == {
        "id": 1,
        "title": "test1",
        "created_at": "2022-11-4",
        "user_id": 1,
    }


def test_create_table(
    table_controller: TableController, app: FastAPI, client: TestClient
) -> None:
    def _mock_create_table():
        table_controller.create_table = Mock(
            return_value=Table(id=1, title="test1", user_id=1, created_at="2022-11-4")
        )
        return table_controller

    app.dependency_overrides[get_table_controller] = _mock_create_table
    create_table_response = client.post(
        "/tables/",
        json={"title": "test1", "created_at": "2022-11-4", "user_id": 1},
    )
    assert create_table_response.status_code == 200
    assert create_table_response.json() == {
        "id": 1,
        "title": "test1",
        "created_at": "2022-11-4",
        "user_id": 1,
    }


def test_delete_table(
    table_controller: TableController, app: FastAPI, client: TestClient
) -> None:
    def _mock_delete_table():
        table_controller.delete_table = Mock(
            return_value=Table(id=1, title="test1", user_id=1, created_at="2022-11-4")
        )
        return table_controller

    app.dependency_overrides[get_table_controller] = _mock_delete_table
    delete_table_response = client.delete("/tables/1")
    assert delete_table_response.status_code == 204


def test_update_table(
    table_controller: TableController, app: FastAPI, client: TestClient
) -> None:
    def _mock_update_table():
        table_controller.update_table = Mock(
            return_value=Table(id=1, title="test1", user_id=1, created_at="2022-11-4")
        )
        return table_controller

    app.dependency_overrides[get_table_controller] = _mock_update_table
    update_table_response = client.patch("/tables/1", json={"title": "test1"})
    assert update_table_response.status_code == 200
    assert update_table_response.json() == {
        "id": 1,
        "title": "test1",
        "created_at": "2022-11-4",
        "user_id": 1,
    }


def test_get_table_columns(
    table_controller: TableController, app: FastAPI, client: TestClient
) -> None:
    def _mock_get_table_columns():
        table_controller.get_table_columns = Mock(
            return_value=[
                Column(id=1, title="test1", table_id=1, created_at="2022-11-4"),
                Column(id=2, title="test2", table_id=1, created_at="2022-11-4"),
                Column(id=3, title="test3", table_id=1, created_at="2022-11-4"),
            ]
        )
        return table_controller

    app.dependency_overrides[get_table_controller] = _mock_get_table_columns
    get_table_columns_response = client.get("/tables/1/columns")
    assert get_table_columns_response.status_code == 200
    assert get_table_columns_response.json() == [
        {"id": 1, "title": "test1", "created_at": "2022-11-4", "table_id": 1},
        {"id": 2, "title": "test2", "created_at": "2022-11-4", "table_id": 1},
        {"id": 3, "title": "test3", "created_at": "2022-11-4", "table_id": 1},
    ]
