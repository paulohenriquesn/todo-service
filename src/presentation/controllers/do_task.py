from src.data.task import TaskService
from src.domain.entities.task import Task


class DoTaskController:
    def __init__(self, TaskService: TaskService):
        self.TaskService = TaskService

    def handle(self, body: dict) -> None:
        try:
            self.TaskService.do(body['id'])
        except Exception as error:
            raise error
