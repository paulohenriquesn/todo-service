from src.domain.entities.task import Task
from typing import Type
from abc import ABC, abstractmethod


class TaskUseCases(ABC):
    @abstractmethod
    def create(self, task: Type[Task]):
        pass

    @abstractmethod
    def list(self):
        pass
