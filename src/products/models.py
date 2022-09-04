from django.db import models

# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=120) #max_length = required
    description = models.TextField()
    price       = models.DecimalField(decimal_places=2, max_digits=10000)
    summary     = models.TextField(blank=False, null=False) # blank check valid field, null is database
    feature     = models.BooleanField(default=False) #null = True, default = True