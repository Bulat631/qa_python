# qa_python

# def collection(self) - создаем фикстуру для создания объекта класса

# def test_init_default_value_books_genre_empty_dict(self, collection) - проверил что при создании объекта класса создался пустой список в переменной

# @pytest.mark.parametrize('name', ['Бабушка велела кланяться и передать, что просит прощения', 'Бабушка велела кланяться и передать, что п', 'Бабушка велела кланяться и передать, что '])
# def test_add_new_book_name_over_40_book_not_add(self, collection, name) - проверил что при добавлении книги с названием более 40 символов, она не добавляется. С помощью параметризации прошелся также по граничным значениям
    
# def test_set_book_genre_name_in_book_genre_set_genre(self, collection) - проверил что жанр добавляется при если книга есть в словаре books_genre

# def test_get_book_genre_name_in_book_genre_return_genre(self, collection) - проверил что метод возвращает верный жанр книги

# def test_get_books_with_specific_genre_two_books_return_one_book(self, collection) - проверил что при добавлении двух книг разных жанров метод возращает нужную книгу

# def test_get_books_genre_add_two_books(self, collection) - проверил что метод возвращает словарь books_genre в задуманной форме

# def test_get_books_for_children_book_age_rating_not_in_books_for_children(self, collection) - проверил что метод исключает книги которые не соответствуют возрастному ограничению

# def test_add_book_in_favorites_book_not_add_again(self, collection) - проверил что метод не позволяет добавить одну книги 2 раза

# def test_delete_book_from_favorites_name_not_in_favorites_not_delete(self, collection) - проверил что метод не срабатывает если передать книгу которой нет в избранном

# def test_get_list_of_favorites_books_return_list(self, collection) - проверил что метод успешно возращает список избранных книг в нужной формате
    
# def test_add_new_book_add_one_book(self, collection) - проверил что метод успешно добавляет книгу в словарь books_genre

# def test_add_book_in_favorites_add_one_book_value_added(self, collection) - проверил что метод успешно добавил книгу в избранное
