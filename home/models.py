
from django.db import models

class User_Details(models.Model):
     username=models.CharField(max_length=30)
     password=models.CharField(max_length=20)
     mobile=models.IntegerField()

class EventDetails(models.Model):
    eventtitle=models.CharField(max_length=20)
    Date=models.DateField()
    Time=models.CharField(max_length=20)
    max_no_participants=models.IntegerField()
    Description=models.CharField(max_length=20)
    eventbanner=models.ImageField(upload_to='pics')
