from src.app.factories.services.task import make_task_service
from src.presentation.controllers.delete_task import DeleteTaskController


def make_delete_task_controller():
    TaskService = make_task_service()
    return DeleteTaskController(TaskService)
