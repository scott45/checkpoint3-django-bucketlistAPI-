from django.db import models
from django.contrib.auth.models import User


class Bucketlist(models.Model):
    name = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_name(self):
        return self.name

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    bucketlist = models.ForeignKey(Bucketlist, on_delete=models.CASCADE)

    def get_name(self):
        return self.name

    def __str__(self):
        return self.name
