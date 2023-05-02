from django.shortcuts import render,redirect
from .models import User,Product,Wishlist
import requests
import random

# Create your views here.
def index(request):
	try:
		user=User.objects.get(email=request.session['email'])
		if user.usertype=="buyer":
			products=Product.objects.all()
			return render(request,'index.html',{'products':products})
		else:
			return render(request,'seller-index.html')
	except:
		products=Product.objects.all()
		return render(request,'index.html',{'products':products})

def seller_index(request):
	return render(request,'seller-index.html')

def signup(request):
	if request.method=="POST":
		try:
			User.objects.get(email=request.POST['email'])
			msg="Email Alredy Registered"
			return render(request,'signup.html',{'msg':msg})
		except:
			if request.POST['password'] == request.POST['cpassword']:
				User.objects.create(
						fname=request.POST['fname'],
						lname=request.POST['lname'],
						email=request.POST['email'],
						mobile=request.POST['mobile'],
						address=request.POST['address'],
						city=request.POST['city'],
						zipcode=request.POST['zipcode'],
						password=request.POST['password'],
						profile_pic=request.FILES['profile_pic'],
						usertype=request.POST['usertype'],
					)
				msg="User Sign Up Successfully"
				return render(request,'signin.html',{'msg':msg})
			else:
				msg="Password & Confirm Password Does Not Matched"
				return render(request,'signup.html',{'msg':msg})
	else:
		return render(request,'signup.html')

def signin(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.POST['email'])
			if user.password == request.POST['password']:
				if user.usertype=="buyer":
					request.session['email']=user.email
					request.session['fname']=user.fname
					request.session['profile_pic']=user.profile_pic.url
					return redirect('index')
				else:
					request.session['email']=user.email
					request.session['fname']=user.fname
					request.session['profile_pic']=user.profile_pic.url
					return render(request,'seller-index.html')
			else:
				msg="Invalid Password"
				return render(request,'signup.html',{'msg':msg})
		except:
			msg="Email Not Registered"
			return render(request,'signin.html',{'msg':msg})
	else:
		return render(request,'signin.html')

def signout(request):
	try:
		del request.session['email']
		del request.session['fname']
		return render(request,'signin.html')
	except:
		return render(request,'signin.html')

def change_password(request):
	user=User.objects.get(email=request.session['email'])
	if request.method=="POST":
		if user.password == request.POST['old_password']:
			if request.POST['new_password'] == request.POST['cnew_password']:
				user.password=request.POST['new_password']
				user.save()
				return redirect('signout')
			else:
				msg="New Password & Confirm New Password Does Not Matched"
				if user.usertype=="buyer":
					return render(request,'change-password.html',{'msg':msg})
				else:
					return render(request,'seller-change-password.html',{'msg':msg})		
		else:
			msg="Old Password Does Not Matched"
			if user.usertype=="buyer":
				return render(request,'change-password.html',{'msg':msg})
			else:
				return render(request,'seller-change-password.html',{'msg':msg})		
	else:
		if user.usertype=="buyer":
			return render(request,'change-password.html')
		else:
			return render(request,'seller-change-password.html')

# def seller_change_password(request):
# 	if request.method=="POST":
# 		user=User.objects.get(email=request.session['email'])
# 		if user.password == request.POST['old_password']:
# 			if request.POST['new_password'] == request.POST['cnew_password']:
# 				user.password=request.POST['new_password']
# 				user.save()
# 				return redirect('signout')
# 			else:
# 				msg="New Password & Confirm New Password Does Not Matched"
# 				return render(request,'seller-change-password.html',{'msg':msg})
# 		else:
# 			msg="Old Password Does Not Matched"
# 			return render(request,'seller-change-password.html',{'msg':msg})
# 	else:
# 		return render(request,'seller-change-password.html')

def forgot_password(request):
	if request.method=="POST":
		try:
			user=User.objects.get(mobile=request.POST['mobile'])
			otp=random.randint(1000,9999)
			mobile=user.mobile
			url = "https://www.fast2sms.com/dev/bulkV2"
			querystring = {"authorization":"EgFyhp8qZQXNG7T2RMSb1vIuTW6w3CMa8j1gjSJitlcItKCvGPqzNXxd2HdW","variables_values":str(otp),"route":"otp","numbers":str(mobile)}
			headers = {'cache-control': "no-cache"}
			response = requests.request("GET", url, headers=headers, params=querystring)
			print(response.text)
			msg="OTP Send Successfully"
			return render(request,'otp.html',{'mobile':mobile,'otp':otp,'msg':msg})
		except:
			msg="Mobile Number Not Registered"
			return render(request,'forgot-password.html',{'msg':msg})
	else:
		return render(request,'forgot-password.html')

def verify_otp(request):
	mobile=request.POST['mobile']
	otp=request.POST['otp']
	uotp=request.POST['uotp']

	if otp==uotp:
		return render(request,'new-password.html',{'mobile':mobile})
	else:
		msg="Invalid OTP"
		return render(request,'otp.html',{'mobile':mobile,'otp':otp,'msg':msg})

def new_password(request):
	mobile=request.POST['mobile']
	np=request.POST['new_password']
	cnp=request.POST['cnew_password']

	if np==cnp:
		user=User.objects.get(mobile=mobile)
		user.password=np
		user.save()
		return redirect('signin')
	else:
		msg="New Password & Confirm New Password Does Not Matched"
		return render(request,'new-password.html',{'mobile':mobile,'msg':msg})

def profile(request):
	user=User.objects.get(email=request.session['email'])
	if request.method=="POST":
		user.fname=request.POST['fname']
		user.lname=request.POST['lname']
		user.mobile=request.POST['mobile']
		user.address=request.POST['address']
		user.city=request.POST['city']
		user.zipcode=request.POST['zipcode']
		try:
			user.profile_pic=request.FILES['profile_pic']
		except:
			pass
		user.save()
		msg="Profile Updated Successfully"
		request.session['profile_pic']=user.profile_pic.url
		if user.usertype=="buyer":
			return render(request,'profile.html',{'user':user,'msg':msg})
		else:
			return render(request,'seller-profile.html',{'user':user,'msg':msg})
	else:
		if user.usertype=="buyer":
			return render(request,'profile.html',{'user':user})
		else:
			return render(request,'seller-profile.html',{'user':user})

def seller_add_product(request):
	seller=User.objects.get(email=request.session['email'])
	if request.method=="POST":
		Product.objects.create(
				seller=seller,
				product_category=request.POST['product_category'],
				product_name=request.POST['product_name'],
				product_price=request.POST['product_price'],
				product_desc=request.POST['product_desc'],
				product_image=request.FILES['product_image'],
				product_stock=request.POST['product_stock'],
			)
		msg="Product Added Successfully"
		return render(request,'seller-add-product.html',{'msg':msg})
	else:
		return render(request,'seller-add-product.html')

def seller_view_product(request):
	user=User.objects.get(email=request.session['email'])
	products=Product.objects.filter(seller=user)
	return render(request,'seller-view-product.html',{'products':products})

def seller_product_details(request,pk):
	product=Product.objects.get(pk=pk)
	return render(request,'seller-product-details.html',{'product':product})

def seller_edit_product(request,pk):
	product=Product.objects.get(pk=pk)
	if request.method=="POST":
		product.product_category=request.POST['product_category']
		product.product_name=request.POST['product_name']
		product.product_price=request.POST['product_price']
		product.product_desc=request.POST['product_desc']
		product.product_stock=request.POST['product_stock']
		try:
			product.product_image=request.FILES['product_image']
		except:
			pass
		product.save()
		return redirect('seller-view-product')
	else:
		return render(request,'seller-edit-product.html',{'product':product})

def seller_delete_product(request,pk):
	product=Product.objects.get(pk=pk)
	product.delete()
	return redirect('seller-view-product')

def product_details(request,pk):
	product=Product.objects.get(pk=pk)
	return render(request,'product-details.html',{'product':product})

def add_to_wishlist(request,pk):
	product=Product.objects.get(pk=pk)
	user=User.objects.get(email=request.session['email'])
	Wishlist.objects.create(product=product,user=user)
	return render(request,'index.html')
