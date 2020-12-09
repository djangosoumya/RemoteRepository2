from django.db import models

class FriendsData(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    mobile = models.BigIntegerField()
    email = models.EmailField(max_length=50)
    gender = models.CharField(max_length=10)
    location = models.CharField(max_length=20)
