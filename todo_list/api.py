from fastapi import FastAPI
from todo_list.routes.users import router as user_router
from todo_list.routes.tables import router as table_router
from todo_list.routes.columns import router as column_router
from todo_list.routes.tasks import router as task_router


def create_app():
    app = FastAPI()
    app.include_router(user_router)
    app.include_router(table_router)
    app.include_router(column_router)
    app.include_router(task_router)
    return app
