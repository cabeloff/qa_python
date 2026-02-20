#qa_python

tests.py - написаны юнит тесты для коллектора книг
-------------------------------------------------------------------------------------------------------------------------------
Успешное добавление книг с валидными именами: test_add_new_book_with_valid_name_success
Ошибка добавления книг с невалидными именами: test_add_new_book_with_invalid_name_fault
Ошибка повторного добавления существующей книги: test_add_new_book_duplicate_fault
Жанр добавленной новой книги отсутствует: test_add_new_book_added_book_without_genre
Успешное присвоение жанра существующей книге: test_set_book_genre_valid_genre_success
Ошибка присвоения жанра неизвестной книге: test_set_book_genre_unknown_book_fault
Ошибка присвоения жанра не из списка доступных жанров: test_set_book_genre_unknown_genre_fault
Успешное получение жанра по названию известной книги: test_get_book_genre_known_name_success
Ошибка получения жанра по неизветсной книге: test_get_book_genre_unknown_name_fault
Успешное получение списка книг по определенным жанрам: test_get_books_with_specific_genre_found
Ошибка получения списка книг при отсутствии книг определенного жанра : test_get_books_with_specific_genre_empty_genre_not_found
Ошибка получения списка книг по невалидным жанрам: test_get_books_with_specific_genre_invalid_genre_fault
Успешное получение словаря книг с жанрами: test_get_books_genre_valid_books_success
Успешное получение книг подходящих детям: test_get_books_for_children_valid_names_success
Успешное добавление книг в избранное: test_add_book_in_favorites_valid_name_success
Ошибка добавления в избранное книги, отсутствующей в коллекции: test_add_book_in_favorites_unknown_book_fault
Успешное удаление книг из избранного: test_delete_book_from_favorites_valid_name_success
Успешное получение списка избранных книг: test_get_list_of_favorites_books_valid_name_success
