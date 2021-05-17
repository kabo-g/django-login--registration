from django.db import models

# Create your models here.

class People(models.Model):
	GENDER_CHOICES = (("MALE", "MALE"),
		("FEMALE", "FEMALE"),)

	name = models.CharField(max_length = 50, blank = True)
	surname = models.CharField(max_length = 50, blank = True)
	age = models.IntegerField()
	gender = models.CharField(max_length = 50, choices = GENDER_CHOICES, default = "MALE")


	def __str__(self):
		return self.name +" "+ self.surname