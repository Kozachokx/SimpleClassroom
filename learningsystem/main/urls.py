from learningsystem.settings import MEDIA_ROOT, MEDIA_URL
from django.conf import settings
from django.conf.urls.static import static

from django.conf import settings
from django.urls import path
from . import views

from django.conf.urls import include, url
from django.contrib import admin

from .views import *

# from django.contrib.auth import logout
from django.contrib.auth.views import LogoutView


urlpatterns = [
# Auth
    path('index', views.index),
    path('register', views.registerPage, name='register'),
    path('login', views.loginPage, name='login'),
    url(r'^logout$', LogoutView.as_view(),  name='logout'),
    path('reg', views.registerPage),
    
# Lessons
    path('classroom/<int:pk>/', ViewTeacherClass.as_view(), name="classroom"),

#   Lections
    path('add_lection/', AddNewLection.as_view(), name="lection-add"),
    path('edit_lection/<int:pk>', UpdateLection.as_view(), name="lection-edit"),
    path('delete_lection/<int:pk>', DeleteLection.as_view(), name="lection-delete"),
    path('classroom/<int:tpk>/lection/id/<int:pk>', LectionDetailView.as_view(), name="lection-details"),

#   Practises
    path('add_practice/', AddNewPractice.as_view(), name="practice-add"),
    path('classroom/<int:tpk>/practice/id/<int:pk>', PracticeDetailView.as_view(), name="practice-details"),
    path('classroom/<int:tpk>/practice/<int:pk>', PracticeDetailExtendedView.as_view(), name="practice-ex-details"),
    path('classroom/<int:tpk>/practice_edit/<int:pk>', PracticeUpdate.as_view(), name="practice-edit"),
    path('classroom/<int:tpk>/practice_delete/<int:pk>', PracticeDelete.as_view(), name="practice-delete"),

    path('classroom/<int:tpk>/practice_pass/<int:pk>/', views.upload_practice, name='practice-pass'),
    # path('classroom/<int:tpk>/practice_pass/<int:pk>/', PassPractice.as_view(), name="practice-pass"),
    # path('classroom/<int:tpk>/practice_pass/<int:pk>/', views.pass_practice, name='practice-pass'),


#   Tests
    path('add_test/', AddNewTest.as_view(), name="test_add_1"),
    path('add_new_test/', views.addTest, name='test_add'),
    # path('test_add/', PracticeDetailView.as_view(), name="test-add"),

# End_Lessons


    path('', TeacherList.as_view(), name='main'),

    path('teacher', views.teacherPage),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)