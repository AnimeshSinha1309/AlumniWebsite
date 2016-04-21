"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User

# Models about user and profile data.

class Workplace(models.Model):
    TYPE_CHOICES = (
        ('SCH', 'School'),
        ('UNV', 'University'),
        ('BSI', 'Business'),
        ('HOS', 'Hospital'),
        ('OTH', 'Others'),
    )
    def __str__(self):
        return self.name
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=3, choices=TYPE_CHOICES)

class Alumnus(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    jobtitle = models.CharField(max_length=50)
    workplace = models.ForeignKey(Workplace)
    batch = models.IntegerField()
    class Meta:
        verbose_name_plural = "Alumni"

class Circle(models.Model):
    FRIENDSHIP_CHOICES = (
        ('FR', 'Friends'),
        ('AQ', 'Acquaintences'),
    )
    user = models.ForeignKey(Alumnus, related_name='alumnus_user')
    friend = models.ForeignKey(Alumnus, related_name='alumnus_friend')
    type = models.CharField(max_length=2, choices=FRIENDSHIP_CHOICES)

# Models about event and program data

class Event(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()