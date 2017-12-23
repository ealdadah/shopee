from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    cost = models.IntegerField()
    category = models.ManyToManyField(Category, related_name="products")
    numberOfProduct = models.IntegerField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    product = models.ManyToManyField(Product, related_name="orders")
    total_cost = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    delivery_date = models.DateTimeField(blank=True)

    def __str__(self):
        return "%s buy some products" % (self.user.username)
