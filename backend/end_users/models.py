from django.db import models

# Create your models here.


class Product(models.Model):
	""""Db model for products"""

	name = models.CharField(max_length=255)
	url = models.CharField(max_length=255)
	price = models.IntegerField()

	def __str__(self):
		return self.name


class Denomination(models.Model):
	""""Db model for Denomination"""

	currency = models.CharField(max_length=255)
	val = models.IntegerField()

	def __str__(self):
		return self.val + self.currency

class Order(models.Model):
	""""Db model for Order"""

	Order_Value = models.IntegerField()
	Date = models.DateField(auto_now=True)


class OrderItem(models.Model):
	""""Db model for OrderItems"""

	Order = models.ForeignKey(Order, on_delete=models.CASCADE)
	Product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
	Quantity = models.IntegerField()
