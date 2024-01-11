from datetime import datetime, timedelta

from sqlmodel import col

from todo_list.models.tables import Table
from todo_list.models.users import User


class KpiController:
    def __init__(self, session):
        self.session = session

    def _get_number_of_users(self):
        return self.session.query(User).count()

    def _get_number_of_users_last_week(self):
        last_week_date = datetime.now() - timedelta(days=7)
        return (
            self.session.query(User)
            .filter(col(User.created_at).between(last_week_date, datetime.now()))
            .count()
        )

    def _get_average_tables_per_users(self):
        total_users = self._get_number_of_users()
        total_tables = self.session.query(Table).count()

        if total_users > 0:
            return total_tables / total_users
        else:
            return 0

    def get_users_kpi(self):
        return {
            "number_of_users": self._get_number_of_users(),
            "number_of_users_last_week": self._get_number_of_users_last_week(),
            "average_tables_per_users": self._get_average_tables_per_users(),
        }
