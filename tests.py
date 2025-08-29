import pytest

from main import BooksCollector

class TestBooksCollector:

    @pytest.fixture
    def collection(self):
        collection = BooksCollector()
        return collection

    def test_init_default_value_books_genre_empty_dict(self, collection):
        assert collection.books_genre == {}

    @pytest.mark.parametrize('name', ['Бабушка велела кланяться и передать, что просит прощения', 'Бабушка велела кланяться и передать, что п', 'Бабушка велела кланяться и передать, что '])
    def test_add_new_book_name_over_40_book_not_add(self, collection, name):
        collection.add_new_book(name)
        assert collection.books_genre.get(name) == None
    
    def test_set_book_genre_name_in_book_genre_set_genre(self, collection):
        name = 'Молчание ягнят'
        collection.add_new_book(name)
        collection.set_book_genre(name, 'Детективы')
        assert collection.books_genre[name] == 'Детективы'

    def test_get_book_genre_name_in_book_genre_return_genre(self, collection):
        name = 'Молчание ягнят'
        collection.add_new_book(name)
        collection.set_book_genre(name, 'Детективы')
        assert collection.get_book_genre(name) == 'Детективы'

    def test_get_books_with_specific_genre_two_books_return_one_book(self, collection):
        name1 = 'Молчание ягнят'
        collection.add_new_book(name1)
        collection.set_book_genre(name1, 'Детективы')
        name2 = 'Дюна'
        collection.add_new_book(name2)
        collection.set_book_genre(name2, 'Фантастика')
        assert 'Дюна' in collection.get_books_with_specific_genre('Фантастика')

    def test_get_books_genre_add_two_books(self, collection):
        name1 = 'Молчание ягнят'
        collection.add_new_book(name1)
        collection.set_book_genre(name1, 'Детективы')
        name2 = 'Дюна'
        collection.add_new_book(name2)
        collection.set_book_genre(name2, 'Фантастика')
        assert collection.get_books_genre() == {name1: 'Детективы', name2: 'Фантастика'}

    def test_get_books_for_children_book_age_rating_not_in_books_for_children(self, collection):
        name1 = 'Молчание ягнят'
        collection.add_new_book(name1)
        collection.set_book_genre(name1, 'Детективы')
        name2 = 'Дюна'
        collection.add_new_book(name2)
        collection.set_book_genre(name2, 'Фантастика')
        name3 = 'Красная шапочка'
        collection.add_new_book(name3)
        collection.set_book_genre(name3, 'Мультфильмы')
        assert 'Молчание ягнят' not in collection.get_books_for_children()

    def test_add_book_in_favorites_book_not_add_again(self, collection):
        name = 'Парень из колорадо'
        collection.add_new_book(name)
        collection.set_book_genre(name, 'Детективы')
        collection.add_book_in_favorites(name)
        collection.add_book_in_favorites(name)
        assert len(collection.favorites) == 1

    def test_delete_book_from_favorites_name_not_in_favorites_not_delete(self, collection):
        name = 'Парень из колорадо'
        collection.add_new_book(name)
        collection.set_book_genre(name, 'Детективы')
        collection.add_book_in_favorites(name)
        collection.delete_book_from_favorites('Дюна')
        assert collection.favorites == [name]

    def test_get_list_of_favorites_books_return_list(self, collection):
        name = 'Парень из колорадо'
        collection.add_new_book(name)
        collection.set_book_genre(name, 'Детективы')
        collection.add_book_in_favorites(name)
        assert collection.get_list_of_favorites_books() == [name]