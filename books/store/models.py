from django.db import models


# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=7)
    author_name = models.CharField(max_length=255)

    def __str__(self):
        return f'Id {self.id}: {self.name}'
