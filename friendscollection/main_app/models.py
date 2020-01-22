from django.db import models
from django.urls import reverse

DRINKS = (
    ('B', 'Beer'),
    ('S', 'Sake'),
    ('T', 'Tequila'),
    ('V', 'Vodka'),
    ('W', 'Wine'),
)

# Create your models here.
class Friend(models.Model):
    name = models.CharField(max_length=150)
    background = models.CharField(max_length=100)
    likes = models.TextField(max_length=350)
    age = models.IntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('details', kwargs={'friend_id': self.id})

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