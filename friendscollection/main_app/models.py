from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

DRINKS = (
    ('B', 'Beer'),
    ('S', 'Sake'),
    ('T', 'Tequila'),
    ('V', 'Vodka'),
    ('W', 'Wine'),
)

class Interest(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('interests_detail', kwargs={'pk': self.id})

# Create your models here.
class Friend(models.Model):
    name = models.CharField(max_length=150)
    background = models.CharField(max_length=100)
    likes = models.TextField(max_length=350)
    age = models.IntegerField()
    interests = models.ManyToManyField(Interest)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('details', kwargs={'friend_id': self.id})
    
    def enough_booze_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= 3

class Feeding(models.Model):
    date = models.DateField('drinking date')
    drink = models.CharField(
        max_length=1,
        choices=DRINKS,
        default=DRINKS[0][0]
    )

    friend = models.ForeignKey(Friend, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_drink_display()} on {self.date}'
    
    class Meta:
        ordering = ['-date']

class Photo(models.Model):
    url = models.CharField(max_length=250)
    friend = models.ForeignKey(Friend, on_delete=models.CASCADE)

    def __str__(self):
        return f'Photo for friend: {self.friend_id} @{self.url}'