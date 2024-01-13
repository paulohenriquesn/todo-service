from domain.entities.task import Task
from abc import ABC, abstractmethod


class TaskRepository(ABC):
    @abstractmethod
    def create(self, task: Task):
        pass
