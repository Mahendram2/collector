from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return f'A {self.color} {self.name}'
    
    def get_absolute_url(self):
        return reverse('toys_detail', kwargs={'pk': self.id})

class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models. CharField(max_length=100)
    description = models.TextField(max_length=100)
    age = models.IntegerField()
    toys = models.ManyToManyField(Toy)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('dogs_detail', kwargs={'dog_id': self.id})

class Feeding(models.Model):
    MEALS = (
        ('B', 'Breakfast'),
        ('L', 'Lunch'),
        ('D', 'Dinner'),
    )
    class Meta:
        ordering = ('-date',)
    
    date = models.DateField()
    meal = models.CharField(max_length=1, choices=MEALS, default=MEALS[0][0])
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_meal_display()} on {self.date}'