from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    supplier_id = models.ForeignKey(Supplier, on_delete = models.CASCADE)
    manufacturer_id = models.ForeignKey(Manufacturer, on_delete = models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete = models.CASCADE)
    discount = models.IntegerField()
    stock = models.IntegerField(default=0)
    description = models.CharField()


class User(models.Model):
    user_name = models.CharField()
    password = models.CharField()
    login = models.CharField()

class Order(models.Model):
    order_date = models.DateField()
    delivery_date = models.DateField()
    status = models.CharField()
    delivery_address = models.ForeignKey(deliveryPoint, on_delete = models.CASCADE)
    receiver_name = models.CharField()
    delivery_code = IntegerField()
    status = models.CharField()
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)


class OrderDetails(models.Model):
    order_id = models.ForeignKey(Order, on_delete = models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete = models.CASCADE)
    order_quantity = models.IntegerField(default=1)

class Supplier(models.Model):
    name = models.CharField()

class Manufacturer(models.Model):
    name = models.CharField()

class Category(models.Model):
    name = models.CharField()

class UserToGroup(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    group_id = models.ForeignKey(group)

class Group(models.Model):
    role = models.CharField()