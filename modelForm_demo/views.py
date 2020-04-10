from django.shortcuts import render
from .forms import BookForm, UserForm, PlayerForm
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views import View
# Create your views here.


@require_POST
def modelform_view(request):
    form = BookForm(request.POST)
    print(request.POST)
    if form.is_valid():
        return HttpResponse('success')
    else:
        print(form.errors.get_json_data())
        return HttpResponse('FAIL')


@require_POST
def modelform_save_view(request):
    form = UserForm(request.POST)
    if form.is_valid():
        # 这个方法可以直接将表单数据存入数据库，前提条件是表单字段与数据库模型字段一致
        # form.save()
        # 用户注册时输入了重复密码，不能直接使用save()方法，可以添加commit参数，阻止其提交，使用它的返回值，为返回值添加password，再save()
        user = form.save(commit=False)
        user.password = form.cleaned_data.get('pwd1')
        user.save()
        return HttpResponse('success')
    else:
        print(form.errors.get_json_data())
        return HttpResponse('FAIL')


class PlayerFormView(View):
    def get(self, request):
        return render(request, 'player_form.html')

    def post(self, request):
        form = PlayerForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return HttpResponse('success')
        else:
            print(form.errors.get_json_data())
            return HttpResponse('Fail')

