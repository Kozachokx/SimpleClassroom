from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, ListView, DetailView, DeleteView

from .forms import CreateUserForm, CreateStudent, CreateNewLection
from .models import Lection, Practice, Teacher

def registerPage(request):
    # form = UserCreationForm()
    form = CreateStudent()
    if request.method == 'POST':
        form = CreateStudent(request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'main/register.html', context)

def loginPage(request):
    context = {}
    return render(request, 'main/login.html', context)

def index(request):
    return render(request, 'main/index.html')


def teacherPage(request):
    context = {'lection_list':Lection}
    return render(request, 'main/teacherPage.html', context)


# from .models import Lection, Teacher

class TeacherList(ListView):
    model = Teacher
    template_name = 'main/student_main.html'

class ViewTeacherClass(ListView):
    model = Teacher
    template_name = 'main/teacherPage.html'

    def get(self, request, *args, **kwargs):
        teacher_id = self.kwargs['pk']
        lections = Lection.objects.filter( author__id = teacher_id )
        practices = Practice.objects.filter( author__id = teacher_id )
        context = {'lections': lections, 'practices': practices}
        return render(request, self.template_name, context=context)



# Lections---------------------------------------------
class AddNewLection(CreateView):
    model = Lection
    template_name = 'lessons/lection_add.html'
    # fields = '__all__'
    form_class = CreateNewLection
    # fields = ('title', 'body', 'document', 'open_time')

class LectionView(ListView):
    model = Lection
    template_name = 'lessons/lections.html'

class LectionDetailView(DetailView):
    model = Lection
    template_name = 'lessons/lection_detail.html'
# -----------------------------------------------------


# Practices--------------------------------------------
class PracticeDetailView(DetailView):
    model = Practice
    template_name = 'lessons/practice_detail.html'

# -----------------------------------------------------
