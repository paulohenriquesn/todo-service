from src.app.factories.services.task import make_task_service
from src.presentation.controllers.do_task import DoTaskController


def make_do_task_controller():
    TaskService = make_task_service()
    return DoTaskController(TaskService)
