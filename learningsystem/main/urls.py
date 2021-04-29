from django.urls import path
from . import views

from .views import TeacherList, ViewTeacherClass, LectionView,  LectionDetailView, AddNewLection, PracticeDetailView

urlpatterns = [
# Auth
    path('index', views.index),
    path('login', views.loginPage),
    path('reg', views.registerPage),
    path('register', views.registerPage),

# Lessons
    path('classroom/<int:pk>/', ViewTeacherClass.as_view(), name="classroom"),
#   Lections
    path('add_lection/', AddNewLection.as_view(), name="lection-add"),
    path('classroom/<int:tpk>/lection/id/<int:pk>', LectionDetailView.as_view(), name="lection-details"),
#   Practises
    path('classroom/<int:tpk>/practice/id/<int:pk>', PracticeDetailView.as_view(), name="practice-details"),

#   Tests
# End_Lessons



    path('', TeacherList.as_view(), name='main'),


    path('teacher', views.teacherPage),
]