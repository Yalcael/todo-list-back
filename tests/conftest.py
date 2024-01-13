import pytest
from faker import Faker
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlmodel import SQLModel, Session
from starlette.testclient import TestClient

from todo_list.api import create_app
from todo_list.controllers.users import UserController


@pytest.fixture(name="engine")
def fixture_engine():
    sqlite_url = "sqlite://"
    engine = create_engine(sqlite_url, connect_args={"check_same_thread": False})
    SQLModel.metadata.create_all(engine)
    return engine


@pytest.fixture(name="session")
def fixture_session(engine):
    with Session(engine) as session:
        yield session


@pytest.fixture(name="user_controller")
def fixture_user_controller(session):
    return UserController(session)


@pytest.fixture(name="faker")
def get_faker() -> Faker:
    return Faker("fr_FR")


@pytest.fixture(name="app")
def get_test_app() -> FastAPI:
    return create_app()


@pytest.fixture(name="client")
def get_test_client(app: FastAPI) -> TestClient:
    return TestClient(app)
