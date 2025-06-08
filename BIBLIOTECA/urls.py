from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index, name="index"),
    path('authors/', views.authors, name="list_all_authors"),
    path('books/', views.books, name="list_all_books"),
    path('members/', views.members, name="list_all_books"),
]
