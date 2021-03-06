from django.db import models
from django_enumfield import enum
from django.forms import Form
from django.forms import ModelForm
from django.contrib.auth.models import User
# Create your models here.
# two table 
# relation between two table is like 
# 1) Each user create many requset (1:*)  
# 2) Each user has assigned to one requset (1:1) 
#                ('status', models.CharField(max_length=10, choices=[(b'1', b'approved'), (b'0', b'unapproved')])),

class User(models.Model):
    #user= models.OneToOneField(User)
    #dep=models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.name

 

class Requst(models.Model):
    creator_id = models.ForeignKey(User)
    #owner_id = models.ForeignKey(User)
    title = models.CharField(max_length=30)
    content = models.TextField(max_length=100)
    pub_date = models.DateTimeField('date published')


    status_CHOICES = (
       ('1', 'approved'),
       ('0', 'unapproved'),
    )
    status = models.CharField(max_length=10, choices=status_CHOICES)







