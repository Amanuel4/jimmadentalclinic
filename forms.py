from django import forms
from .models import Appointment


class MemberForm(forms.ModelForm):
	class Meta:
		model=Appointment
		fields=['name','email','tell','date','dept','dentist','message']

class Subscribe(forms.Form):
	Email=forms.EmailField()

	def __str__(self):
		return self.Email
