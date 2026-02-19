from main import BooksCollector
import pytest

class TestBooksCollector:

    valid_book_names = [
        'Бегающий сейф',
        'С',
        'Се',
        '39 симв. Сергей Вишневский. Бегающий се',
        '40 симв. Сергей Вишневский. Бегающий сей'
    ]

    @pytest.mark.parametrize('book_name', valid_book_names)
    def test_add_new_book_with_valid_name_success(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert book_name in collector.books_genre
        print(book_name)

    invalid_book_names = [
        '',
        '41 симв. Сергей Вишневский. Бегающий сейф',
        '42 симв. Сергей Вишневский. Бегающий сейф ',
        '60 симв. Сергей Вишневский. Бегающий сейф. Сергей Вишневский'
    ]

    @pytest.mark.parametrize('book_name', invalid_book_names)
    def test_add_new_book_with_invalid_name_fault(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert book_name not in collector.books_genre

    def test_add_new_book_duplicate_fault(self):
        collector = BooksCollector()
        collector.add_new_book('Играть чтобы жить')
        collector.add_new_book('Играть чтобы жить')
        assert len(collector.books_genre) == 1

    def test_add_new_book_added_book_without_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Господство клана Неспящих')
        assert collector.books_genre['Господство клана Неспящих'] == ''

    def test_set_book_genre_valid_genre_success(self):
        collector = BooksCollector()
        collector.add_new_book('Макс Глебов. Бригадный генерал')
        collector.set_book_genre('Макс Глебов. Бригадный генерал', 'Фантастика')
        assert collector.books_genre['Макс Глебов. Бригадный генерал'] == 'Фантастика'

    def test_set_book_genre_unknown_book_fault(self):
        collector = BooksCollector()
        collector.set_book_genre('Неизвестная книга', 'Фантастика')
        assert 'Неизвестная книга' not in collector.books_genre

    def test_set_book_genre_unknown_genre_fault(self):
        collector = BooksCollector()
        collector.add_new_book('Дмитрий Рус. Играть чтобы Жить')
        collector.set_book_genre('Дмитрий Рус. Играть чтобы Жить', 'ЛитРПГ')
        assert collector.books_genre['Дмитрий Рус. Играть чтобы Жить'] == ''

    def test_get_book_genre_known_name_success(self):
        collector = BooksCollector()
        collector.add_new_book('Макс Глебов. Блюстители хаоса')
        collector.set_book_genre('Макс Глебов. Блюстители хаоса', 'Фантастика')
        assert collector.get_book_genre('Макс Глебов. Блюстители хаоса') == 'Фантастика'

    def test_get_book_genre_unknown_name_fault(self):
        collector = BooksCollector()
        assert collector.get_book_genre('Гарри поттер') == None


    def test_get_books_with_specific_genre_found(self):
        book_names_with_genre = [
            ['Дюна','Фантастика'],
            ['Приключения Шерлока Холмса','Детективы'],
            ['Оно','Ужасы'],
            ['Гиперион','Фантастика'],
            ['Бригадный генерал','Фантастика'],
            ['12 стульев','Комедии']
        ]
        collector = BooksCollector()
        for i in book_names_with_genre:
            collector.add_new_book(i[0])
            collector.set_book_genre(i[0],i[1])
        assert collector.get_books_with_specific_genre('Фантастика') == ['Дюна', 'Гиперион', 'Бригадный генерал']

    def test_get_books_with_specific_genre_empty_genre_not_found(self):
        book_names_with_genre = [
            ['Дюна','Фантастика'],
            ['Приключения Шерлока Холмса','Детективы'],
            ['Оно','Ужасы'],
            ['Гиперион','Фантастика'],
            ['Бригадный генерал','Фантастика'],
            ['12 стульев','Комедии']
        ]
        collector = BooksCollector()
        for i in book_names_with_genre:
            collector.add_new_book(i[0])
            collector.set_book_genre(i[0],i[1])
        assert collector.get_books_with_specific_genre('Мультфильмы') == []

    def test_get_books_with_specific_genre_invalid_genre_fault(self):
        collector = BooksCollector()
        assert collector.get_books_with_specific_genre('ЛитРПГ') == []

    def test_get_books_genre_valid_books_success(self):
        book_names_with_genre = [
            ['Дюна', 'Фантастика'],
            ['Приключения Шерлока Холмса', 'Детективы']
        ]
        collector = BooksCollector()
        for i in book_names_with_genre:
            collector.add_new_book(i[0])
            collector.set_book_genre(i[0], i[1])
        assert collector.get_books_genre() == {'Дюна': 'Фантастика', 'Приключения Шерлока Холмса': 'Детективы'}

    def test_get_books_for_children_valid_names_success(self):
        book_names_with_genre = [
            ['Гарри Поттер','Фантастика'],
            ['Приключения Шерлока Холмса','Детективы'],
            ['Оно','Ужасы'],
            ['Винни Пух','Мультфильмы']
        ]
        collector = BooksCollector()
        for i in book_names_with_genre:
            collector.add_new_book(i[0])
            collector.set_book_genre(i[0],i[1])
        assert collector.get_books_for_children() == ['Гарри Поттер', 'Винни Пух']

    def test_add_book_in_favorites_valid_name_success(self):
        collector = BooksCollector()
        collector.add_new_book('Артём Каменистый. Самый странный нуб')
        collector.add_book_in_favorites('Артём Каменистый. Самый странный нуб')
        assert 'Артём Каменистый. Самый странный нуб' in collector.favorites

    def test_delete_book_from_favorites_valid_name_success(self):
        collector = BooksCollector()
        collector.add_new_book('Дмитрий Распопов. Лучшая пятерка')
        collector.add_book_in_favorites('Дмитрий Распопов. Лучшая пятерка')
        collector.delete_book_from_favorites('Дмитрий Распопов. Лучшая пятерка')
        assert 'Дмитрий Распопов. Лучшая пятерка' not in collector.favorites
    
    def test_get_list_of_favorites_books_valid_name_success(self):
        collector = BooksCollector()
        collector.add_new_book('Дмитрий Распопов. Жить заново')
        collector.add_book_in_favorites('Дмитрий Распопов. Жить заново')
        collector.add_new_book('Василий Маханенко. Путь шамана')
        collector.add_book_in_favorites('Василий Маханенко. Путь шамана')
        assert collector.favorites == ['Дмитрий Распопов. Жить заново', 'Василий Маханенко. Путь шамана']
