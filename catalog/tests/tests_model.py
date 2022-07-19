from catalog.models import Author, Book, Genre
from django.test import TestCase


class AuthorTest(TestCase):
    @classmethod
    def setUp(cls):
        Author.objects.create(first_name="Antoine", last_name="Saint-Exupéry", date_of_birth="1900-11-29", date_of_death="1944-07-31") # noqa

    def test_first_name_label(self):
        authorInfo = Author.objects.get(id=1)
        first_name = authorInfo._meta.get_field("first_name").verbose_name
        self.assertEqual(first_name, "first name")
        print("OK")

    def test_last_name_label(self):
        authorInfo = Author.objects.get(id=1)
        last_name = authorInfo._meta.get_field("last_name").verbose_name
        self.assertEqual(last_name, "last name")
        print("Author Label: " + last_name)

    def test_object_name_is_last_name_comma_first_name(self):
        author = Author.objects.get(id=1)
        expected_object_name = f'{author.last_name}, {author.first_name}'
        self.assertEqual(expected_object_name, str(author))
        print(expected_object_name)

    def test_date_of_birth(self):
        authorINFO = Author.objects.get(id=1)
        date_of_birth = f'{authorINFO.date_of_birth}'
        self.assertEqual(date_of_birth, "1900-11-29")
        print("Date of Birth: " + date_of_birth)

    def test_date_of_death(self):
        authorINFO = Author.objects.get(id=1)
        date_of_death = f'{authorINFO.date_of_death}'
        self.assertEqual(date_of_death, "1944-07-31")
        print("Date of Birth: " + date_of_death)


class BookTest(TestCase):
    @classmethod
    def setUp(cls):
        Genre.objects.create(name="Literatura Infanto-Juvenil")
        Book.objects.create(title="O pequeno Principe", isbn="978-8595081512") # noqa
        #Book.objects.create(title="O pequeno Principe", isbn="978-8595081512") # noqa

    def test_title_name(self):
        bookINFO = Book.objects.get(id=1)
        title = f'{bookINFO.title}'
        self.assertEqual(title, "O pequeno Principe")
        print("Title name: " + title)

    def test_book_genre(self):
        # bookINFO = Book.objects.create(
        #     title="O pequeno Principe", 
        #     isbn="978-8595081512") # noqa
        genreBook1 = Genre.objects.create(name="Infanto-Juvenil")

        #bookINFO = Book.objects.get(id=1)
        #title = f'{bookINFO.genre}'
        self.assertEqual(genreBook1.name, 'Infanto-Juvenil')
        print("Genre Book: " + genreBook1.name)

    def test_title_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('title').max_length
        self.assertEquals(max_length, 200)
        print("Max length - OK")

    def test_title_is_null(self):
        book = Book.objects.get(id=1)
        is_null = book._meta.get_field('title').null
        self.assertEquals(bool(is_null), False)
        print("Title: " + is_null)
