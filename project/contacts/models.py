from django.db import models
from django.contrib.auth.models import User


PERMISSION_CHOICES = [('RO', 'ReadOnly'), ('RA', 'ReadAdd'), ('RAD', 'ReadAddDelete')]


class Contact(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, default=None)
    email = models.CharField(max_length=255, default=None)

    class Meta:
        ordering = ['id']


class Role(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    permission = models.CharField(choices=PERMISSION_CHOICES, max_length=100)
