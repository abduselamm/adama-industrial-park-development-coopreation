from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Owner(models.Model):
    user = models.OneToOneField(User, null=True,blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(default="profile1.png", null=True, blank=True)

    
    def __str__(self):
        return self.name


class Lease(models.Model):
    STATUS = (
            ('HAVE', 'HAVE'),
            ('HAVE NO', 'HAVE NO'),
            )
    lease = models.OneToOneField(User, null=True,blank=True, on_delete=models.CASCADE)
    Title_deeded_no = models.CharField(max_length=200, null=True)
    Date_of_deliver = models.DateTimeField(null=True)
    Site_plan = models.CharField(max_length=200, null=True,choices = STATUS)
    Plan_agreement_date = models.DateTimeField(null=True)
    permission_of_building_date = models.DateTimeField(null=True) 
    Starting_of_Building = models.DateTimeField(null=True)
    finishing_of_building = models.DateTimeField(null=True)
    Nationality = models.CharField(max_length=200, null=True)
    Email = models.CharField(max_length=200, null=True)
    Phone_Number = models.CharField(max_length=200, null=True)
    EIA = models.CharField(max_length=200, null=True,choices = STATUS)
    Lease_agreement_and_other_documents = models.FileField(null=True,blank=True)
    
    def __str__(self):
        return self.Email


class Projects(models.Model):
    owner = models.ForeignKey(Owner, null=True, on_delete= models.SET_NULL)
    lease = models.ForeignKey(Lease, null=True, on_delete= models.SET_NULL)
    Project_name = models.CharField(max_length=200, null=True)
    purpose = models.CharField(max_length=200, null=True)
    cluster = models.CharField(max_length=200, null=True)
    Investment_Capital = models.CharField(max_length=200, null=True)
    Job_Creation = models.CharField(max_length=200, null=True)
    Mayor_Approval_of_land = models.CharField(max_length=200, null=True)
    Recieved_Land_Meter_square = models.CharField(max_length=200, null=True)
    Industry_Village = models.CharField(max_length=200, null=True)
    UPIN_Number = models.CharField(max_length=200, null=True)
    Block_Number = models.CharField(max_length=200, null=True)
    Parcel_Number = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.Project_name

  
class About(models.Model):
    about = models.TextField(null=True, blank=True)
    