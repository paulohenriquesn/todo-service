from src.data.task import TaskService
from src.domain.entities.task import Task


class CreateTaskController:
    def __init__(self, TaskService: TaskService):
        self.TaskService = TaskService

    def handle(self, body: dict) -> None:
        try:
            task = Task(None, body['title'], False)
            self.TaskService.create(task)
        except Exception as error:
            raise error
