from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    stock = models.IntegerField(default=0)
    discount = models.IntegerField()
    stock = models.IntegerField()
    description = models.CharField()


class User(models.Model):
    role = models.CharField()
    user_name = models.CharField()
    password = models.CharField()
    login = models.CharField()

class Order(models.Model):
    order_date = models.DateField()
    delivery_date = models.DateField()
    status = models.CharField()

class orderDetails(models.Model):
    order_id = models.ForeignKey(Order, on_delete = models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete = models.CASCADE)
    order_quantity = models
    