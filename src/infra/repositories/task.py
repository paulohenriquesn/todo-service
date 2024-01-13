import uuid
from sqlalchemy import insert, select, Table, MetaData, Column, String, Boolean
from src.domain.repositories.task import TaskRepository
from src.domain.entities.task import Task
from src.infra.db.pg import engine


tasks = Table(
    "tasks",
    MetaData(),
    Column("id", String, primary_key=True),
    Column("title", String, nullable=False),
    Column("done", Boolean)
)


class TaskPostgresRepository(TaskRepository):
    def create(self, task: Task):
        try:
            query = (insert(tasks).values(
                id=uuid.uuid4(), title=task.title, done=False))
            with engine.connect() as conn:
                conn.execute(query)
                conn.commit()
        except Exception as error:
            raise error

    def list(self) -> list[Task]:
        try:
            query = (select(tasks))
            with engine.connect() as conn:
                results = []
                for row in conn.execute(query):
                    results.append(Task(row[1], row[2]))
                return results
        except Exception as error:
            raise error
