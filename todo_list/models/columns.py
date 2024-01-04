from sqlmodel import SQLModel, Field


class ColumnBase(SQLModel):
    title: str


class Column(ColumnBase, table=True):
    id: int = Field(default=None, primary_key=True)
    table_id: int = Field(default=None, foreign_key="table.id")


class ColumnCreate(ColumnBase):
    table_id: int


class ColumnUpdate(ColumnBase):
    pass
