from django.db import models
from django.contrib.auth.models import User
from django.core .validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Account(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)



class Review(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, default=1)
    rating = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    title= models.CharField(max_length=64)
    text = models.CharField(max_length=10000)
    date = models.DateTimeField()
    company = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField()

    def __str__(self):
        return '{}: {}'.format(self.id, self.rating, self.date, self.title, self.text)