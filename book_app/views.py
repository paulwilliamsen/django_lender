from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Book


def books_list_view(request):
    books = get_list_or_404(Book)
    context = {
        'books': books,
    }

    return render(request, 'home.html', context)


def book_detail_view(request, pk=None):
    book = get_object_or_404(Book, id=pk)
    context = {
        'book': book,
    }

    return render(request, 'home.html', context)

    #fix above route for books