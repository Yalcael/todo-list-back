from fastapi import FastAPI
from todo_list.routes.users import router as user_router
from todo_list.routes.tables import router as table_router


def create_app():
    app = FastAPI()
    app.include_router(user_router)
    app.include_router(table_router)
    return app
