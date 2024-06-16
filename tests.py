import pytest


class TestBooksCollector:
    """Класс TestBooksCollector объединяет набор юнит-тестов, для класса BooksCollector"""

    def test_add_new_book_add_two_books(self, books_collector):
        """Тестируем добавление 2 разных книг, методом add_new_book"""
        books_collector.add_new_book('Book1')
        books_collector.add_new_book('Book2')

        assert len(books_collector.get_books_genre()) == 2

    def test_add_new_book_add_exist_books(self, books_collector):
        """Тестируем добавление уже добавленной книги, методом add_new_book"""
        books_collector.add_new_book('Book1')
        books_collector.add_new_book('Book1')

        assert len(books_collector.get_books_genre()) == 1

    def test_add_new_book_add_correct_addition_books(self, books_collector):
        """Тестируем добавление именно той книги, которую мы добавили, методом add_new_book"""
        books_collector.add_new_book('Book1')

        assert 'Book1' in books_collector.get_books_genre()

    def test_add_new_book_add_length_books(self, books_collector):
        """Тестируем добавление книги, с не разрешенном размером названия(41), методом add_new_book"""
        books_collector.add_new_book('12345678912345678912345678912345678912345')

        assert '12345678912345678912345678912345678912345' not in books_collector.get_books_genre()

    @pytest.mark.parametrize("name, genre", [("Book1", "Фантастика"), ("Book2", "Детективы"), ("Book3", "Ужасы")])
    def test_set_book_genre(self, books_collector, name, genre):
        """Тестируем добавление жанра книги, методом set_book_genre"""
        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)

        assert books_collector.get_book_genre(name) == genre

    def test_get_books_genre(self, books_collector):
        """Тестируем получение словаря books_genre, методом get_books_genre"""
        books_collector.add_new_book("Book1")
        books_collector.add_new_book("Book2")
        books_collector.set_book_genre("Book1", "Фантастика")
        books_collector.set_book_genre("Book2", "Ужасы")

        assert books_collector.get_books_genre() == {"Book1": "Фантастика", "Book2": "Ужасы"}

    def test_get_book_genre(self, books_collector):
        """Тестируем получение жанра книги по имени, методом get_book_genre"""
        books_collector.add_new_book("Book1")
        books_collector.set_book_genre("Book1", "Ужасы")

        assert books_collector.get_book_genre("Book1") == "Ужасы"

    @pytest.mark.parametrize("name, genre", [("Book1", "Фантастика"), ("Book2", "Детективы"), ("Book3", "Ужасы")])
    def test_get_books_with_specific_genre(self, books_collector, name, genre):
        """Тестируем получение списка книг определенного жанра, методом get_books_with_specific_genre"""
        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)

        assert name in books_collector.get_books_with_specific_genre(genre)

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
