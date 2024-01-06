from typing import Any
from django import forms
import re 
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

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