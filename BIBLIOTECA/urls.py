from os import path
from django.contrib import admin
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index, name="index"),
    path('authors/', views.authors, name="authors"),
    path('books/', views.books, name="books"),
    path('members/', views.members, name="members"),
    path('loans/', views.loans, name="loans"),
    path('configurations/', views.configurations, name="configurations"),
]
