from django.db import models

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class City(models.Model):
    pass


class Post(models.Model):
    pass
