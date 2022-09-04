from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=120) #max_length = required
    description = models.TextField()
    price       = models.DecimalField(decimal_places=2, max_digits=10000)
    summary     = models.TextField(blank=False, null=False) # blank check valid field, null is database
    feature     = models.BooleanField(default=False) #null = True, default = True


    def get_absolute_url(self):
        return f"/products/{self.id}"

    # using keyword argument <id: id>
    # reverse url => make url dynamic, when you change url in url.py, app will update automate
    
    # def get_absolute_url(self):
    #     return reverse("products:product-detail", kwargs={"id": self.id})
