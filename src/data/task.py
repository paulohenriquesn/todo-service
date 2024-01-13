from dataclasses import dataclass
from domain.usecases.task import TaskUseCases
from domain.entities.task import Task
from typing import Type
from domain.repositories.task import TaskRepository


@dataclass
class TaskService(TaskUseCases):
    task_repository: TaskRepository

    def create(self, task: Type[Task]):
        self.task_repository.create(task)
