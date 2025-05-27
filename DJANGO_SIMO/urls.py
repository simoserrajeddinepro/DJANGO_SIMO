"""
URL configuration for DJANGO_SIMO project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from Hello_Simo.views import hello_view, personalized_hello , student_list , add_student , update_student, delete_student ,register
from Hello_Simo.views import dashboard


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello_view), # default homepage
    path('hello/<str:name>/', personalized_hello), # dynamic URL

    path('students/', student_list,name='student_list'),  # 🆕
    path('add/', add_student, name='add_student'),

    path('students/<int:id>/edit/', update_student, name='update_student'),
    path('students/<int:id>/delete/', delete_student, name='delete_student'),

    path('login/', auth_views.LoginView.as_view(template_name='Hello_Simo/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', register, name='register'),

    path('dashboard/', dashboard, name='dashboard'),




]
