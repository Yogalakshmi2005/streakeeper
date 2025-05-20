from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('',views.logo_splash_view, name='logo_splash'),
    path('home/', views.home_view, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='skapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('dashboard/', views.dashboard_view, name='dashborad'),
    path('create_goal/', views.create_goal_view, name='create_goal'),
    path('check_in/', views.check_in_view, name='check_in'),
]
