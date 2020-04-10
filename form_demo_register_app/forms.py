from django import forms
from .models import User


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100, min_length=1, label='登录名')
    telephone = forms.CharField(max_length=100, label='电话')
    password1 = forms.CharField(max_length=100, min_length=1, label='密码')
    password2 = forms.CharField(max_length=100, min_length=1, label='重复密码')

    def clean_telephone(self):
        telephone = self.cleaned_data.get('telephone')
        exits_flag = User.objects.filter(telephone=telephone).exists()
        if exits_flag:
            raise forms.ValidationError("手机号已存在！")
        else:
            return telephone

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError("输入密码不一致！")
        else:
            return cleaned_data
