from django.db import models
from django.contrib.auth.models import AbstractUser
from decimal import *

class User(AbstractUser):
    status = (
        (1, "Director"), # Abduxoliq
        (2, "Cooker"), # Abduxoliq
        (3, "Waiter"),
        (4, "manager"), # Abduxoliq
        (5, "call center")
    )
    type = models.IntegerField(choices=status, default=1)
    number = models.BigIntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='user', null=True, blank=True)

class Client(models.Model):
    name = models.CharField(max_length=255)
    phone = models.IntegerField(unique=True)

class Room(models.Model):
    number = models.IntegerField()
    is_free = models.BooleanField(default=True)
    people = models.IntegerField()

class Maxsulot(models.Model):
    quantity = models.IntegerField()
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=50, decimal_places=2)
    is_yes = models.BooleanField(default=True)


class Order(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=True)
    delivery = models.BooleanField(default=False)
    owner = models.CharField(max_length=255)
    address = models.CharField(max_length=1000, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    delivery_date = models.DateTimeField(null=True, blank=True)
    done = models.BooleanField(default=False)
    total_price = models.DecimalField(max_digits=50, decimal_places=2, default=0)



class Meal(models.Model):
    is_yes = models.BooleanField(default=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=50, decimal_places=2)



class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    maxsulot = models.ForeignKey(Maxsulot, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, null=True, blank=True)
    meal_quantity = models.IntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        order = Order.objects.get(id=self.order.id)
        print(order.total_price)
        if self.maxsulot is not None and self.meal is not None:
            order.total_price = order.total_price + (Maxsulot.objects.get(id=self.maxsulot.id).price * Decimal(self.quantity))
            order.total_price += Meal.objects.get(id=self.meal.id).price * Decimal(self.meal_quantity)
        elif self.maxsulot is not None and self.meal is None:
            order.total_price = order.total_price + (Maxsulot.objects.get(id=self.maxsulot.id).price * Decimal(self.quantity))
        elif self.maxsulot is None and self.meal is not None:
            order.total_price += Meal.objects.get(id=self.meal.id).price * Decimal(self.meal_quantity)
        else:
            pass
        order.save()
        super(OrderItem, self).save(*args, **kwargs)

class Bot(models.Model):
    text = models.TextField()
    name = models.CharField(max_length=255)


class BotDetail(models.Model):
    text = models.TextField()
    phone = models.CharField(max_length=255)
    lat = models.CharField(max_length=255)
    lng = models.CharField(max_length=255)


