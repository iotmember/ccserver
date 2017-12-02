from django.db import models

# Create your models here.

class Website(models.Model):
	"""
	Informations about a website
	"""

	domain = models.CharField(max_length=100, help_text="Domain")

	address = models.CharField(max_length=50, help_text="IP Address")

	content = models.CharField(max_length=200, help_text="Description about website")

	def __str__(self):
		return (self.domain + " : " + self.address)
