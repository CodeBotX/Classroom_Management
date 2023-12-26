from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('classroom/', views.classroom, name='Classroom'),
    path('home/', views.Home, name='home'),
    path('register/', views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name="logout"),
]
