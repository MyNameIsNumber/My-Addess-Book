from django.db import models

class Address(models.Model):
	name = models.CharField(max_length=200)
	email = models.EmailField(max_length=200)
	phone = models.CharField(max_length=15)
	address_first_line = models.CharField(max_length=200)
	address_second_line = models.CharField(max_length=200)
	town = models.CharField(max_length=200)
	postcode = models.CharField(max_length=7)

	def __str__(self):
		return self.name