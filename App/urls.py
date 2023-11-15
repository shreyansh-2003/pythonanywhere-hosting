from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    #path('App/',views.members, name='page')
    path('login/', auth_views.LoginView.as_view(),name='login'),
    path('logout/', auth_views.LogoutView.as_view(),name='logout'),
    path('home/', views.home, name = 'home'),
    path('register/', views.register, name='register')
]

