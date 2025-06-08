from django.db import models


class Author(models.Model): 
    author_name = models.CharField(max_length=80, null=False, blank=False)

    class Meta:
        ordering = ['author_name']
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
    
    def __str__(self):
        return self.author_name


class Genre(models.Model):
    genre_title = models.CharField(max_length=25, unique=True, null=False, blank=False)

    class Meta:
        ordering = ['genre_title']
        verbose_name = "Gênero"
        verbose_name_plural = "Gêneros"
    
    def __str__(self):
        return self.genre_title


class Book(models.Model):
    book_name = models.CharField(max_length=80, null=False, blank=False)
    book_code = models.CharField(max_length=128, unique=True, null=False, blank=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book_year = models.IntegerField(null=True, blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    class Meta:
        ordering = ['book_name']
        verbose_name = "Livro"
        verbose_name_plural = "Livros"
    
    def __str__(self):
        return self.book_name


class Member(models.Model):
    TYPE = [
        ('default', 'Padrão'),
        ('social', 'Social'),
        ('public', 'Público'),
    ]
    member_name = models.CharField(max_length=80, null=False, blank=False)
    member_email = models.EmailField(max_length=80, unique=True, null=False, blank=False)
    member_phone = models.CharField(max_length=11, null=False, blank=False)
    member_type = models.CharField(choices=TYPE)
    create_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    member_active = models.BooleanField(default=True)

    class Meta:
        ordering =['member_name']
        verbose_name = "Membro"
        verbose_name_plural = "Membros"
    
    def __str__(self):
        return self.member_name


class Loan(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    loan_date = models.DateTimeField()
    return_date = models.DateTimeField()

    class Meta:
        ordering = ["loan_date"]
        verbose_name = "Empréstimo"
        verbose_name_plural = "Empréstimos"
    
    def __str__(self):
        return f"{self.member.member_name} - {self.loan_date.strftime('%d/%m/%Y')} às {self.loan_date.strftime('%H:%M:%S')}"


