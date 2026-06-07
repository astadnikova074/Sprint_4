from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_init_created_empty_books_genre(self):
        collector = BooksCollector()

        assert collector.books_genre == {}
    
    def test_init_created_empty_favorites_list(self):
        collector = BooksCollector()

        assert collector.favorites == []
    
    def test_init_created_genre_list(self):
        collector = BooksCollector()

        assert collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
    
    def test_init_created_genre_age_rating_list(self):
        collector = BooksCollector()

        assert collector.genre_age_rating == ['Ужасы', 'Детективы']

    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']) 
    def test_set_book_genre_added_genre_for_book(self,genre):
        collector = BooksCollector()

        collector.add_new_book('Книга')
        collector.set_book_genre('Книга',genre)

        assert collector.get_book_genre('Книга') == genre

    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']) 
    def test_get_books_with_specific_genre_retutn_two_books_for_same_genre(self,genre):
        collector = BooksCollector()

        collector.add_new_book('Книга 1')
        collector.set_book_genre('Книга 1',genre)
        collector.add_new_book('Книга 2')
        collector.set_book_genre('Книга 2',genre)

        assert collector.get_books_with_specific_genre(genre) == ['Книга 1', 'Книга 2']

    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']) 
    def test_get_books_genre_return_two_books(self,genre):
        collector = BooksCollector()
    
        collector.add_new_book('Книга 1')
        collector.set_book_genre('Книга 1',genre)
        collector.add_new_book('Книга 2')
        collector.set_book_genre('Книга 2',genre)

        assert collector.get_books_genre() == {
            "Книга 1":genre,
            "Книга 2":genre
        }
    
    @pytest.mark.parametrize('genre', ['Фантастика', 'Мультфильмы', 'Комедии']) 
    def test_get_books_for_children_return_list_of_books(self,genre):
        collector = BooksCollector()
    
        collector.add_new_book('Книга 1')
        collector.set_book_genre('Книга 1',genre)
        collector.add_new_book('Книга 2')
        collector.set_book_genre('Книга 2',genre)

        assert collector.get_books_for_children() == ['Книга 1', 'Книга 2']

    @pytest.mark.parametrize('genre', ['Ужасы', 'Детективы']) 
    def test_get_books_for_children_return_empty_list(self,genre):
        collector = BooksCollector()
    
        collector.add_new_book('Книга 1')
        collector.set_book_genre('Книга 1',genre)
        collector.add_new_book('Книга 2')
        collector.set_book_genre('Книга 2',genre)

        assert collector.get_books_for_children() == []
    
    def test_add_book_in_favorites_add_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Книга 1')
        collector.add_book_in_favorites('Книга 1')
        collector.add_new_book('Книга 2')
        collector.add_book_in_favorites('Книга 2')

        assert len(collector.get_list_of_favorites_books()) == 2
    
    def test_add_book_in_favorites_not_add_book_repeated(self):
        collector = BooksCollector()

        collector.add_new_book('Книга 1')
        collector.add_book_in_favorites('Книга 1')
        collector.add_book_in_favorites('Книга 1')

        assert collector.get_list_of_favorites_books() == ['Книга 1']
    
    def test_delete_book_from_favorites_deleted_book_from_favorites_list(self):
        collector = BooksCollector()

        collector.add_new_book('Книга 1')
        collector.add_book_in_favorites('Книга 1')
        collector.add_new_book('Книга 2')
        collector.add_book_in_favorites('Книга 2')
        collector.delete_book_from_favorites('Книга 2')

        assert collector.get_list_of_favorites_books() == ['Книга 1']
    
    def test_get_list_of_favorites_books_return_list_of_books(self):
        collector = BooksCollector()

        collector.add_new_book('Книга 1')
        collector.add_book_in_favorites('Книга 1')
        collector.add_new_book('Книга 2')
        collector.add_book_in_favorites('Книга 2')

        assert collector.get_list_of_favorites_books() == ['Книга 1', 'Книга 2']
        