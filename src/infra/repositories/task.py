import uuid
from typing import Type
from pypika import Query, Table
from src.domain.repositories.task import TaskRepository
from src.domain.entities.task import Task
from src.infra.db.pg import connection


class TaskPostgresRepository(TaskRepository):
    def create(self, task: Type[Task]):
        table_name = Table('tasks')
        cursor = connection.cursor()
        try:
            query = Query.into(table_name).insert(
                uuid.uuid4(), task.title, False)
            print(query.get_sql())
            cursor.execute(query.get_sql())
            connection.commit()
        except Exception as error:
            raise error
        finally:
            connection.close()
