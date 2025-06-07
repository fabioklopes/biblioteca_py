from django.db import models


class Author(models.Model): 
    author_name = models.CharField(max_length=80, null=False, blank=False)

    class Meta:
        ordering = ['author_name']
    
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
    book_code = models.CharField(max_length=128, null=False, blank=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book_year = models.IntegerField(null=True, blank=True)
    book_genre = models.CharField(choices=GENRE)

    class Meta:
        ordering = ['book_name']
    
    def __str__(self):
        return self.book_name


