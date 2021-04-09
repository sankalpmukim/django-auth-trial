from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    popularity = models.CharField(max_length=50)

    def __str__(self):
        return self.popularity

