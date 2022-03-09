from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

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