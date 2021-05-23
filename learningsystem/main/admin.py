from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Register your models here.


# from .models import CustomUser
# admin.site.register(CustomUser)

# from .models import Answer, Lection, Practice, NewUser, Question, Teacher, Student, Test, TestResult
from .models import *
from .forms import UserCreationForm

class CustomUserAdmin(UserAdmin):
    # The forms to add and change user instances
    add_form = UserCreationForm
    list_display = ("username","first_name","last_name","username","email","password")
    ordering = ("email",)

    fieldsets = (
        (None, {'fields': ("username",'email', 'password', 'first_name', 'last_name')}),
        )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','email', 'password', 'first_name', 'last_name')}
            ),
        )





class CustomUserField(admin.ModelAdmin):
    list_display = ('first_name','last_name','username', 'email', 'password')
    fields = ('username','first_name','last_name','password','email')

class CustomLesson(admin.ModelAdmin):
    list_display = ('author','title', 'open_time','include_file','document')
    def include_file(self,obj):
        return 'YES' if obj.document else 'NO'
    # fields = ('username','first_name','last_name','password','email')

class PracticeAdmin(CustomLesson):
    list_display = ('author','title', 'open_time','include_file','document','student_formated_list')
    filter_horizontal = ('students',)






# ---------__________ T _ E _ S _ T __________---------
class TestAdmin(admin.ModelAdmin):
    # list_display = ('author','title')
    pass

class QuestionInline(admin.TabularInline):
    extra = 1
    model = Question

class AnswerInline(admin.TabularInline):
    extra = 1
    model = Answer
    # list_display = ('test.title', 'question.title', 'title')


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

# class QuestionAdmin(admin.ModelAdmin):
#     list_display = ('test_title',"test",'title')
#     def test_title(self,obj):
#         return obj.test.title
    # pass




# class Lection
admin.site.register(Practice, PracticeAdmin)
admin.site.register(Lection, CustomLesson)

admin.site.register(Test, TestAdmin)
# admin.site.register(Question, QuestionAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, TestAdmin)
admin.site.register(PracticeResult)
admin.site.register(TestResult)
# admin.site.register(Lection)

# admin.site.register(Teacher, CustomUserField)
admin.site.register(Student, CustomUserField)

filter_horizontal = ()
admin.site.register(Teacher, CustomUserAdmin)



