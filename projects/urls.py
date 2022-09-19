from django.urls import path
from . import views


urlpatterns=[
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
    path('user/', views.userPage, name="user-page"),
    path('', views.home,name="home"),
    path('account/', views.accountSettings, name="account"),
    path('dashboard/', views.dashboard,name="dashboard"),
    path('projects/', views.projects,name="projects"),
    path('owner/<str:pk_test>/', views.owner,name="owner"),
    path('lease/', views.lease,name='lease'),
    path('about/', views.about,name="about"),
    path('faq/', views.faq,name="faq"),
    path('createproject/', views.createProject,name="createproject"),
    path('updateproject/<str:pk>/', views.updateProject,name="updateproject"),
    path('deleteproject/<str:pk>/', views.deleteProject,name="deleteproject"),
    path('createlease/', views.createLease,name="createlease"),
    path('updatelease/<str:pk>/', views.updateLease,name="updatelease"),
    path('deletelease/<str:pk>/', views.deleteLease,name="deletelease")
]   