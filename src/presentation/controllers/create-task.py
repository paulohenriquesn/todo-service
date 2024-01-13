from data.task import TaskService
from domain.entities.task import Task


class CreateTaskController:
    def handle(self, body: dict, TaskService: TaskService) -> bool:
        try:
            task = Task(body['title'], False)
            TaskService.create(task)
            return True
        except Exception as error:
            raise (error)
