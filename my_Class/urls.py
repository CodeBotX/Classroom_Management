from django.urls import path
from . import views
from .views import CustomLoginView
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView


urlpatterns = [
    # path('login/', auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    # path('login/', views.siteLoginView.as_view(),name='login'),
    path('home/', CustomLoginView.as_view(template_name='login.html'), name='home'),
    path('option/', views.option_view, name='register'),
    path('classroom/',views.classroom_view , name='Classroom'),
    path('register/', views.register_view, name='register'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name="logout"),
    path('student/<int:student_ID>/', views.student_detail, name='student_detail'),
    path('student_grade/<int:student_ID>', views.student_grade_view, name='student_grade_view'),
    path('reviewweekend/',views.week_summary_view , name='reviewweekend'),
]

