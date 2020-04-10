from django import forms
from .models import Book


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