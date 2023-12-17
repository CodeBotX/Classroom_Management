from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView


urlpatterns = [
    # path('login/', auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('login/', views.siteLoginView.as_view(),name='login'),
    path('classroom/',views.classroom_view , name='Classroom'),
    path('home/', views.Home_view, name='home'),
    path('register/', views.register_view, name='register'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name="logout"),
]

# {'next_page':'login'}
# login_required(views.classroom_view)