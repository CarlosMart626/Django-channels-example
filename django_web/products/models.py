from django.db import models


class Product(models.Model):
    uuid = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=140)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'
