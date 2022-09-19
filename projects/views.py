from django.shortcuts import render,redirect
from django.http import HttpResponse 
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *
from .filters import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required


# Create your views here.
from .decorators import *

def home(request):
    return render(request,'projects/home.html')


def about(request):
    about = About.objects.all()
    return render(request,'projects/aboutus.html',{'about':about})

def faq(request):
    return render(request,'projects/faq.html')

@unauthenticated_user
def registerPage(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')

			group = Group.objects.get(name='owner')
			user.groups.add(group)
			Owner.objects.create(
				user=user,
				name=user.username
			)
			messages.success(request, 'Account was created for ' + username)

			return redirect('login')
		

	context = {'form':form}
	return render(request, 'projects/register.html', context)
@unauthenticated_user
def loginPage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('dashboard')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'projects/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('home')

@login_required(login_url='login')
@admin_only
def dashboard(request):
	project = Projects.objects.all()
	lease = Lease.objects.all()
	total_projects = project.count()
	context = {'total_projects':total_projects,'project':project,'lease':lease}
	return render(request,'projects/dashboard.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['owner'])
def userPage(request):
	owner = Owner.objects.all()
	lease = Lease.objects.all()
	owners = request.user.owner.projects_set.all()
	context = {'owner':owner,'owners':owners,'lease':lease}
	return render(request, 'projects/user.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def projects(request):
    project = Projects.objects.all()
    context = {'project':project}
    return render(request,'projects/projects.html', context)
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','owner'])
def owner(request, pk_test):
	owner = Owner.objects.get(id=pk_test)
	projects = owner.projects_set.all()
	project_count = projects.count()
    
	myFilter = ProjectsFilter(request.GET, queryset=projects)
	project = myFilter.qs
	context = {'owner':owner,'projects':projects,'project_count':project_count,'myFilter':myFilter,'project':project}
	return render(request,'projects/owner.html', context)
@login_required(login_url='login')
@allowed_users(allowed_roles=['owner','admin'])
def accountSettings(request):
	owner = request.user.owner
	form = OwnerForm(instance=owner)
	if request.method == 'POST':
		form = OwnerForm(request.POST, request.FILES,instance=owner)
		if form.is_valid():
			form.save()
	context = {'form':form}
	return render(request,'projects/account_settings.html', context)
def lease(request):
	lease = Lease.objects.all()
	
	context = {'lease':lease}
	return render(request,'projects/lease.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createProject(request):
    form = ProjectsForm()
    if request.method == 'POST':
        form = ProjectsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dashboard')

    context = {'form':form}
    return render(request,'projects/create_project.html',context)
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateProject(request, pk):
    project = Projects.objects.get(id=pk)
    form = ProjectsForm(instance=project)
    context = {'form':form}
    if request.method == 'POST':
        form = ProjectsForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('/dashboard')
    return render(request,'projects/update_project.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteProject(request, pk):
	project = Projects.objects.get(id=pk)
	if request.method == "POST":
		project.delete()
		return redirect('/dashboard')

	context = {'item':project}
	return render(request, 'projects/deleteproject.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createLease(request):
    form = LeaseForm()
    if request.method == 'POST':
        form = LeaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dashboard')

    context = {'form':form}
    return render(request,'projects/lease_form.html',context)
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateLease(request, pk):
    lease = Lease.objects.get(id=pk)
    form = LeaseForm(instance=lease)
    context = {'form':form}
    if request.method == 'POST':
        form = LeaseForm(request.POST, instance=lease)
        if form.is_valid():
            form.save()
            return redirect('/dashboard')
    return render(request,'projects/update_lease.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteLease(request, pk):
	lease = Lease.objects.get(id=pk)
	if request.method == "POST":
		lease.delete()
		return redirect('/dashboard')

	context = {'item':lease}
	return render(request, 'projects/deletelease.html', context)