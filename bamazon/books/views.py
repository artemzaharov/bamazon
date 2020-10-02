from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book, Author


class BooksView(ListView):

    model = Book
    queryset = Book.objects.all()


class BookDetailView(DetailView):

    model = Book
    slug_field = 'url'


class AuthorDetailView(DetailView):

    model = Author
    slug_field = 'url'