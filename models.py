from django.db import models

# Create your models here.
class registrationForm(models.Model):
    first_name=models.CharField(max_length=50,default='')
    midle_name=models.CharField(max_length=50,default='')
    last_name=models.CharField(max_length=50,default='')
    date_of_birth=models.CharField(max_length=50,default='')
    home_address=models.CharField(max_length=50,default='')
    physical_address=models.CharField(max_length=50,default='')
    phone_number=models.CharField(max_length=50,default='')
    
     
    
    
    def __str__(self):
        return self.first_name
    
    
class relative1Form(models.Model):
    relation_ship = models.CharField(max_length=40,default='')      
    first_name = models.CharField(max_length=40,default='')
    midle_name=models.CharField(max_length=50,default='')
    last_name=models.CharField(max_length=50,default='')
    home_address=models.CharField(max_length=50,default='')
    physical_address=models.CharField(max_length=50,default='')
    phone_number=models.CharField(max_length=50,default='')
    
    
    
    def __str__(self):
        return self.first_name
    
    
class relative2Form(models.Model): 
    relation_ship = models.CharField(max_length=40,default='')     
    first_name = models.CharField(max_length=40,default='')
    midle_name=models.CharField(max_length=50,default='')
    last_name=models.CharField(max_length=50,default='')
    home_address=models.CharField(max_length=50,default='')
    physical_address=models.CharField(max_length=50,default='')
    phone_number=models.CharField(max_length=50,default='')
    
    
    
    def __str__(self):
        return self.first_name 
    
    
class relative3Form(models.Model):
    relation_ship = models.CharField(max_length=40,default='')   
    first_name = models.CharField(max_length=40,default='')
    midle_name=models.CharField(max_length=50,default='')
    last_name=models.CharField(max_length=50,default='')
    home_address=models.CharField(max_length=50,default='')
    physical_address=models.CharField(max_length=50,default='')
    phone_number=models.CharField(max_length=50,default='')
    
    
    
    def __str__(self):
        return self.first_name       
    
    
class educationForm(models.Model):   
    Form_FOUR_certification = models.FileField(default='')
    Birth_Certification=models.FileField(default='')
    Parent_or_Guardian_NationalID_card = models.FileField(default='')
    
    
    def __str__(self):
        return f'{self.Form_FOUR_certification}'
    
    
    

class UserForm(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    