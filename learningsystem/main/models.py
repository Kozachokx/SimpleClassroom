from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, time
from django.http import request  
import pytz
utc=pytz.UTC
from django.urls import reverse


from django import forms
from django.db.models.deletion import CASCADE
# from .models import Post

# Create your models here.

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
    def abv(self):
        return f'{self.first_name[0]}.{self.last_name}'

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

    def is_open(self):
        # print(f"datetime.now = {datetime.now()} | open_time = {self.open_time}")
        # print(f"datetime.now = {utc.localize(datetime.now())} | ")
        # print(f"datetime.now >= open_time  {utc.localize(datetime.now()) >= self.open_time}")
        return utc.localize(datetime.now()) >= self.open_time

    def get_absolute_url(self):
        return reverse("classroom", kwargs={"pk": self.pk})
    

    # myfile = os.path.join(settings.MEDIA_ROOT, document)
    @property
    def filename(self):
        return os.path.join(settings.MEDIA_ROOT, self.document.name)

    @property
    def fileurl(self):
        return os.path.join(settings.MEDIA_URL, self.document.name)

class Lection(AssignmentForm):
    def __str__(self):
        # return self.title + ' | ' + str(self.author)
        return str(self.author) + ' | ' + ('YES' if self.document else 'NO') + ' | ' + self.title
        # return f'{self.aut}'
    
class Practice(AssignmentForm):
    students = models.ManyToManyField(Student)

    def __str__(self):
        # return self.title + ' | ' + str(self.author)
        return self.title  + ' | by ' + str(self.author)

    def st_list(self):
        return [].append( Student.objects.get(pk=x.id).id for x in self.students.all() )

    def student_ids(self):
        return [Student.objects.get(pk=x.id).id for x in self.students.all()]

    def st_ids(self):
        res = [Student.objects.get(pk=x.id).id for x in self.students.all()]
        print (f"                            {res}        <<<<<<<<<<<<--------------")
        return str([Student.objects.get(pk=x.id).id for x in self.students.all()])

    def student_exists_in(self):
        return ', '.join([str(Student.objects.get(pk=x.id).id) for x in self.students.all()])
        # return [].push([x.id for x in self.students.all()])
        # return [].push([x.id for x in self.students.all()])

    def student_formated_list(self):
        return ', '.join([x.first_name[0] + "." + x.last_name for x in self.students.all()])
    student_formated_list.short_description = "Student List"

    def get_practise_results(self):
        return self.practiceresults.all()

    def passed_student_ids(self):
        passed_students_id_list = []
        passed_works = PracticeResult.objects.filter( practice__id = self.pk )
        for i in passed_works:
            passed_students_id_list.append(Student.objects.get(pk=i.student.id).id)
        return passed_students_id_list

    def get_all_practise_results(self):
        passed_works = PracticeResult.objects.filter( practice__id = self.pk )
        passed_students = []
        temp = []
        for i in passed_works:
            passed_students.append(Student.objects.get(pk=i.student.id))
            s = Student.objects.get(pk=i.student.id)
            # his_work = 
            t1 = f"[PASSED] {s.first_name} {s.last_name} "
            temp.append(t1)
        
        print(f" models.py Practice ________________________________   {passed_students}")
        need_to = [Student.objects.get(pk=x.id) for x in self.students.all()]
        for i in need_to:
            if( i not in passed_students ):
                temp.append(f"[didn't] {i.first_name} {i.last_name}")

        
        return temp

class PracticeResult(models.Model):
    practice = models.ForeignKey(Practice, on_delete=models.CASCADE, null=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='practiceresults')
    document = models.FileField(upload_to='upload/sfiles/', null=True, blank=True, default=None)
    # filename = os.path.join(settings.MEDIA_ROOT, document)
    passed_time = models.DateTimeField(default=datetime.now)


    def passed_student_ids(self):
        return [Student.objects.get(pk=x.id).id for x in self.students.all()]

    def include_file(self):
        print(f'   - - - - - - --       {self.document.name}  <<<<--------')
        return self.document

    # myfile = os.path.join(settings.MEDIA_ROOT, document)
    @property
    def filename(self):
        return os.path.join(settings.MEDIA_ROOT, self.document.name)

    @property
    def fileurl(self):
        return os.path.join(settings.MEDIA_URL, self.document.name)

    def doc_sended(self):
        return self.document
    

QUESTION_TYPES = [
    ('default','default'),
    ('extended','extended'),
    ('input','input'),
]

class Test(models.Model):
    class Meta:
        verbose_name = '[Test] Test'
        verbose_name_plural = '[Test] Tests'

    author = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=False)
    title = models.CharField(max_length=255, default='Test №')

    count_of_question_type_1 = models.PositiveSmallIntegerField(default=0, help_text="Default type: 4 Answers")
    sroce_value_per_type_1 = models.PositiveSmallIntegerField(default=1, help_text="Value per 1 RIGHT answer")
    count_of_question_type_2 = models.PositiveSmallIntegerField(default=0, help_text="Extended type: N Answers (where n < k answers)")
    sroce_value_per_type_2 = models.PositiveSmallIntegerField(default=1, help_text="Value per 1 RIGHT answer")
    count_of_question_type_3 = models.PositiveSmallIntegerField(default=0, help_text="Input type: input your answer")
    sroce_value_per_type_3 = models.PositiveSmallIntegerField(default=1, help_text="Value per 1 RIGHT answer")

    time = models.PositiveSmallIntegerField(help_text="Time duration for the Quiz in minutes")
    open_time = models.DateTimeField(default=datetime.now)

    def is_open(self):
        return utc.localize(datetime.now()) >= self.open_time

    def get_questions(self):
        return self.questions.all()

    def get_current_count(self):
        t = self.questions.all().count()
        t1 = self.questions.all().filter(type = 'default').count()
        t2 = self.questions.all().filter(type = 'extended').count()
        t3 = self.questions.all().filter(type = 'input').count()
        return f"_ _ [ {t} ] question(s)| default({t1}) extended:({t2}) input: ({t3}) "
    
    def __str__(self):        
        return f"ID[ {self.pk} ] -|- {str(self.title)}  |  by {self.author.first_name[0]}.{self.author.last_name} | {self.get_current_count()}"
        # return f"{self.__class__.__name__}[{self.pk}] -|- {str(self.title)}  |  by {self.author.first_name[0]}.{self.author.last_name} | {self.get_current_count()}"

    
    
    

class Question(models.Model):
    class Meta:
        verbose_name = '[Test] Question'
        verbose_name_plural = '[Test] Questions'

    title = models.CharField(max_length=255)
    test = models.ForeignKey(Test, on_delete=models.CASCADE,related_name='questions')
    # created = models.DateTimeField(auto_now_add=True)
    type = models.CharField(
        max_length=10,
        choices=QUESTION_TYPES,
        default=QUESTION_TYPES[0]
    )

    def __str__(self):
        return f"{str(self.test.title)}  |  {self.title} _  _ [ {self.type} ]"
    
    def get_answers(self):
        return self.answers.all()
        # pass
    

class Answer(models.Model):
    class Meta:
        verbose_name = '[Test] Answer'
        verbose_name_plural = '[Test] Answers'

    title = models.CharField(max_length=255)
    is_true = models.BooleanField(default=False)
    questtion = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')

    def __str__(self):
        return f"{self.questtion.test.title} | [Q]: {self.questtion.title} --|-- [A]: {self.title} | [Correct]: {self.is_true}"

class TestResult(models.Model):
    class Meta:
        verbose_name = '[Test] Result'
        verbose_name_plural = '[Test] Results'
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    result = models.PositiveSmallIntegerField()

    def __str__(self):
        return str(self.pk)
        # return self.test.title + self.score


    

