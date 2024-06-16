import pytest

from main import BooksCollector


@pytest.fixture
def books_collector():
    """Создаем фикстуру для инициализации коллекции книг"""
    return BooksCollector()
