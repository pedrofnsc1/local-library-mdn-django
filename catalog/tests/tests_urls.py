from django.test import TestCase
from django.urls import reverse


class UrlsTestCase(TestCase):
    def test_local_library_index(self):
        url = reverse('catalog:index')
        self.assertEqual(url, '/catalog/')
        print('URL: PASSED')

    def test_book_url(self):
        url = reverse('catalog:book')
        self.assertEqual(url, '/catalog/book/')
        print('URL: PASSED')

    def test_book_detail(self):
        url = reverse('catalog:book-detail', kwargs={'pk': 1})
        self.assertEqual(url, '/catalog/book/1')
        print('URL: PASSED')

    def test_authors_url(self):
        url = reverse('catalog:authors')
        self.assertEqual(url, '/catalog/authors/')
        print('URL: PASSED')

    def test_authors_detail(self):
        url = reverse('catalog:author-detail', kwargs={'pk': 1})
        self.assertEqual(url, '/catalog/authors/1')
        print('URL: PASSED')

    def test_my_borrowed_books(self):
        url = reverse('catalog:my-borrowed')
        self.assertEqual(url, '/catalog/mybooks/')
        print('URL: PASSED')

    def test_all_borrowed_books(self): 
        url = reverse('catalog:all-borrowed')
        self.assertEqual(url, '/catalog/borrowed/')
        print('URL: PASSED')

    def test_renew_book(self):
        url = reverse('catalog:renew-book-librarian', kwargs={'pk':'d59d3af6-00e1-4fea-8f36-cf5e89fc5b67'}) # noqa
        self.assertEqual(url, '/catalog/book/d59d3af6-00e1-4fea-8f36-cf5e89fc5b67/renew/') # noqa
        print('URL: PASSED')

    def test_author_create(self):
        url = reverse('catalog:author-create')
        self.assertEqual(url, '/catalog/author/create/')
        print('URL: PASSED')

    def test_author_update(self):
        url = reverse('catalog:author-update', kwargs={'pk': 1})
        self.assertEqual(url, '/catalog/author/1/update/')
        print('URL: PASSED')

    def test_author_delete(self):
        url = reverse('catalog:author-delete', kwargs={'pk': 1})
        self.assertEqual(url, '/catalog/author/1/delete/')
        print('URL: PASSED')

    def test_book_create(self):
        url = reverse('catalog:book-create')
        self.assertEqual(url, '/catalog/book/create/')
        print('URL: PASSED')

    def test_book_update(self):
        url = reverse('catalog:book-update', kwargs={'pk': 1})
        self.assertEqual(url, '/catalog/book/1/update/')
        print('URL: PASSED')

    def test_book_delete(self):
        url = reverse('catalog:book-delete', kwargs={'pk': 1})
        self.assertEqual(url, '/catalog/book/1/delete/')
        print('URL: PASSED')

    def test_instance_create(self):
        url = reverse('catalog:instance-create')
        self.assertEqual(url, '/catalog/instance/create/')
        print('URL: PASSED')
