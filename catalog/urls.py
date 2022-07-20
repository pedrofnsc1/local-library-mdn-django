from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.index, name='index'),
    path('book/', views.BookListView.as_view(), name='book'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('authors/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'), # noqa:
]

urlpatterns += [
    path('mybooks/', views.LoanedBookByUserListView.as_view(), name='my-borrowed'), # noqa:
    path(r'borrowed/', views.LoanedAllBooksListView.as_view(), name='all-borrowed'), # noqa:
]


urlpatterns += [
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'), # noqa:
]

urlpatterns += [
    path('author/create/', views.AuthorCreate.as_view(), name='author-create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author-update'), # noqa:
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author-delete'), # noqa:
]

urlpatterns += [
    path('book/create/', views.BookCreate.as_view(), name='book-create'),
    path('book/<int:pk>/update/', views.BookUpdate.as_view(), name='book-update'), # noqa:
    path('book/<int:pk>/delete/', views.BookDelete.as_view(), name='book-delete'), # noqa:
]

urlpatterns += [
    path('instance/create/', views.BookInstanceCreate.as_view(), name='instance-create'), # noqa:
]