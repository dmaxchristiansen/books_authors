from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('authors', views.authors),
    path('add_book', views.addBook),
    path('add_author', views.addAuthor),
    path('view_book/<number>', views.viewBook),
    path('view_author/<number>', views.viewAuthor),
    path('add_author_to_book/<number>', views.addAuthorToBook),
    path('add_book_to_author/<number>', views.addBookToAuthor),
]