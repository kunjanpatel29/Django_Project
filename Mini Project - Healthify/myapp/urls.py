from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('signup/',views.signup,name='signup'),
    path('signin/',views.signin,name='signin'),
    path('signout/',views.signout,name='signout'),
    path('change-password/',views.change_password,name='change-password'),
    path('profile/',views.profile,name='profile'),
]