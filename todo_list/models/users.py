from datetime import datetime

from sqlmodel import Field, SQLModel


class UserBase(SQLModel):
    first_name: str
    last_name: str
    email: str


class User(UserBase, table=True):
    id: int = Field(default=None, primary_key=True)
    password: str
    created_at: datetime = Field(default_factory=datetime.now)


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    pass
