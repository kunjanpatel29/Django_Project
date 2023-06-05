from django.shortcuts import render,redirect
from .models import User,Contact

# Create your views here.
def index(request):
	return render(request,'index.html')

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
				return render(request,'index.html')
			else:
				msg="Invalid Password"
				return render(request,'signin.html',{'msg':msg})
		except:
			msg="Email Not Registered"
			return render(request,'signup.html',{'msg':msg})
	else:
		return render(request,'signin.html')

def signout(request):
	try:
		del request.session['email']
		del request.session['fname']
		return render(request,'signin.html')
	except:
		return render(request,'signin.html')

def about(request):
	return render(request,'about.html')

def doctors(request):
	return render(request,'doctors.html')

def contact(request):
	if request.method=="POST":
		Contact.objects.create(
				name=request.POST['name'],
				email=request.POST['email'],
				mobile=request.POST['mobile'],
				remarks=request.POST['remarks'],
			)
		# contacts=Contact.objects.all().order_by("-id")[:5]
		msg="Contact Saved Successfully"
		return render(request,'contact.html',{'msg':msg})
	else:
		# contacts=Contact.objects.all().order_by("-id")[:5]
		return render(request,'contact.html')

def change_password(request):
	if request.method=="POST":
		user=User.objects.get(email=request.session['email'])
		if user.password==request.POST['old_password']:
			if request.POST['new_password'] == request.POST['cnew_password']:
				user.password = request.POST['new_password']
				user.save()
				return redirect('signout')
			else:
				msg="New Password & Confirm New Password Does Not Matched"
				return render(request,'change-password.html',{'msg':msg})
		else:
			msg="Old Password Does Not Matched"
			return render(request,'change-password.html',{'msg':msg})
	else: 
		return render(request,'change-password.html')

def forgot_password(request):
	if request.method == "POST":
		try:
			user=User.objects.get(email=request.POST['email'])
			otp=random.randint(1000,9999)
			subject = 'OTP for Forgot Password'
			message = 'Hello '+user.fname+", Your OTP For Forgot Password Is "+str(otp)
			email_from = settings.EMAIL_HOST_USER
			recipient_list = [user.email, ]
			send_mail( subject, message, email_from, recipient_list )
			return render(request,'otp.html',{'email':user.email,'otp':otp})
		except:
			msg="Email Not Registered"
			return render(request,'forgot-password.html',{'msg':msg}) 			
	else:
		return render(request,'forgot-password.html')

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
		request.session['profile_pic'] = user.profile_pic.url 
		return render(request,'profile.html',{'user':user,'msg':msg})
	else:
		return render(request,'profile.html',{'user':user})
