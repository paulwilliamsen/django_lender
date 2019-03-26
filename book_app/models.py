from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=48)
    author = models.CharField(max_length=4096)
    year = models.CharField(max_length=4096)
    date_added = models.DateTimeField(max_length=4096, )
    last_borrowed = models.DateTimeCheckMixin(max_length=4096)

    STATES = [
        ('available', 'Available'),
        ('checked_out', 'Checked Out')
    ]

    status = models.CharField(choices=STATES, default='available', max_length=48)

    def __repr__(self):
        return f'<Note: { self.title } | Status: { self.status }>'

    def __str__(self):
        return f'{ self.title } | Status: { self.status }'