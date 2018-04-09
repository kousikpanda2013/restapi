from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=140)
    last_name = models.CharField(max_length=60)
    company = models.CharField(max_length=100)
    age = models.IntegerField()
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=40)
    pin = models.IntegerField()
    email = models.EmailField(
        max_length=70, blank=True, null=True, unique=True)
    web = models.CharField(max_length=1000)

    def __str__(self):
        return self.first_name + self.last_name
