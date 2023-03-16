from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField()
    image_url = models.CharField(max_length=350)
    blade_length = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name
    


