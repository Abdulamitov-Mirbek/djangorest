from django.db import models


class Student(models.Model):
	name = models.CharField(max_length=100)
	age = models.PositiveIntegerField()
	course = models.CharField(max_length=100, default='Python')
	is_active = models.BooleanField(default=True)

	def __str__(self):
		return self.name
