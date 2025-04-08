from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Items(models.Model):


    MEALS_TYPES = (
        ("starters","Starters"),
        ("salads","Salads"),
        ("main dishes","Main Dishes"),
        ("desserts","Desserts")
    )

    STATUS = (
        (0,"Unavailable"),
        (1,"Available")
    )
    meals = models.CharField(max_length=1000)
    meals_description = models.CharField(max_length=2000)
    price = models.DecimalField(decimal_places=5,max_digits=200)
    meals_type = models.CharField(choices= MEALS_TYPES)
    author_cook_user = models.ForeignKey(User,on_delete=models.PROTECT) #This jusify a many to one relationship btw the meals and cook , one cook can create many meals and update same on portal with admin interface
    status = models.IntegerField(choices = STATUS, default=1)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now= True)

    def __str__(self):
        self.meals