
from django.contrib import admin
from django.urls import path
from juba import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view,name=''),



   
   path('adminlogin', LoginView.as_view(template_name='juba/adminlogin.html')),
   path('logisticlogin', LoginView.as_view(template_name='juba/logisticlogin.html')),
   path('oblogin', LoginView.as_view(template_name='juba/oblogin.html')),
   path('cidlogin', LoginView.as_view(template_name='juba/cidlogin.html')),
   
    path('admin-add-police', views.admin_add_police_view,name='admin-add-police'),
    path('admin-view-police', views.admin_view_police_view,name='admin-view-police'),

    path('admin-logistic', views.admin_logistic_view,name='admin-logistic'),
    path('admin-add-logistic', views.admin_add_logistic_view,name='admin-add-logistic'),
    path('admin-view-logistic', views.admin_view_logistic_view,name='admin-view-logistic'),
    path('logistic-dashboard', views.logistic_dashboard_view,name='logistic-dashboard'),
    path('logistic-cid', views.logistic_cid_view,name='logistic-cid'),
    path('logistic-police', views.logistic_police_view,name='logistic-police'),
    path('logistic-ob', views.logistic_ob_view,name='logistic-ob'),


    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('logout', LogoutView.as_view(template_name='juba/index.html'),name='logout'),


    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),
    path('admin-police', views.admin_police_view,name='admin-police'),
    path('admin-cid', views.admin_cid_view,name='admin-cid'),
    path('admin-ob', views.admin_ob_view,name='admin-ob'),
    path('admin-report', views.admin_report_view,name='admin-report'),
    path('delete-report/<int:pk>', views.delete_report_view,name='delete-report'),

    path('admin-add-cid', views.admin_add_cid_view,name='admin-add-cid'),
    path('admin-view-cid', views.admin_view_cid_view,name='admin-view-cid'),
    path('cid-dashboard', views.cid_dashboard_view,name='cid-dashboard'),

    path('ob-dashboard', views.ob_dashboard_view,name='ob-dashboard'),
    path('ob-add-report', views.ob_add_report_view,name='ob-add-report'),
    path('ob-view-report', views.ob_view_report_view,name='ob-view-report'),

    path('admin-add-ob', views.admin_add_ob_view,name='admin-add-ob'),
    path('admin-view-ob', views.admin_view_ob_view,name='admin-view-ob'),
    path('cid-add-report', views.cid_add_report_view,name='cid-add-report'),
    path('cid-view-report', views.cid_view_report_view,name='cid-view-report'),

    path('aboutus', views.aboutus_view),
    path('contactus', views.contactus_view),
  
]
