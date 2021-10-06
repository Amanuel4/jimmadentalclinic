from django.db import models

# Create your models here.
class Customer(models.Model):
	cust_f_name=models.CharField(max_length=50)
	cust_l_name=models.CharField(max_length=50)
	cust_addr=models.CharField(max_length=120)
	cust_job=models.CharField(max_length=80)
	cust_dob=models.DateTimeField()
	cust_case=models.TextField()
	#cust_pass=models.PasswordField()
	cust_username=models.CharField(max_length=100)

	booking_date=models.DateTimeField()


	def __str__(self):
		return self.cust_f_name



class Dentist(models.Model):
	dentf_f_name=models.CharField(max_length=100,default="name")
	dent_l_name=models.CharField(max_length=100)
	dent_username=models.CharField(max_length=100)
	dent_password=models.CharField(max_length=100)
	dent_addres=models.CharField(max_length=100)




	def __str__(self):
		return self.dentf_f_name


class Classroom(models.Model):
	classroom_name=models.CharField(max_length=30)

	def __str__(self):
		return self.classroom_name

class CaseandPricing(models.Model):
	case_name=models.CharField(max_length=255)
	price=models.CharField(max_length=5)

	def __str__(self):
		return self.case_name+' '+ self.price

#class Pricing(models.Model):
#	case_name=models.ForeignKey(Case,on_delete=models.CASCADE)
#	price=models.CharField(max_length=5)
 
#	def __str__(self):
#		return self.P

class Appointment(models.Model):
	name=models.CharField(max_length=100)
	email=models.EmailField()
	tell=models.CharField(max_length=255)
	date=models.DateTimeField()
	dept=models.CharField(max_length=50)
	dentist=models.CharField(max_length=100)
	message=models.CharField(max_length=255)
	

	def __str__(self):
		return self.name


