from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login



from django.views.generic import CreateView, ListView, DetailView, DeleteView

from .forms import *
from .models import Lection, Practice, PracticeResult, Student, Teacher, Test

from .forms import LoginStudent, LoginForm
from django.shortcuts import redirect

def registerPage(request):
    form = CreateStudent(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            # user = None
            cd = form.cleaned_data
            Student.objects.create_user(username=cd['username'], password=cd['password'], email=cd['email'], first_name=cd['first_name'], last_name=cd['last_name'])
            # user_login = cd['username']
            # user_password = cd['password']
            # fn = cd['first_name']
            # ln = cd['last_name']
            # em = cd['email']
            # print(" - USER - " + user_login + " " + user_password + " " + fn + " " + ln + " " + em)
            # print(user)
            form.full_clean()
            messages.success(request,'User has beem registered.')
            # return HttpResponse('User successfully registered!')
            return redirect('/login')

    context = {'form':form}
    return render(request, 'auth/register.html', context)

    
# def registerPage(request):
#     # form = UserCreationForm()
#     form = CreateStudent()
#     if request.method == 'POST':
#         form = CreateStudent(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request,'User has beem registered.')

#     context = {'form':form}
#     return render(request, 'auth/register.html', context)

# def authenticate(username=None, password=None, **kwargs):
#         from django.contrib.auth import get_user_model
#         UserModel = get_user_model()
#         if username is None:
#             username = kwargs.get(UserModel.USERNAME_FIELD)
#         try:
#             user = UserModel._default_manager.get_by_natural_key(username)
#             if user.check_password(password):
#                 return user
#         except UserModel.DoesNotExist:
#             # Run the default password hasher once to reduce the timing
#             # difference between an existing and a non-existing user (#20760).
#             UserModel().set_password(password)


# def loginPage(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = request.POST.get('username')
#             password = request.POST.get('password')
#             user = authenticate(username=username, password=password)
#             if user:
#                 if user.is_active:
#                     login(request,user)
#                     return HttpResponseRedirect(reverse(''))
#                 else:
#                     return HttpResponse("Your account was inactive.")
#             else:
#                 print("-------Someone tried to login and failed.")
#                 print("-------They used username: {} and password: {}".format(username,password))
#                 return HttpResponse("Invalid login details given")
#     else:
#         form = LoginForm()
#     return render(request, 'auth/login.html', {'form': form})














# DDDDEEEEBBBBBBBBBBUUUUUUUUUGGGGGGGG
# def loginPage(request):
#     print("-----------------------------")

#     # user = Student.objects.create_user( username="whatever", email="whatever@some.com", password="password")
#     user = authenticate( username="whatever",password="password")
#     print(user)
#     print(user.check_password("password"))
#     # user.set_password()

#     user = authenticate( username="wtfisthis",password="pizdecNahyi5")
#     print(user)

#     user = authenticate( username="NEWS",password="123")
#     print(user)

#     # print("Login tryout by ")
#     # print("Login result ")
#     # print(user)
#     print("-----------------------------")
#     return render(request, 'auth/login.html')


# def loginPage(request):
#     user = None

#     user_login = 'aaa123'
#     user_password = 'SybaKa007!'

#     user = authenticate(username=user_login, password=user_password)

#     noUser = user == None

#     print("Login tryout by "+user_login +" "+user_password)
#     print("Login result ")
#     print(user)
#     print("-----------------------------")

#     return render(request, 'auth/login.html')


def loginPage(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = None
        
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])

            user_login = cd['username']
            user_password = cd['password']
            print("Login tryout by "+user_login)
            print(user)

            if user_login != "" and user_password != "":
                user = authenticate(username=user_login, password=user_password)
            
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # return HttpResponse('Authenticated successfully')
                    return redirect('/')

                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login' + "\n User was "+cd['username']+" "+cd['password'])
    else:
        form = LoginForm()
    return render(request, 'auth/login.html', {'form': form})


def logout(request):
    logout(request)

# def loginPage(request):
#     if request.method == "POST":
#         form = LoginForm(request.POST)
#         cd = form.cleaned_data
#         user = authenticate(username=cd['username'], password=cd['password'])
        
#         user = None
#         user_login = request.POST['login']
#         user_password = request.POST['password']

#         if user_login != "" and user_password != "":
#             user = authenticate(username=user_login, password=user_password)

#         if user is not None:
#             login(request, user)
#             return HttpResponseRedirect(reverse('public_gate:home'))
#         else:
#             # User.objects.create_user(user_login, '', user_password).save()
#             return render(request, 'auth/login.html', {"error_message": "Wrong login/password combination"})
#     return render(request, 'auth/login.html', {"error_message": "One or more fields are empty"}) 

# def loginPage(request):
#     form = LoginStudent()
#     # username = request.POST['username']
#     # password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         # Redirect to a success page.
#     # else:
#         # Return an 'invalid login' error message.
#     context = {}
#     return render(request, 'auth/login.html', context)


# def loginPage(request):
#     context = {}
#     return render(request, 'auth/login.html', context)

def index(request):
    return render(request, 'auth/index.html')


def teacherPage(request):
    context = {'lection_list':Lection}
    return render(request, 'main/teacherPage.html', context)

def addTest(request):
    context = {}
    return render(request, 'lessons/test_add.html', context)



# def upload(request):
#     if request.method == 'POST':
#         upload_file = request.FILES['document']
#         print(upload_file.name)
#         print(upload_file.size)
#     return render(request, 'upload.html')

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
        tests = Test.objects.filter( author__id = teacher_id )

        context = {'lections': lections, 'practices': practices, 'tests': tests, 'teacher_id': teacher_id}
        return render(request, self.template_name, context=context)




# Lections---------------------------------------------
class AddNewLection(CreateView):
    model = Lection
    template_name = 'lessons/lection_add.html'
    # fields = '__all__'
    form_class = CreateNewLection
    # fields = ('title', 'body', 'document', 'open_time')
    def post(self,request):
        form = CreateNewLection(request.POST)
        if form.is_valid():
            test = form.save(commit=False)
            test.author = Teacher.objects.get(pk=request.user.id)
            test.save()
            # pass
        return render(request, self.template_name, {'form':form})

class LectionView(ListView):
    model = Lection
    template_name = 'lessons/lections.html'

class LectionDetailView(DetailView):
    model = Lection
    template_name = 'lessons/lection_detail.html'
# -----------------------------------------------------




# Practices--------------------------------------------
class AddNewPractice(CreateView):
    model = Practice
    template_name = 'lessons/practice_add.html'
    # fields = '__all__'
    form_class = CreateNewPractice
    # fields = ('title', 'body', 'document', 'open_time')

    def post(self,request):
        form = CreateNewPractice(request.POST)
        if form.is_valid():
            test = form.save(commit=False)
            test.author = Teacher.objects.get(pk=request.user.id)
            print(f"----------STUDENTS 2 : {form.cleaned_data['students']}   ---------------------")
            # test.students = form.cleaned_data['students']
            test.save()
            test.students.set(form.cleaned_data['students'])

            # student_lst = form.cleaned_data['students']
            # lsit1 = Student.objects.filter(username__in = student_lst)

            # # test.students.set(students)
            # for x in student_lst:
            #     print(f"              {User.objects.get(pk = x.id)}-  -  -  -  -  -  {x}       =    {x.id}   {x.username}")
            #     test.students.add(x)
            
            # test.save()
            # pass
        return render(request, self.template_name, {'form':form})
    

class PracticeDetailView(DetailView):
    model = Practice
    template_name = 'lessons/practice_detail.html'

class PracticeDetailExtendedView(DetailView):
    model = Practice
    template_name = 'lessons/practice_extended_detail.html'

    def get(self, request, *args, **kwargs):
        teacher_id = self.kwargs['tpk']
        practice_id = self.kwargs['pk']

        practice = Practice.objects.get( id = practice_id )
        practice_results = PracticeResult.objects.filter( id = practice_id )
        
        print(f"  - - - - - -- - - - - - -- - - --   {practice_results}")

        context = {'practice': practice, 'practice_results':  practice_results, 'teacher_id': teacher_id, 'practice_id': practice_id}
        return render(request, self.template_name, context=context)

# -----------------------------------------------------


# Tests------------------------------------------------
class AddNewTest(CreateView):
    model = Test
    template_name = 'lessons/test_add_1.html'
    # fields = '__all__'
    form_class = CreateNewTest

    def post(self,request):
        form = CreateNewTest(request.POST)
        if form.is_valid():
            test = form.save(commit=False)
            test.author = Teacher.objects.get(pk=request.user.id)
            test.save()
            # pass
        return render(request, self.template_name, {'form':form})

    



# -----------------------------------------------------