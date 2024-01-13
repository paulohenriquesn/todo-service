from src.data.task import TaskService
from src.domain.entities.task import Task


class ListTaskController:
    def __init__(self, TaskService: TaskService):
        self.TaskService = TaskService

    def handle(self, body: None) -> list[Task]:
        try:
            return self.TaskService.list()
        except Exception as error:
            raise error
