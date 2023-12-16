import pytest

from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        # проверяем, что добавилось именно две
        # словарь имеет длину == 2
        assert len(collector.get_books_genre()) == 2

    def test_set_book_genre_true(self):
        # создаем экземпляр (объект) класса BooksCollector
        collection = BooksCollector()
        # добавил книгу с названием Мастер и Маргарита
        collection.add_new_book('Мастер и Маргарита')
        # установил книге жанр
        collection.set_book_genre('Мастер и Маргарита', 'Фантастика')
        assert collection.get_book_genre('Мастер и Маргарита') == 'Фантастика'

    def test_add_new_book_add_two_book_with_equal_name(self):
        # тест в котором проверяется , вторая книга с одинаковым названием не добавляется в список
        # создаем экземпляр (объект) класса BooksCollector
        collection_kolobok = BooksCollector()
        # добавляем две книги
        collection_kolobok.add_new_book('Колобок')
        collection_kolobok.add_new_book('Колобок')
        # проверяем, что добавилась одна книга с одинаковвым названием
        # словарь имеет длину 1
        assert len(collection_kolobok.get_books_genre()) == 1

    @pytest.mark.parametrize('name',
                             [
                                 'Удивительное путешествие Нильса Хольгерссона с дикими гусями по Швеции',
                                 # книга больше 70 символов
                                 '',  # у книги 0 символов
                                 'Удивительное путешествие Нильса Хольгерсq'  # книга больше 41 символа
                             ])
    def test_add_new_book_add_book_name_lenght_more_40_symbols_true(self, name):
        long_book_tittle = BooksCollector()
        # добавляем книгу с длинным названием
        long_book_tittle.add_new_book(name)
        # проверка, что книги нет в словаре так как название больше 40 символов
        assert len(long_book_tittle.get_books_genre()) == 0

    def test_get_books_for_children_in_children_list_true(self):
        # проверяем, что жанр в списке для детей не должен входить в список genre_age_rating, но должен быть в списке genre
        # создал объект
        children_books = BooksCollector()
        # добавил книгу
        children_books.add_new_book('Принцесса на горошене')
        # добавил жанр
        children_books.set_book_genre('Принцесса на горошене', 'Сказка')
        # проверил, что жанр в списке для дете не должен входить в список genre_age_rating, но должен быть в списке genre
        assert children_books.get_book_genre('Принцесса на горошене') not in children_books.genre_age_rating and \
               children_books.get_book_genre('Принцесса на горошене') in children_books.genre

    def test_add_book_in_favorites_check_favourite_list_with_favorite_book_true(self):
        # создал объект
        favorite_book = BooksCollector()
        # добавил книгу
        favorite_book.add_new_book('Хоббит')
        # добавил жанр
        favorite_book.set_book_genre('Хоббит', 'Фантастика')
        # добавил книгу в список любимых книг
        favorite_book.add_book_in_favorites('Хоббит')
        # выполнил проверку, что согласно условию в словаре появился любимы фильм
        assert 'Хоббит' in favorite_book.favorites and 'Фантастика' in favorite_book.get_books_genre()['Хоббит'] and \
               len(favorite_book.favorites) == 1

    def test_delete_book_from_favorites_check_favorite_list_after_delete(self):
        # создал объект
        favorite_book = BooksCollector()
        # добавил книгу
        favorite_book.add_new_book('Бриллиянтовая рука')
        # добавил жанр
        favorite_book.set_book_genre('Бриллиаятовая рука', 'Комедия')
        # добавил книгу в список любимых книг
        favorite_book.add_book_in_favorites('Бриллиаятовая рука')
        # удалил книгу из списка с люимыми книгами
        favorite_book.delete_book_from_favorites('Бриллиаятовая рука')
        # проверил, что книги нет в списке favorite
        assert 'Бриллиаятовая рука' not in favorite_book.favorites and len(favorite_book.favorites) == 0

    def test_get_books_with_specific_genre_find_film_simple_genre(self):
        # создал объект
        specific_genre = BooksCollector()
        # наполняю словарь фильмами и привязываю по фильму жанр
        specific_genre.add_new_book('Кавказкая пленница')
        specific_genre.set_book_genre('Кавказкая пленница', 'Комедии')
        specific_genre.add_new_book('Операция Ы')
        specific_genre.set_book_genre('Операция Ы', 'Комедии')
        specific_genre.add_new_book('Служебный роман')
        specific_genre.set_book_genre('Служебный роман', 'Драмма')
        specific_genre.add_new_book('Москва слезам не верит')
        specific_genre.set_book_genre('Москва слезам не верит', 'Драмма')
        specific_genre.add_new_book('Жмурки')
        specific_genre.set_book_genre('Жмурки', 'Криминал')
        # проверяю , что жанра Комедии добавлено 2 фильма
        assert len(specific_genre.get_books_with_specific_genre('Комедии')) == 2
