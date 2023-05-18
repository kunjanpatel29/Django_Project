from django.db import models

# Create your models here.
class Admin(models.Model):

	product_id=models.BigAutoField(primary_key=True)
	product_name=models.CharField(max_length=100)

	class Meta:
		db_table='Product_mst'

	def __str__(self):
		return self.product_name

class Product_Subcategory(models.Model):
	
	product=models.ForeignKey(Admin,on_delete=models.CASCADE)
	product_price=models.PositiveIntegerField()
	product_image=models.ImageField(upload_to='profile_pic/')
	product_model=models.CharField(max_length=100)
	product_ram=models.CharField(max_length=100)

	class Meta:
		db_table="Product_sub_cat"