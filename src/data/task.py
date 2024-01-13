from dataclasses import dataclass
from src.domain.usecases.task import TaskUseCases
from src.domain.entities.task import Task
from src.domain.repositories.task import TaskRepository


@dataclass
class TaskService(TaskUseCases):
    task_repository: TaskRepository

    def create(self, task: Task):
        self.task_repository.create(task)
