from django.db import models

# Create your models here.
class Inventory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    image = models.ImageField(upload_to='inventory/images/')
    def __str__(self):
        return self.name