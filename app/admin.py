from django.contrib import admin

from app.models import Author, Genre, Book, Member, Loan

admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(Member)
admin.site.register(Loan)