
from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title