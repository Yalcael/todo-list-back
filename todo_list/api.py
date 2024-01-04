from fastapi import FastAPI
from todo_list.routes.users import router as user_router


def create_app():
    app = FastAPI()
    app.include_router(user_router)
    return app
