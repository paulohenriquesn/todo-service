from src.domain.entities.task import Task
from abc import ABC, abstractmethod


class TaskRepository(ABC):
    @abstractmethod
    def create(self, task: Task) -> None:
        pass

    @abstractmethod
    def list(self) -> list[Task]:
        pass

    @abstractmethod
    def delete(self, id: str) -> None:
        pass
