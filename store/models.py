from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/images/')
    price = models.FloatField()
    is_active = models.BooleanField(default=True)
    stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ordered_date = models.DateTimeField(auto_now=True)
    price = models.FloatField(null=True, blank=True)
    def __str__(self):
        return f"{self.product.name} + {self.user.username}"



