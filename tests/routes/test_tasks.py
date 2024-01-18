from unittest.mock import Mock

from fastapi import FastAPI
from starlette.testclient import TestClient

from todo_list.controllers.tasks import TaskController
from todo_list.dependencies import get_task_controller
from todo_list.models.tasks import Task


def test_get_tasks(
    task_controller: TaskController, app: FastAPI, client: TestClient
) -> None:
    def _mock_get_tasks():
        task_controller.get_tasks = Mock(
            return_value=[
                Task(
                    id=1,
                    title="test1",
                    created_at="2022-11-4",
                    column_id=1,
                    description="test1",
                    tags="tag1, tag2",
                ),
                Task(
                    id=2,
                    title="test2",
                    created_at="2022-11-4",
                    column_id=1,
                    description="test2",
                    tags="tag3, tag4",
                ),
                Task(
                    id=3,
                    title="test3",
                    created_at="2022-11-4",
                    column_id=1,
                    description="test3",
                    tags="tag5, tag6",
                ),
            ]
        )
        return task_controller

    app.dependency_overrides[get_task_controller] = _mock_get_tasks
    get_tasks_response = client.get("/tasks/")
    assert get_tasks_response.status_code == 200
    assert get_tasks_response.json() == [
        {
            "id": 1,
            "title": "test1",
            "created_at": "2022-11-4",
            "column_id": 1,
            "description": "test1",
            "tags": "tag1, tag2",
        },
        {
            "id": 2,
            "title": "test2",
            "created_at": "2022-11-4",
            "column_id": 1,
            "description": "test2",
            "tags": "tag3, tag4",
        },
        {
            "id": 3,
            "title": "test3",
            "created_at": "2022-11-4",
            "column_id": 1,
            "description": "test3",
            "tags": "tag5, tag6",
        },
    ]


def test_get_task_by_id(
    task_controller: TaskController, app: FastAPI, client: TestClient
) -> None:
    def _mock_get_task_by_id():
        task_controller.get_task_by_id = Mock(
            return_value=Task(
                id=1,
                title="test1",
                created_at="2022-11-4",
                column_id=1,
                description="test1",
                tags="tag1, tag2",
            ),
        )
        return task_controller

    app.dependency_overrides[get_task_controller] = _mock_get_task_by_id
    get_task_by_id_response = client.get("/tasks/1")
    assert get_task_by_id_response.status_code == 200
    assert get_task_by_id_response.json() == {
        "id": 1,
        "title": "test1",
        "created_at": "2022-11-4",
        "column_id": 1,
        "description": "test1",
        "tags": "tag1, tag2",
    }


def test_create_task(
    task_controller: TaskController, app: FastAPI, client: TestClient
) -> None:
    def _mock_create_task():
        task_controller.create_task = Mock(
            return_value=Task(
                id=1,
                title="test1",
                created_at="2022-11-4",
                column_id=1,
                description="test1",
                tags="tag1, tag2",
            )
        )
        return task_controller

    app.dependency_overrides[get_task_controller] = _mock_create_task
    create_task_response = client.post(
        "/tasks/",
        json={
            "title": "test1",
            "created_at": "2022-11-4",
            "column_id": 1,
            "description": "test1",
            "tags": "tag1, tag2",
        },
    )
    assert create_task_response.status_code == 200
    assert create_task_response.json() == {
        "id": 1,
        "title": "test1",
        "created_at": "2022-11-4",
        "column_id": 1,
        "description": "test1",
        "tags": "tag1, tag2",
    }


def test_delete_task(
    task_controller: TaskController, app: FastAPI, client: TestClient
) -> None:
    def _mock_delete_task():
        task_controller.delete_task = Mock(
            return_value=Task(
                id=1,
                title="test1",
                created_at="2022-11-4",
                column_id=1,
                description="test1",
                tags="tag1, tag2",
            )
        )
        return task_controller

    app.dependency_overrides[get_task_controller] = _mock_delete_task
    delete_task_response = client.delete("/tasks/1")
    assert delete_task_response.status_code == 204


def test_update_task(
    task_controller: TaskController, app: FastAPI, client: TestClient
) -> None:
    def _mock_update_task():
        task_controller.update_task = Mock(
            return_value=Task(
                id=1,
                title="test1",
                created_at="2022-11-4",
                column_id=1,
                description="test1",
                tags="tag1, tag2",
            )
        )
        return task_controller

    app.dependency_overrides[get_task_controller] = _mock_update_task
    update_task_response = client.patch(
        "/tasks/1",
        json={
            "title": "test1",
            "created_at": "2022-11-4",
            "column_id": 1,
            "description": "test1",
            "tags": "tag1, tag2",
        },
    )
    assert update_task_response.status_code == 200
    assert update_task_response.json() == {
        "id": 1,
        "title": "test1",
        "created_at": "2022-11-4",
        "column_id": 1,
        "description": "test1",
        "tags": "tag1, tag2",
    }
