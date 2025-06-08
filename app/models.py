from django.db import models


class Author(models.Model): 
    author_name = models.CharField(max_length=80, null=False, blank=False)

    class Meta:
        ordering = ['author_name']
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
    
    def __str__(self):
        return self.author_name


class Book(models.Model):
    GENRE = [
        ('romance', 'Romance'),
        ('poesia', 'Poesia'),
        ('ficcao_cientifica', 'Ficção Científica'),
        ('fantasia', 'Fantasia'),
        ('suspense', 'Suspense'),
        ('misterio', 'Mistério'),
        ('terror', 'Terror'),
        ('cronica', 'Crônica'),
        ('novela', 'Novela'),
    ]

    book_name = models.CharField(max_length=80, null=False, blank=False)
    book_code = models.CharField(max_length=128, unique=True, null=False, blank=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book_year = models.IntegerField(null=True, blank=True)
    book_genre = models.CharField(choices=GENRE)

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
    member_phone = models.CharField(max_length=11, unique=True, null=False, blank=False)
    member_type = models.CharField(choices=TYPE)
    create_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    member_active = models.BooleanField(default=False)

    class Meta:
        ordering =['member_name']
        verbose_name = "Membro"
        verbose_name_plural = "Membros"
    
    def __str__(self):
        return self.member_name