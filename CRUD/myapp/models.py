from django.db import models

# Create your models here.
class Staff(models.Model):
	category = (
			('trainer','trainer'),
			('counsellor','counsellor'),
			('backoffice','backoffice'),
			('admin','admin')
		)
	staff_category=models.CharField(max_length=100,choices=category)
	fname=models.CharField(max_length=100)
	lname=models.CharField(max_length=100)
	email=models.EmailField()
	mobile=models.PositiveIntegerField()

	def __str__(self):
		return self.fname+" - "+self.staff_category

class Task(models.Model):
	staff = models.ForeignKey(Staff,on_delete=models.CASCADE)
	remarks=models.TextField()
	date=models.CharField(max_length=100)
	status=models.CharField(max_length=100)

	def __str__(self):
		return self.staff.fname + " - "+self.remarks