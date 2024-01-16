from todo_list.models.tasks import Task, TaskCreate, TaskUpdate
from sqlmodel import select


class TaskController:
    def __init__(self, session):
        self.session = session

    def get_tasks(self) -> list[Task]:
        return self.session.exec(select(Task)).all()

    def get_task_by_id(self, task_id: int) -> Task:
        return self.session.exec(select(Task).where(Task.id == task_id)).one()

    def create_task(self, task_create: TaskCreate) -> Task:
        new_task = Task(
            title=task_create.title,
            column_id=task_create.column_id,
            description=task_create.description,
            tags=task_create.tags,
        )
        self.session.add(new_task)
        self.session.commit()
        self.session.refresh(new_task)
        return new_task

    def delete_task(self, task_id: int) -> None:
        task = self.session.exec(select(Task).where(Task.id == task_id)).one()
        self.session.delete(task)
        self.session.commit()

    def update_task(self, task_id: int, task_update: TaskUpdate) -> Task:
        task = self.session.exec(select(Task).where(Task.id == task_id)).one()
        for key, val in task_update.dict(exclude_unset=True).items():
            setattr(task, key, val)
        self.session.add(task)
        self.session.commit()
        self.session.refresh(task)
        return task
