from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('signupform/',views.signupform,name='signupform'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('loginform/',views.loginform,name='loginform'),
    path('quiz0/',views.quiz0,name='quiz0'),
    path('quiz02/',views.quiz02,name='quiz02'),
    path('quiz12/',views.quiz12,name='quiz12'),
    path('quiz13/',views.quiz13,name='quiz13'),
    path('quiz14/',views.quiz14,name='quiz14'),
    path('quiz15/',views.quiz15,name='quiz15'),
    path('quiz16/',views.quiz16,name='quiz16'),
    path('quiz17/',views.quiz17,name='quiz17'),
    path('quiz18/',views.quiz18,name='quiz18'),
    path('quiz19/',views.quiz19,name='quiz19'),
    path('quiz20/',views.quiz20,name='quiz20'),
    path('quiz21/',views.quiz21,name='quiz21'),
    path('quiz22/', views.quiz22, name='quiz22'),
    path('quiz23/', views.quiz23, name='quiz23'),
    path('quiz24/', views.quiz24, name='quiz24'),
    path('quiz25/', views.quiz25, name='quiz25'),
    path('quiz26/', views.quiz26, name='quiz26'),
    path('quiz27/', views.quiz27, name='quiz27'),
    path('quiz28/', views.quiz28, name='quiz28'),
    path('quiz29/', views.quiz29, name='quiz29'),
    path('quiz30/', views.quiz30, name='quiz30'),
    path('quiz31/', views.quiz31, name='quiz31'),

]
