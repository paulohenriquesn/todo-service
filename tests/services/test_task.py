from unittest.mock import MagicMock
from src.domain.entities.task import Task
from src.data.task import TaskService
from tests.stubs.repositories.task import TaskRepositoryStub
from tests.entities.task import make_task

stub_repository = TaskRepositoryStub()
service = TaskService(stub_repository)


class TestCreate:
    input: Task = make_task()

    def test_repository_is_called(self):
        stub_repository.create = MagicMock()
        service.create(self.input)
        stub_repository.create.assert_called_with(self.input)


class TestDelete:
    def test_repository_is_called(self):
        fake_id = 'fake_id'
        stub_repository.delete = MagicMock()
        service.delete(fake_id)
        stub_repository.delete.assert_called_once_with(fake_id)


class TestList:
    def test_repository_is_returning(self):
        sut = service.list()
        assert sut[0].title == 'fake'
