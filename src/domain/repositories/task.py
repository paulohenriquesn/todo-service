from domain.entities.task import Task
from typing import Type
from abc import ABC, abstractmethod


class TaskRepository(ABC):
    @abstractmethod
    def create(self, task: Type[Task]):
        pass