from src.domain.repositories.task import TaskRepository
from src.domain.entities.task import Task
from tests.entities.task import make_task


class TaskRepositoryStub(TaskRepository):
    def create(self, task: Task):
        pass

    def list(self) -> list[Task]:
        return [make_task()]

    def delete(self, id: str) -> None:
        pass
