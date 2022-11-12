import imp
from django.db import models
from datetime import datetime

# Create your models here.
# from django.contrib.auth.models import User
from accounts.models import User


class School(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    school_name = models.CharField(max_length=100, null=True, blank=True)
    bus_route = models.CharField(max_length=100, null=True, blank=True)

# class Driver(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
#     name = models.CharField(max_length=255)
#     # name = models.CharField(max_length=255)
#     # email = models.EmailField(null=True)
#     # photo = models.ImageField(upload_to='media/coders/')
#     # description = RichTextField()
#     # city = models.CharField(max_length=255)
#     # level_type = models.CharField(max_length=255, choices=level_choices)
#     # job_type = models.CharField(max_length=255, choices=job_choices)
#     # developer_type = models.CharField(
#     #     max_length=255)
#     # is_featured = models.BooleanField(default=False)
#     # created_date = models.DateTimeField(default=datetime.now, blank=True)
#     # skills = models.CharField(max_length=255, blank=True, null=True)

#     def __str__(self):
# 	    return self.name


# class Driver(models.Model):
# 	driver_username = models.CharField(max_length=255)
# 	driver_name = models.CharField(max_length=100)
# 	driver_email = models.EmailField(null=True)
# 	driver_password = models.CharField(max_length=30)
# 	driver_phone = models.CharField(max_length=16)
# 	bus_route = models.CharField(max_length=30)
# 	bus_plateNo = models.CharField(max_length=10)
# 	school = models.ForeignKey(School, on_delete=models.CASCADE)

# 	def __str__(self):
# 		return self.driver_name

class NavigationLog(models.Model):
	lattitude = models.FloatField()
	longitude = models.FloatField()
	datetime =  models.DateTimeField(default=datetime.now)
	bus = models.ForeignKey(User,on_delete=models.CASCADE)

	def __str__(self):
		return self.datetime
