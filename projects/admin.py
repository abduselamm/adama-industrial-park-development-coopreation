from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Projects)
admin.site.register(Lease)
admin.site.register(Owner)
admin.site.register(About)
admin.site.register(Request)

