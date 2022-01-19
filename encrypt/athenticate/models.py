import email
from pickle import TRUE
from django.db import models
from django.forms import CharField, EmailField

# Create your models here.
class RegistrationModel(models.Model):
    username = models.CharField(max_length=100,blank=False)
    f_name= models.CharField(max_length=100,blank=True)
    l_name= models.CharField(max_length=100,blank=True)
    email=models.EmailField(max_length=100, unique=True, blank=False)
    password=models.CharField(max_length=20,blank=False)

    def __str__(self):
        return self.username

    def fullname(self):
        return f'{self.f_name} {self.l_name}'
    
    def shortname(self):
        return self.f_name

    def normalizeEmail(self):
        return self.email.lower()
    
    

