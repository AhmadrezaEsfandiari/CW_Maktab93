from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    publication_date = models.DateField()
    ISBN = models.CharField(max_length=100)
    availability_status = models.BooleanField()

class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField()
    email = models.EmailField()

class Member(models.Model):
    class StatusChoices(models.TextChoices):
        ACTIVE = ('ac', 'active')
        DEACTIVATE = ('dc', 'deactivate')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact_number = models.IntegerField()
    address = models.CharField(max_length=200)
    status = models.CharField(max_length=2, choices=StatusChoices.choices,
    default=StatusChoices.DEACTIVATE)


