from dataclasses import dataclass
from domain.usecases.task import TaskUseCases
from domain.entities.task import Task
from typing import Type


@dataclass
class TaskService(TaskUseCases):
    def create(self, task: Type[Task]):
        print('creating on db')
