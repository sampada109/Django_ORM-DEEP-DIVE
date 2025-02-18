from django.db import models

#user model
from django.contrib.auth.models import User

# Create your models here.

# Building Restaurant Managment System
# Tables needed -> Restaurant, User, Rating, Sales

# Restaurant Table
class Restaurant(models.Model):
    #choices
    class TypeChoices(models.TextChoices):
        INDIAN = "IN", "INDIAN"
        CHINESE = "CH", "CHINESE"
        ITALIAN = "IT", "ITALIAN"
        MEXICAN = "MX", "MEXICAN"
        FASTFOOD = "FF", "FAST FOOD"
        OTHER = "OT", "OTHER"
  
    name = models.CharField(max_length=120)
    website = models.URLField(default='')
    date_opened = models.DateField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    restaurant_type = models.CharField(max_length=2, choices=TypeChoices.choices, default='OT')

    def __str__(self):
        return self.name
    

# Ratings Table
class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"Rating: {self.rating}"
    

# Sales Table
class Sales(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null=True)
    income = models.DecimalField(max_digits=8, decimal_places=2)
    datetime = models.DateTimeField()