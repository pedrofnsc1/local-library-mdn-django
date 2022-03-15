# A classe Form permite a manipulação de formulários no django. O Form especifica
# os campos em um formulário, seu Layout, widgets, valores iniciais, formato de 
# valores validos inseridos, mensagens de erro que podem ser geradas.
# essa classe também permite renderizar-se em modelos do sistema usando formatos
# predefinidos por ela.

import datetime
from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from catalog.models import Book, BookInstance

class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text='Enter a date between today and 4 weeks (default 3)')

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - try again.'))
        
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - Renewal more than 4 weeks ahead'))
        
        return data


## REALISA A MESMA COISA DA CLASSE ACIMA 
#class RenewalBookModelForm(ModelForm):
#    def clean_due_back(self):
#       data = self.cleaned_data['due_back']

#        if data < datetime.date.today():
#          raise ValidationError(_('Invalid date - Try again.'))
#        if data > datetime.date.today() + datetime.timedelta(weeks=4):
#           raise ValidationError(_('Invalid date - Renewal more than 4 weeks ahead))
#
#        return data
#
#    class Meta:
#        model = BookInstance
#        fields = ['due_back']
#        labels = {'due_back': _('Renewal date')}
#        help_texts = {'due_back': _('Enter a date between today and 4 weeks (default 3).')}



class BookCreateForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class BookInstanceCreateForm(ModelForm):
    class Meta:
        model = BookInstance
        fields = '__all__'