from sqlmodel import SQLModel, Field


class TableBase(SQLModel):
    title: str


class Table(TableBase, table=True):
    id: int = Field(default=None, primary_key=True)
    user_id: int = Field(default=None, foreign_key="user.id")


class TableCreate(TableBase):
    user_id: int


class TableUpdate(TableBase):
    pass
