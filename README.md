Реализованные тесты:
test_add_new_book_add_two_books - добавление двух книг корректно увеличивает словарь books_genre
test_init_created_empty_books_genre	- при инициализации словарь books_genre создаётся пустым
test_init_created_empty_favorites_list	- при инициализации список favorites создаётся пустым
test_init_created_genre_list	- при инициализации список допустимых жанров содержит все 5 жанров
test_init_created_genre_age_rating_list	- при инициализации список возрастных жанров содержит Ужасы и Детективы
test_set_book_genre_added_genre_for_book	- установка жанра для существующей книги работает корректно для всех допустимых жанров
test_get_books_with_specific_genre_retutn_two_books_for_same_genre	- поиск книг по жанру возвращает все книги с указанным жанром
test_get_books_genre_return_two_books	- метод get_books_genre() возвращает полный словарь с книгами и их жанрами
test_get_books_for_children_return_list_of_books	- фильтрация книг для детей возвращает книги из допустимых жанров (не Ужасы и не Детективы)
test_get_books_for_children_return_empty_list	- фильтрация книг для детей возвращает пустой список, если все книги имеют возрастной рейтинг
test_add_book_in_favorites_add_two_books	- добавление двух книг в избранное корректно увеличивает список избранного
test_add_book_in_favorites_not_add_book_repeated	- повторное добавление одной и той же книги в избранное не создаёт дубликатов
test_delete_book_from_favorites_deleted_book_from_favorites_list	- удаление книги из избранного работает корректно
test_get_list_of_favorites_books_return_list_of_books	- метод get_list_of_favorites_books() возвращает актуальный список избранных книг
