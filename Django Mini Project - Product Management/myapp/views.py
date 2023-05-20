from django.shortcuts import render,redirect
from . models import Admin

# Create your views here.
def index(request):
	product=Admin.objects.all()
	return render(request,'index.html',{'product':product})

def add(request):
	if request.method=="POST":
		Admin.objects.create(
				product_name=request.POST['product_name'],
				product_price=request.POST['product_price'],
				product_model=request.POST['product_model'],
				product_image=request.FILES['product_image'],
				product_ram=request.POST['product_ram']
			)
		product=Admin.objects.all()
		return render(request,'index.html',{'product':product})

def edit(request):
	product=Admin.objects.all()
	return redirect(request,'index.html',{'product':product})

def update(request,id):
	if request.method=="POST":
		product_name=request.POST.get('product_name')
		product_price=request.POST.get('product_price')
		product_model=request.POST.get('product_model')
		product_ram=request.POST.get('product_ram')
		data=Admin(
				id=id, 
				product_name=product_name,
				product_price=product_price,
				product_model=product_model,
				product_ram=product_ram	
			)
		data.save()
		return redirect('index')
	else:
		product=Admin.objects.all()
		return redirect(request,'index.html',{'product':product})

def delete(request,id):
	product=Admin.objects.filter(id=id)
	product.delete()
	context={
		'product':product
	}
	return redirect('index')

def product_manager(request):
		return render(request,'table.html')
