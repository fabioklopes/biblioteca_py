from django.shortcuts import render

from app.models import Author, Book


def index(request):
    return render(request, 'index.html')


def authors(request):
    authors = Author.objects.all()
    return render(request, 'authors.html', {'authors':authors})


def books(request):
    books = Book.objects.all()
    return render(request, 'books.html', {'books':books})


def members(request):
    members = Members.objects.all()
    return render(request, 'members.html', {'members':members})


