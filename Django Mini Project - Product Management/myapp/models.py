from django.db import models

# Create your models here.
class Admin(models.Model):

	product_name=models.CharField(max_length=100)
	product_price=models.PositiveIntegerField()
	product_image=models.ImageField(upload_to='product_image/')
	product_model=models.CharField(max_length=100)
	product_ram=models.CharField(max_length=100)

	class Meta:
		db_table="product_mst"

	def __str__(self):
		return self.product_name
