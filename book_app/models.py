from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


# Create your models here.

STATES = [
    ('Available', 'Available'),
    ('Checked Out', 'Checked Out')
    ]


class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')
    title = models.CharField(max_length=48)
    author = models.CharField(max_length=4096)
    year = models.CharField(max_length=4096)
    date_added = models.DateTimeField(default=now)
    last_borrowed = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATES, default='available', max_length=48)

    def __repr__(self):
        return f'<Note: { self.title } | Status: { self.status }>'

    def __str__(self):
        return f'{ self.title } | Status: { self.status }'

