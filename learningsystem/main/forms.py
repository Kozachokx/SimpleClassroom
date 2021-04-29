from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Student, Lection
    
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class CreateStudent(ModelForm):
    class Meta:
        model = Student
        fields = ['username', 'first_name', 'last_name', 'email', 'password']


class CreateCustomForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']



from datetime import datetime  
class CreateNewLection(ModelForm):
    class Meta:
        model = Lection
        fields = ('title', 'body', 'document', 'open_time')
        # widgets = {
        #     'open_time' : forms.DateTimeField(default=datetime.now)
        # }

    # def include_file(self,obj):
    #     return 'YES' if obj.document else 'NO'
