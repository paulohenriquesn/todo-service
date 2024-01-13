from src.data.task import TaskService
from src.domain.entities.task import Task


class CreateTaskController:
    def __init__(self, TaskService: TaskService):
        self.TaskService = TaskService

    def handle(self, body: dict) -> bool:
        try:
            task = Task(body['title'], False)
            self.TaskService.create(task)
            return True
        except Exception as error:
            raise error
