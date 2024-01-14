from src.domain.entities.task import Task


def make_task() -> Task:
    return Task('fake_id', 'fake', False)
