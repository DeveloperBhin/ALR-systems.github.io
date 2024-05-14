from django import forms
from .models import *

class userCreationForm(forms.ModelForm):
    class Meta:
        model = registrationForm
        fields = ['first_name','midle_name','last_name','date_of_birth','home_address' ,'physical_address', 'phone_number']
        
        
        
class relative1createForm(forms.ModelForm):
    class Meta:
        model = relative1Form
        fields =  ['relation_ship','first_name','midle_name','last_name','home_address' ,'physical_address', 'phone_number']  
        
        
class relative2createForm(forms.ModelForm):
    class Meta:
        model = relative2Form
        fields =  ['relation_ship','first_name','midle_name','last_name','home_address' ,'physical_address', 'phone_number']  
        
          
class relative3createForm(forms.ModelForm):
    class Meta:
        model = relative3Form
        fields =  ['relation_ship','first_name','midle_name','last_name','home_address' ,'physical_address', 'phone_number']                      
        
        
        
class educationCreateForm(forms.ModelForm):
     class Meta:
        model = educationForm
        fields = ['Form_FOUR_certification','Birth_Certification','Parent_or_Guardian_NationalID_card']  

class RegisterForm(forms.ModelForm):
    class Meta:
        model = UserForm
        fields = ['username', 'email', 'password']
        
         
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
          