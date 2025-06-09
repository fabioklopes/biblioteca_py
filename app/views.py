import datetime
from datetime import timedelta
from django.shortcuts import render
from app.models import Book, Member, Loan


def index(request):
    total_books = Book.objects.all().count()
    total_members = Member.objects.all().count()
    total_loans = Loan.objects.all().count()
    # loan_date = Loan.objects.get().loan_date.strftime("%d/%m/%Y %H:%M:%S")

    # if loan_date:
    #     expire_date = loan_date + timedelta(days=7)

    context = {
        'total_books': total_books,
        'total_members': total_members,
        'total_loans': total_loans,
        # 'expire_date': expire_date,
    }
    return render(request, 'index.html', context)


def authors(request):
    return render(request, 'authors.html')


def books(request):
    return render(request, 'index.html')


def members(request):
    return render(request, 'members.html')


def loans(request):
    return render(request, 'loans.html')

# def configurations(request):
#     loans = Configurations.objects.all()
#     return render(request, 'configurations.html', {'configurations':configurations})
