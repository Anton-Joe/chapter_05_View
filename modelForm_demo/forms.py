from django import forms
from .models import Book,User2


class BookForm(forms.ModelForm):
    def clean_page(self):
        page = self.cleaned_data.get('page')
        if page > 100:
            return ValueError('PAGE 大于 100')
        return page

    class Meta:
        model = Book
        fields = '__all__'
        # fields = ['price', 'title']
        # exclude = ['price']
        error_messages = {
            'page': {
                'required': '请输入page',
                'invalid': '请输入一个有效参数'
            }
        }


class UserForm(forms.ModelForm):
    pwd1 = forms.CharField(max_length=10, min_length=1)
    pwd2 = forms.CharField(max_length=10, min_length=1)

    def clean(self):
        cleaned_data = super().clean()
        pwd1 = cleaned_data.get('pwd1')
        pwd2 = cleaned_data.get('pwd2')
        if pwd1 != pwd2:
            raise forms.ValidationError("两次密码输入不一致")
        else:
            return cleaned_data

    class Meta:
        model = User2
        fields = ['username']