from django.db import models


class Phone(models.Model):
    dbid = models.IntegerField(primary_key=True)
    name = models.TextField()
    image = models.ImageField()
    price = models.DecimalField(decimal_places=2, max_digits=15)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.TextField()