from django.shortcuts import render,redirect
from .models import User
import requests
import random

# Create your views here.
def index(request):
	try:
		user=User.objects.get(email=request.session['email'])
		if user.usertype=="buyer":
			return render(request,'index.html')
		else:
			return render(request,'seller-index.html')
	except:
		return render(request,'index.html')

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
				request.session['email']=user.email
				request.session['fname']=user.fname
				request.session['profile_pic']=user.profile_pic.url
				request.session['usertype']=user.usertype

				if user.usertype=="seller":
					return render(request,'seller-index.html')
				else:
					return render(request,'index.html')
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