import uuid
from sqlalchemy import delete, insert, select, Table, MetaData, Column, String, Boolean
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
                    results.append(Task(row[0], row[1], row[2]))
                return results
        except Exception as error:
            raise error

    def delete(self, id: str) -> None:
        try:
            query = (delete(tasks).where(tasks.c.id == id))
            with engine.connect() as conn:
                conn.execute(query)
                conn.commit()
        except Exception as error:
            raise error
