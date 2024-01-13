from src.infra.factories.services.task import make_task_service
from src.presentation.controllers.list_tasks import ListTaskController


def make_list_tasks_controller():
    TaskService = make_task_service()
    return ListTaskController(TaskService)
