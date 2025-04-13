from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    #genres
    releaseDate = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    numPages = models.IntegerField()
    bookCover = models.ImageField()
    isAvail = models.BooleanField()
    def __str__(self):
        return f"{self.name}"
    
class Genre(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class BookGenre(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

class Translator(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    birthDate = models.DateField()

    def __str__(self):
        return f"{self.name}"
    
class BookTranslator(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    translator = models.ForeignKey(Translator, on_delete=models.CASCADE)


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    comment = models.CharField(max_length=300)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)