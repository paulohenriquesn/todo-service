from src.app.factories.services.task import make_task_service
from src.presentation.controllers.create_task import CreateTaskController


def make_create_task_controller():
    TaskService = make_task_service()
    return CreateTaskController(TaskService)
