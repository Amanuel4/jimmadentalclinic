from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import Customer, Dentist, CaseandPricing, Classroom,Appointment
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import MemberForm
from . import forms
from dentalclinic.settings import EMAIL_HOST_USER

# Create your views here.
def homepage(request):
	dental=Dentist.objects.all

	return render(request,'main/home.html',{'dental':dental})


def doctors(request):

	dental=Dentist.objects.all
	return render(request,'main/doctors.html',{'dental':dental})


def service(request):

	return render(request,'main/service.html',{})

def about(request):

	return render(request,'main/about.html',{})

def contactview(request):

	return render(request,'main/contactview.html',{})


def register(request):
	if request.method=='POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request,f"New Account Created: {username}")
			return redirect("main:homepage")
	else:
		form= UserCreationForm
		for msg in form.error_messages:
			messages.error(request,f"{msg}: {form.error_messages}")
		#form= UserCreationForm
	return render(request,"main/register.html",{"form":form})

def appointment(request):
	if request.method == "POST":
		 

		if request.POST.get('name') and request.POST.get('email') and request.POST.get('phone') and request.POST.get('date') and request.POST.get('department') and request.POST.get('doctor') and request.POST.get('message'):
			app = Appointment()
			app.name = request.POST.get('name')
			app.email = request.POST.get('email')
			app.tell = request.POST.get('phone')
			app.date = request.POST.get('date')
			app.dept = request.POST.get('department')
			app.dentist = request.POST.get('doctor')
			app.message = request.POST.get('message')
			app.save()
		return redirect("main:homepage")

	else:
		return redirect("main:homepage")

def appointmentlist(request):
	app=Appointment.objects.all

	return render(request,"main/appointmentlist.html",{"app":app})




	'''if request.method == "POST":
		form=MemberForm(request.POST or None)
		name1=request.POST['name']
		email1=request.POST['email']
		tel=request.POST['phone']
		time =request.POST['date']
		dept =request.POST['department']
		doctor =request.POST['doctor']
		message =request.POST['message']
		if form.is_valid():
			form.save()
	return render(request,'main/appointment.html', {
				"name1": name1 ,
				'email1': email1,
				'tel': tel,
				'time': time,
				'dept': dept,
				'doctor': doctor,
				'message': message
				   })'''




def contact(request):
	if request.method=="POST":
		name1=request.POST['name']
		email=request.POST['email']
		subject=request.POST['subject']
		message=request.POST['message']

		'''send_mail(
				 subject,
				 message, 
				 email,
				 ['amanessa4@gmail.com']		  

				 )'''

		return render(request,'main/contact.html',{
				"name1": name1 ,
				'email': email,
				'subject': subject,
				'message': message 

			})




	return render(request,'main/contact.html',{})




def logout_request(request):
	logout(request)
	messages.info(request,"Logged out successfully!")
	return redirect("main:homepage")

def login_request(request):
	if request.method=='POST':	
		form = AuthenticationForm(request,data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username,password=password)
			if user is not None:
				login(request,user)
				messages.info(request,f"You are now logged in as {username}")
				return redirect("main:homepage")
			else:
				messages.error(request,"Invalid username or Password")
		else:
			messages.error(request,"Invalid username or Password")

	form = AuthenticationForm()
	return render(request,'main/login.html',{'form':form}) 




 
def join(request):
	if request.method=='POST':
		form=Memberform(request.POST or None)
		if form.is_valid():
			form.save()
		return render(request,'main/appointment.html',{})
	else:
		return render(request,'main/appointment.html',{}) 
	


def subscribe(request):
	sub= forms.Subscribe()
	if request.method == 'POST':
		sub = forms.Subscribe(request.POST)
		subject = 'Welcome to Jimma Dental Clinic'
		message = 'Hope you are enjoying our services'
		recepient = str(sub['Email'].value())
		send_mail(subject,message,EMAIL_HOST_USER,[recepient],fail_silently=False)
		return render(request,'main/success.html',{'recepient':recepient})

	return render(request,'main/home.html',{'form':sub})


