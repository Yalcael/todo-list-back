import uvicorn

from todo_list.api import create_app

app = create_app()


if __name__ == "__main__":
    uvicorn.run(app, port=5001)
