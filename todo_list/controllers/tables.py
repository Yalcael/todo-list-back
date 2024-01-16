from sqlmodel import select

from todo_list.models.columns import Column
from todo_list.models.tables import Table, TableCreate, TableUpdate


class TableController:
    def __init__(self, session):
        self.session = session

    def get_tables(self) -> list[Table]:
        return self.session.exec(select(Table)).all()

    def get_table_by_id(self, table_id: int) -> Table:
        return self.session.exec(select(Table).where(Table.id == table_id)).one()

    def create_table(self, table_create: TableCreate) -> Table:
        new_table = Table(title=table_create.title, user_id=table_create.user_id)
        self.session.add(new_table)
        self.session.commit()
        self.session.refresh(new_table)
        return new_table

    def delete_table(self, table_id: int) -> None:
        table = self.session.exec(select(Table).where(Table.id == table_id)).one()
        self.session.delete(table)
        self.session.commit()

    def update_table(self, table_id: int, table_update: TableUpdate) -> Table:
        table = self.session.exec(select(Table).where(Table.id == table_id)).one()
        for key, val in table_update.dict(exclude_unset=True).items():
            setattr(table, key, val)
        self.session.add(table)
        self.session.commit()
        self.session.refresh(table)
        return table

    def get_table_columns(self, table_id) -> list[Column]:
        return self.session.exec(
            select(Column).join(Table).where(Table.id == table_id)
        ).all()
