from django.test import TestCase
from catalog.forms import RenewBookForm, BookCreateForm, BookInstanceCreateForm


class RenewBookFormTest(TestCase):
    def test_renew_book_date_label(self):
        form = RenewBookForm()
        self.assertTrue(form.fields['renewal_date'].label == None or form.fields['renewal_date'].label == 'renewal date') # noqa
        print(form.fields['renewal_date'].label)
    
    def test_renew_with_invalid_date(self):
        ...
    
    def test_renew_with_more_than_4_weeks(self):
        ...
    