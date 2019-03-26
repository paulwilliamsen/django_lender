from django.db import models

# Create your models here.

class First(models.Model):
    title = models.CharField(max_length=48)
    detail = models.CharField(max_length=4096)

    STATES = [
        ('incomplete', 'Incomplete'),
        ('complete', 'Complete')
    ]

    status = models.CharField(choices=STATES, default='incomplete', max_length=48)