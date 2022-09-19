import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class ProjectsFilter(django_filters.FilterSet):
	class Meta:
		model = Projects
		fields = '__all__'
		exclude = ['date_created','purpose','cluster','Investment_Capital','Job_Creation','Mayor_Approval_of_land','Recieved_Land_Meter_square','Industry_Village','UPIN_Number','Block_Number','Parcel_Number']