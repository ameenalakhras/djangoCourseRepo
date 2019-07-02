from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)
    user_id = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + " " + self.second_name


class Book(models.Model):
    name = models.CharField(max_length=100)
    author_id = models.ForeignKey(to=Author, on_delete=models.CASCADE)

    def __str__(self):
        return f"'{self.name}' for '{self.author_id.first_name} {self.author_id.second_name}'"