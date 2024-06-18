# Класс TestBooksCollector объединяет набор модульных тестов для класса BooksCollector.

Определенные здесь методы:

1) test_add_book_in_favorites(self, books_collector) - Тестируем добавление книги в избранное, методом
   add_book_in_favorites

2) test_add_new_book_add_exist_books(self, books_collector) - Тестируем добавление уже добавленной книги, методом
   add_new_book
3) test_add_new_book_boundary_values_in_name(self, books_collector, name) - Тестируем добавление книги, с невалидным
   размером названия(0,41,60), методом add_new_book
4) test_delete_book_from_favorites(self, books_collector) - Тестируем удаления книги из избранного, методом
   delete_book_from_favorites
5) test_get_book_genre(self, books_collector) - Тестируем получение жанра книги по имени, методом get_book_genre
6) test_get_books_for_children(self, books_collector) - Тестируем получение списка книг, которые подходят детям, методом
   get_books_for_children
7) test_get_books_genre(self, books_collector) - Тестируем получение словаря books_genre, методом get_books_genre
8) test_get_books_with_specific_genre(self, books_collector) - Тестируем получение списка книг определенного жанра,
   методом get_books_with_specific_genre
9) test_get_list_of_favorites_books(self, books_collector) - Тестируем получения списка избранных книги, методом
   get_list_of_favorites_books
10) test_set_book_genre(self, books_collector) - Тестируем добавление жанра книги, методом set_book_genre
