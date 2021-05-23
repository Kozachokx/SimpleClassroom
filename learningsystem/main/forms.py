from django.forms import ModelForm, widgets
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Practice, Student, Lection, Teacher, Test
# from learningsystem.main import models
    
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class CreateStudent(ModelForm):
    class Meta:
        model = Student
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

class LoginStudent(ModelForm):
    class Meta:
        model = Student
        fields = ['username', 'password']


class CreateCustomForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)



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


class CreateNewPractice(ModelForm):
    class Meta:
        model = Practice
        fields = ('title', 'body', 'document', 'open_time','students')
        
    students = forms.ModelMultipleChoiceField(
        queryset=Student.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
        # widgets = {
        #     'open_time' : forms.DateTimeField(default=datetime.now)
        # }

    # def include_file(self,obj):
    #     return 'YES' if obj.document else 'NO'


class CreateNewTest(ModelForm):
    class Meta:
        model = Test
        fields = '__all__'
        exclude = ('author',)
        


class UserCreationForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ("username",'first_name','last_name')

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        print("________--------------__________")
        print(user)
        print("________--------------__________")
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user