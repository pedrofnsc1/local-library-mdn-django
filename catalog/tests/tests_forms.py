import datetime
from django.test import TestCase
from catalog.forms import RenewBookForm


class RenewBookFormTest(TestCase):
    def test_renew_book_date_label(self):
        form = RenewBookForm()
        self.assertTrue(form.fields['renewal_date'].label == None or form.fields['renewal_date'].label == 'renewal date') # noqa
        print('PASSED')

    def test_renew_with_invalid_date(self):
        date = datetime.date.today() - datetime.timedelta(days=1)
        renew = RenewBookForm(data={'renewal_date': date})
        self.assertFalse(renew.is_valid())
        print('PASSED')

    def test_renew_with_more_than_4_weeks(self):
        date = datetime.date.today() + datetime.timedelta(days=1) + datetime.timedelta(weeks=4) # noqa
        renew = RenewBookForm(data={'renewal_date': date})
        self.assertFalse(renew.is_valid())
        print('PASSED')
