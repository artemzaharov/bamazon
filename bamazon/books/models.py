from django.db import models
from django.urls import reverse
# Create your models here.


class Author(models.Model):

    name = models.CharField('Имя', max_length=100)
    age = models.PositiveSmallIntegerField('Возраст', default=0)
    description = models.TextField('Описание')
    url = models.SlugField(max_length=160, unique=True)

    def get_absolute_url(self):
        return reverse('author_detail', kwargs={'slug': self.url})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Автор'


class Book(models.Model):

    title = models.CharField("Название", max_length=100)
    description = models.TextField('Описание')
    poster = models.ImageField('Постер', upload_to='books/')
    year = models.PositiveSmallIntegerField('Дата выхода', default=2019)
    country = models.CharField('Страна', max_length=30)
    author = models.ManyToManyField(
        Author, verbose_name='Автор', related_name='book_author')
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'slug': self.url})

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
