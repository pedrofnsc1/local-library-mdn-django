import datetime

from django.views import generic
from django.shortcuts import get_object_or_404, render

from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from catalog.forms import RenewBookForm
from catalog.models import Author, Book, BookInstance, Genre

# Create your views here.

@login_required
def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    num_genre = Genre.objects.filter(name__exact='Fantasy').count()

    num_authors = Author.objects.count()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1



    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_availble': num_instances_available,
        'num_authors': num_authors,
        'num_genre': num_genre,
        'num_visits': num_visits,
    }

    return render(request, 'index.html', context=context)


class BookListView(LoginRequiredMixin, generic.ListView):
    model = Book
    paginate_by = 5
    context_object_name = 'book_list'

    # def get_queryset(self):
     #  return Book.objects.filter(title__icontains='war')[:5]
    
    template_name = 'catalog/book_list.html'


class BookDetailView(generic.DetailView):
    model = Book

    def book_detail_view(request, primary_key):
     book = get_object_or_404(Book, pk=primary_key)
     return render(request, 'catalog/book_detail.html', context={'book': book})


class AuthorListView(LoginRequiredMixin, generic.ListView):
    model = Author
    context_object_name = 'author_list'
    template_name = 'catalog/author_list.html'


class AuthorDetailView(generic.DetailView):
    model = Author

    def author_detail_view(request, primary_key):
        author = get_object_or_404(Author, pk=primary_key)
        return render(request, 'catalog/author_detail.html', context={'author': author})


class LoanedBookByUserListView(LoginRequiredMixin, generic.ListView):
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 5

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')

class LoanedAllBooksListView(PermissionRequiredMixin, generic.ListView):
    model = BookInstance
    permission_required = 'catalog.can_mark_returned'
    template_name = 'catalog/bookinstance_list_borrowed_all.html'
    paginate_by = 5 

    def get_queryset(self):
        return BookInstance.objects.filter(status__exact='o').order_by('due_back')

@login_required
@permission_required('catalog.can_mark_returned')
def renew_book_librarian(request, pk):
    book_instance = get_object_or_404(BookInstance, pk=pk)

    if request.method == 'POST':

        form = RenewBookForm(request.POST)

        if form.is_valid():
            book_instance.due_back = form.cleaned_data['renewal_date']
            book_instance.save()

            return HttpResponseRedirect(reverse('index'))
    
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date})
    
    context = {
        'form': form,
        'book_instance': book_instance,
    }

    return render(request, 'catalog/book_renew_librarian.html', context)


class AuthorCreate(PermissionRequiredMixin, generic.edit.CreateView):
    model = Author
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']
    permission_required = 'catalog.can_mark_returned'

class AuthorUpdate(PermissionRequiredMixin, generic.edit.UpdateView):
    model = Author
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']
    permission_required = 'catalog.can_mark_returned'

class AuthorDelete(generic.edit.DeleteView):
    model = Author
    success_url = reverse_lazy('authors')
    permission_required = 'catalog.can_mark_returned'


#from challenge nº9
class BookCreate(PermissionRequiredMixin, generic.edit.CreateView):
    model = Book
    fields = ['title', 'author', 'summary', 'isbn', 'genre']
    permission_required = 'catalog.can_mark_returned'


class BookUpdate(PermissionRequiredMixin, generic.edit.UpdateView):
    model = Book
    fields = '__all__'
    permission_required = 'catalog.can_mark_returned'


class BookDelete(PermissionRequiredMixin, generic.edit.DeleteView):
    model = Book
    success_url = reverse_lazy('authors')
    permission_required = 'catalog.can_mark_returned'


class BookInstanceCreate(generic.edit.CreateView):
    model = BookInstance
    fields = '__all__'
    intial = {'Book.title': ['title']}
    permission_required = 'catalog.can_mark_returned'
