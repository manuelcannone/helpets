from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth.models import User
from django.forms import PasswordInput

class LoginForm(AuthenticationForm):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=PasswordInput())
	
# Create your forms here.
class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ( "email", "password")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
       
		user.email = self.cleaned_data['email']
      
        
		if commit:
			user.save()
		return user