

from catalog.models import Author, Book, BookInstance, Genre
from django.test import TestCase


class AuthorTest(TestCase):
    @classmethod
    def setUp(cls):
        Author.objects.create(first_name="Antoine", last_name="Saint-Exupéry", date_of_birth="1900-11-29", date_of_death="1944-07-31") # noqa

    def test_first_name_label(self):
        authorInfo = Author.objects.get(id=1)
        first_name = authorInfo._meta.get_field("first_name").verbose_name
        self.assertEqual(first_name, "first name")
        # print("OK")
        print("PASSED")

    def test_last_name_label(self):
        authorInfo = Author.objects.get(id=1)
        last_name = authorInfo._meta.get_field("last_name").verbose_name
        self.assertEqual(last_name, "last name")
        # print("Author Label: " + last_name)
        print("PASSED")

    def test_object_name_is_last_name_comma_first_name(self):
        author = Author.objects.get(id=1)
        expected_object_name = f'{author.last_name}, {author.first_name}'
        self.assertEqual(expected_object_name, str(author))
        # print(expected_object_name)
        print("PASSED")

    def test_date_of_birth(self):
        authorINFO = Author.objects.get(id=1)
        date_of_birth = f'{authorINFO.date_of_birth}'
        self.assertEqual(date_of_birth, "1900-11-29")
        # print("Date of Birth: " + date_of_birth)
        print("PASSED")

    def test_date_of_death(self):
        authorINFO = Author.objects.get(id=1)
        date_of_death = f'{authorINFO.date_of_death}'
        self.assertEqual(date_of_death, "1944-07-31")
        # print("Date of Birth: " + date_of_death)
        print("PASSED")


class BookTest(TestCase):
    @classmethod
    def setUp(cls):
        Genre.objects.create(name="Literatura Infanto-Juvenil")
        Book.objects.create(title="O pequeno Principe", isbn="978-8595081512") # noqa
        # Book.objects.create(title="O pequeno Principe", isbn="978-8595081512") # noqa

    def test_title_name(self):
        bookINFO = Book.objects.get(id=1)
        title = f'{bookINFO.title}'
        self.assertEqual(title, "O pequeno Principe")
        # print("Title name: " + title)
        print("PASSED")

    def test_book_genre(self):
        genreBook1 = Genre.objects.create(name="Infanto-Juvenil")
        self.assertEqual(genreBook1.name, 'Infanto-Juvenil')
        # print("Genre Book: " + genreBook1.name)
        print("PASSED")

    def test_title_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('title').max_length
        self.assertEqual(max_length, 200)
        # print("Max length - OK")
        print("PASSED")


class BookInstanceTest(TestCase):
    @classmethod
    def setUp(cls):
        BookInstance.objects.create(id="d59d3af6-00e1-4fea-8f36-cf5e89fc5b67", imprint="Capa dura – Edição padrão, 15 julho 2019", due_back="2022-07-19") # noqa

    def test_imprint(self):
        bookInstance = BookInstance.objects.get(id="d59d3af6-00e1-4fea-8f36-cf5e89fc5b67") # noqa
        imprint = f'{bookInstance.imprint}'
        self.assertEqual(imprint, "Capa dura – Edição padrão, 15 julho 2019")
        print("PASSED")

    def test_due_back_label(self):
        bookInstance = BookInstance.objects.get(id="d59d3af6-00e1-4fea-8f36-cf5e89fc5b67") # noqa
        due_back = bookInstance._meta.get_field("due_back").verbose_name
        self.assertEqual(due_back, "due back")
        # print("OK")
        print("PASSED")
