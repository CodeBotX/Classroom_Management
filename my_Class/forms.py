from typing import Any
from django import forms
import re 
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .models import *

class RegistrationForm(forms.Form):
    username = forms.CharField(label='Tài Khoản', max_length=50)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Mật Khẩu', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Nhập Lại Mật Khẩu', widget=forms.PasswordInput())
    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1==password2 and password1:
                return password2
        raise forms.ValidationError('Mật Khẩu không Hợp Lệ')
    def clean_username(self):
        username = self.cleaned_data['username']
        if re.search(r'^\w+s', username):
            raise forms.ValidationError('Tên Tài Khoản Chứa Kí Tự Đặc Biệt')
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError('Tài Khoản Đã Tồn Tại')
    def save(self):
        User.objects.create_user(username=self.cleaned_data['username'], email=self.cleaned_data['email'], password=self.cleaned_data['password2'])
        
class StudentIDForm(forms.Form):
    student_id = forms.IntegerField(
        label='Student ID',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'id': 'Student ID',
                'placeholder': 'Enter Student ID',
                'name': 'Student ID'
            }
        )
    )

from django.contrib.auth.forms import AuthenticationForm

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'Student ID',
                'placeholder': 'Enter Student ID',
                'name': 'Student ID'
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'id': 'Password',
                'placeholder': 'Enter Password',
                'name': 'Password'
            }
        )
    )





class ScoreForm_Test(forms.ModelForm):
    class Meta:
        model = Score
        fields = ['student','subject','K1_score', 'K2_score', 'K3_score']
        
class LessonReviewForm(forms.ModelForm):
    class Meta:
        model = LessonReview
        fields = ['lesson', 'review', 'rating']
        widgets = {
            'lesson': forms.Select(attrs={'class': 'form-control'}),
            
        }


class LessonsForm(forms.ModelForm):
    class Meta:
        model = Lessons
        fields = ['classroom', 'subject', 'teacher']