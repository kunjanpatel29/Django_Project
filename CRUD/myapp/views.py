from django.shortcuts import render,redirect
from .models import Staff,Task

# Create your views here.
def index(request):
	staff=Staff.objects.all()
	tasks=Task.objects.all()
	return render(request,'index.html',{'staff':staff,'tasks':tasks})

def add_task(request):
	pk=int(request.POST['staff'])
	staff=Staff.objects.get(pk=pk)
	Task.objects.create(
		staff=staff,
		remarks=request.POST['remarks'],
		date=request.POST['date'],
		status=request.POST['status'],
	)
	msg="Task Created Successfully"
	staff=Staff.objects.all()
	tasks=Task.objects.all()
	return render(request,'index.html',{'staff':staff,'msg':msg,'tasks':tasks})

def complete_task(request):
	id=int(request.POST['id'])
	task=Task.objects.get(pk=id)
	task.status="completed"
	task.save()
	return redirect('index')

def all_task(request):
	return redirect('index')

def pending(request):
	tasks=Task.objects.filter(status="pending")
	staff=Staff.objects.all()
	return render(request,'index.html',{'staff':staff,'tasks':tasks})

def completed(request):
	tasks=Task.objects.filter(status="completed")
	staff=Staff.objects.all()
	return render(request,'index.html',{'staff':staff,'tasks':tasks})
