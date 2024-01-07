from todo_list.models.columns import Column, ColumnCreate, ColumnUpdate
from sqlmodel import select


class ColumnController:
    def __init__(self, session):
        self.session = session

    def get_columns(self) -> list[Column]:
        return self.session.exec(select(Column)).all()

    def get_column_by_id(self, column_id: int) -> Column:
        return self.session.exec(select(Column).where(Column.id == column_id)).one()

    def create_column(self, column_create: ColumnCreate) -> Column:
        new_column = Column(title=column_create.title, table_id=column_create.table_id)
        self.session.add(new_column)
        self.session.commit()
        self.session.refresh(new_column)
        return new_column

    def delete_column(self, column_id: int) -> None:
        column = self.session.exec(select(Column).where(Column.id == column_id)).one()
        self.session.delete(column)
        self.session.commit()

    def update_column(self, column_id: int, column_update: ColumnUpdate) -> Column:
        column = self.session.exec(select(Column).where(Column.id == column_id)).one()
        if column_update.title:
            column.title = column_update.title
        self.session.add(column)
        self.session.commit()
        self.session.refresh(column)
        return column
