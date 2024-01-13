from src.infra.repositories.task import TaskPostgresRepository
from src.data.task import TaskService


def make_task_service():
    task_repository = TaskPostgresRepository()
    return TaskService(task_repository)
