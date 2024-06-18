import pytest


class TestBooksCollector:
    """Класс TestBooksCollector объединяет набор юнит-тестов, для класса BooksCollector"""

    def test_add_new_book_add_exist_books(self, books_collector):
        """Тестируем добавление уже добавленной книги, методом add_new_book"""
        books_collector.add_new_book('Book1')
        books_collector.add_new_book('Book1')
        assert len(books_collector.get_books_genre()) == 1

    names_valid = ['1', "12345678912345678912", '1234567891234567891234567891234567891234']

    @pytest.mark.parametrize('name', names_valid)
    def test_add_new_book_boundary_values_in_name(self, books_collector, name):
        """Тестируем добавление книги, с валидным размером названия(1,20.40), методом add_new_book"""
        books_collector.add_new_book(name)
        assert name in books_collector.get_books_genre()

    names_invalid = ['', '12345678912345678912345678912345678912345', '12345678912345678912345678912345678912453523243']

    @pytest.mark.parametrize('name', names_invalid)
    def test_add_new_book_boundary_values_in_name(self, books_collector, name):
        """Тестируем добавление книги, с невалидным размером названия(0,41,60), методом add_new_book"""
        books_collector.add_new_book(name)
        assert name not in books_collector.get_books_genre()

    def test_set_book_genre(self, books_collector):
        """Тестируем добавление жанра книги, методом set_book_genre"""
        books_collector.add_new_book("Book1")
        books_collector.set_book_genre("Book1", "Фантастика")
        assert books_collector.get_book_genre("Book1") == "Фантастика"

    def test_get_books_genre(self, books_collector):
        """Тестируем получение словаря books_genre, методом get_books_genre"""
        books_collector.add_new_book("Book1")
        books_collector.set_book_genre("Book1", "Фантастика")
        assert books_collector.get_books_genre() == {"Book1": "Фантастика"}

    def test_get_book_genre(self, books_collector):
        """Тестируем получение жанра книги по имени, методом get_book_genre"""
        books_collector.add_new_book("Book1")
        books_collector.set_book_genre("Book1", "Ужасы")
        assert books_collector.get_book_genre("Book1") == "Ужасы"

    def test_get_books_with_specific_genre(self, books_collector):
        """Тестируем получение списка книг определенного жанра, методом get_books_with_specific_genre"""
        books_collector.add_new_book("Book1")
        books_collector.set_book_genre("Book1", "Фантастика")
        assert "Book1" in books_collector.get_books_with_specific_genre("Фантастика")

    def test_get_books_for_children(self, books_collector):
        """Тестируем получение списка книг, которые подходят детям, методом get_books_for_children"""
        books_collector.add_new_book("Book1")
        books_collector.add_new_book("Book2")
        books_collector.set_book_genre("Book1", "Фантастика")
        books_collector.set_book_genre("Book2", "Ужасы")
        assert books_collector.get_books_for_children() == ["Book1"]

    def test_add_book_in_favorites(self, books_collector):
        """Тестируем добавление книги в избранное, методом add_book_in_favorites"""
        books_collector.add_new_book("Book1")
        books_collector.add_book_in_favorites("Book1")
        assert "Book1" in books_collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self, books_collector):
        """Тестируем удаления книги из избранного, методом delete_book_from_favorites"""
        books_collector.add_new_book("Book1")
        books_collector.add_book_in_favorites("Book1")
        books_collector.delete_book_from_favorites("Book1")
        assert "Book1" not in books_collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books(self, books_collector):
        """Тестируем получения списка избранных книги, методом get_list_of_favorites_books"""
        books_collector.add_new_book("Book1")
        books_collector.add_new_book("Book2")
        books_collector.add_new_book("Book3")
        books_collector.add_book_in_favorites("Book1")
        books_collector.add_book_in_favorites("Book2")
        assert books_collector.get_list_of_favorites_books() == ["Book1", "Book2"]
