from django.shortcuts import render


def home_view(request):
    return render(request, 'generic/home.html')


def book_view(request):
    return render(request, 'book_app/templates/book_list.html')
