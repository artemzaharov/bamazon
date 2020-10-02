
from django.urls import path
from . import views


urlpatterns = [
    path("", views.BooksView.as_view()),
    path("books/<slug:slug>/", views.BookDetailView.as_view(), name='book_detail'),
    path("books/author/<slug:slug>/", views.AuthorDetailView.as_view(), name='author_detail'),
]
