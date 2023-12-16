# qa_python
test_add_new_book_add_two_books() - проверка, что в словаре добавлено два фильма
test_set_book_genre_true() - проверка, что в словарь добавлена определенная книга и жанр
test_add_new_book_add_two_book_with_equal_name() - проверка , если добавлены книги с одинаковыми названиями, будет отображаться только одна
test_add_new_book_add_book_name_lenght_more_40_symbols_true() - проверка, параметризированный тест, где проверяется что книги с некорректными названиями не добавляются в словарь
test_get_books_for_children_in_children_list_true() - проверка, что жанр в списке для детей не должен входить в список genre_age_rating, но должен быть в списке genre
test_add_book_in_favorites_check_favourite_list_with_favorite_book_true() - проверка, что любимый фильм добавлен в список favorite
test_delete_book_from_favorites_check_favorite_list_after_delete() - проверка, из списка favorite удален любимый фильм, список пуст
