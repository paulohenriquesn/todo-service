import uuid
from typing import Type
from pypika import Query, Table
from domain.repositories.task import TaskRepository
from domain.entities.task import Task
from infra.db.pg import connection


class TaskPostgresRepository(TaskRepository):
    table_name = Table('tasks')
    cursor = connection.cursor()

    def create(self, task: Type[Task]):
        try:
            query = Query.into(self.table_name).insert(
                uuid.uuid4(), task.title, False)
            self.cursor.execute(query)
        except Exception as error:
            print(error)
