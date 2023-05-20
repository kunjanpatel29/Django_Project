from django.shortcuts import render,redirect
from . models import Admin

# Create your views here.
def index(request):
	product=Admin.objects.all()
	return render(request,'index.html',{'product':product})

def add(request):
	if request.method=="POST":
		Admin.objects.create(
				product_name=request.POST['name'],
				product_price=request.POST['price'],
				product_model=request.POST['model'],
				product_image=request.FILES['image'],
				product_ram=request.POST['ram']
			)
		product=Admin.objects.all()
		return render(request,'index.html',{'product':product})


