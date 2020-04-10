from django import forms


class MessageBoardForm(forms.Form):
    title = forms.CharField(min_length=2, max_length=100, label='标题', error_messages={"min_length": "最短长度为2"})
    context = forms.CharField(widget=forms.Textarea, label='留言内容')
    email = forms.EmailField(label='邮箱')
    reply = forms.BooleanField(required=False, label='是否需要回复')

