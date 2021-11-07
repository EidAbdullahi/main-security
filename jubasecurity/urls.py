
from django.contrib import admin
from django.urls import path
from juba import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view,name=''),



   # path('adminsignup', views.admin_signup_view),
   # path('studentsignup', views.student_signup_view,name='studentsignup'),
   # path('teachersignup', views.teacher_signup_view),
   path('adminlogin', LoginView.as_view(template_name='juba/adminlogin.html')),
   path('logisticlogin', LoginView.as_view(template_name='juba/logisticlogin.html')),
   path('oblogin', LoginView.as_view(template_name='juba/oblogin.html')),
   path('cidlogin', LoginView.as_view(template_name='juba/cidlogin.html')),
   # path('studentlogin', LoginView.as_view(template_name='school/studentlogin.html')),
   # path('teacherlogin', LoginView.as_view(template_name='school/teacherlogin.html')),
    path('admin-add-police', views.admin_add_police_view,name='admin-add-police'),
    path('admin-view-police', views.admin_view_police_view,name='admin-view-police'),


    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('logout', LogoutView.as_view(template_name='juba/index.html'),name='logout'),


    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),
    path('admin-police', views.admin_police_view,name='admin-police'),


    path('aboutus', views.aboutus_view),
    path('contactus', views.contactus_view),
  
]
