from datetime import datetime

from sqlmodel import SQLModel, Field


class TaskBase(SQLModel):
    title: str
    description: str
    tags: str


class Task(TaskBase, table=True):
    id: int = Field(default=None, primary_key=True)
    column_id: int = Field(default=None, foreign_key="column.id")
    created_at: datetime = Field(default_factory=datetime.now)


class TaskCreate(TaskBase):
    column_id: int


class TaskUpdate(TaskBase):
    pass
