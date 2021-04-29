from django.contrib import admin

# Register your models here.


# from .models import CustomUser
# admin.site.register(CustomUser)

from .models import Lection, Practice, NewUser, Teacher, Student



class CustomUserField(admin.ModelAdmin):
    list_display = ('first_name','last_name','username', 'email')
    fields = ('username','first_name','last_name','password','email')

class CustomLesson(admin.ModelAdmin):
    list_display = ('author','title', 'open_time','include_file','document')
    def include_file(self,obj):
        return 'YES' if obj.document else 'NO'
    # fields = ('username','first_name','last_name','password','email')

class PracticeAdmin(CustomLesson):
    list_display = ('author','title', 'open_time','include_file','document', 'student_names')
    filter_horizontal = ('students',)

# class Lection
admin.site.register(Practice, PracticeAdmin)
admin.site.register(Lection, CustomLesson)
# admin.site.register(Lection)

admin.site.register(Teacher, CustomUserField)
admin.site.register(Student, CustomUserField)




