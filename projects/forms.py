from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class ProjectsForm(ModelForm):
	class Meta:
		model = Projects
		fields = '__all__'
class LeaseForm(ModelForm):
	class Meta:
		model = Lease
		fields = '__all__'
class OwnerForm(ModelForm):
	class Meta:
		model = Owner
		fields = '__all__'
		exclude = ['user']


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
