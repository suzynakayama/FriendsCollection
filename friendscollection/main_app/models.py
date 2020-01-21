from django.db import models

# Create your models here.
class Friend(models.Model):
    name = models.CharField(max_length=150)
    background = models.CharField(max_length=100)
    likes = models.TextField(max_length=350)
    age = models.IntegerField()

    def __str__(self):
        return self.name