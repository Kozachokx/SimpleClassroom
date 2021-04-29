from django.db import models
from django.contrib.auth.models import User
from datetime import datetime  

from django import forms
# from .models import Post

# Create your models here.

# class CustomUser(User):
#     class Meta:
#         abstract = True

class Teacher(User):
    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Student(User):
    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class TestUser(models.Model):
    name = models.CharField(max_length=50, null=True)
    surname = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.name +' '+ self.surname +' email: '+ self.email 

class NewUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_teacher = models.BooleanField(default=False)



# class CustomPost(models.Model):
#     post_type = forms.ChoiceField(widget=forms.RadioSelect(), choices=[(1, 'Lection'), (2, 'Practice'), (3, 'Test')])
#     title = models.CharField(max_length=255)
#     description = models.CharField(max_length=255)


from django.conf import settings
import os

class AssignmentForm(models.Model):
    class Meta:
        abstract = True
    author = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=False)
    title = models.CharField(max_length=255, default='DELETE')
    body = models.TextField(max_length=255, default='', blank=True)
    document = models.FileField(upload_to='upload/', null=True, blank=True, default=None)
    # filename = os.path.join(settings.MEDIA_ROOT, document)
    open_time = models.DateTimeField(default=datetime.now)

    # myfile = os.path.join(settings.MEDIA_ROOT, document)
    @property
    def filename(self):
        return os.path.join(settings.MEDIA_ROOT, self.document.name)

class Lection(AssignmentForm):
    def __str__(self):
        # return self.title + ' | ' + str(self.author)
        return str(self.author) + ' | ' + ('YES' if self.document else 'NO') + ' | ' + self.title
        # return f'{self.aut}'
    
class Practice(AssignmentForm):
    students = models.ManyToManyField(Student)
    def student_names(self):
        return ', '.join([x.last_name for x in self.students.all()])
    student_names.short_description = "Student Names"


