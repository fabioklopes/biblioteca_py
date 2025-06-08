from django.shortcuts import render

from app.models import Author, Book, Member


def index(request):
    return render(request, 'index.html')


def authors(request):
    authors = Author.objects.all()
    return render(request, 'authors.html', {'authors':authors})


def books(request):
    books = Book.objects.all()
    return render(request, 'books.html', {'books':books})


def members(request):
    members = Member.objects.all()
    return render(request, 'members.html', {'members':members})


def loans(request):
    loans = Loans.objects.all()
    return render(request, 'loans.html', {'loans':loans})


# def configurations(request):
#     loans = Configurations.objects.all()
#     return render(request, 'configurations.html', {'configurations':configurations})


