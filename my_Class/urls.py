from django.urls import path
from . import views
from .views import CustomLoginView
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView


urlpatterns = [

    path('home/', CustomLoginView.as_view(template_name='login.html'), name='home'),
    path('option/', views.option_view, name='option'),
    path('classroom/',views.classroom_view , name='Classroom'),
    path('register/', views.register_view, name='register'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name="logout"),
    # details
    path('student/<int:student_ID>', views.student_detail, name='student_detail'),
    # 
    path('student_grade/<int:student_ID>', views.student_grade_view, name='student_grade_view'),
    path('reviewweekend/',views.week_summary_view , name='reviewweekend'),
    # path('student/<int:student_ID>/save_score/',views.save_score, name='save_score'),
    path('test/',views.test_saveScore, name='test'),
    
]

