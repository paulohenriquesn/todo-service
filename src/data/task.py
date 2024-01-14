from dataclasses import dataclass
from src.domain.usecases.task import TaskUseCases
from src.domain.entities.task import Task
from src.domain.repositories.task import TaskRepository


@dataclass
class TaskService(TaskUseCases):
    task_repository: TaskRepository

    def create(self, task: Task):
        self.task_repository.create(task)

    def list(self) -> list[Task]:
        return self.task_repository.list()

    def delete(self, id: str):
        return self.task_repository.delete(id)

    def do(self, id: str):
        return self.task_repository.do(id)
