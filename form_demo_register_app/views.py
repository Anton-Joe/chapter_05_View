from django.shortcuts import render
from django.views import View
from .forms import RegisterForm
from .models import User
from django.http import HttpResponse
# Create your views here.


class RegisterView(View):
    def get(self, request):
        return render(request, 'form_demo_register_app/register_view.html')

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            telephone = form.cleaned_data.get('telephone')
            User.objects.create(username=username, password=password, telephone=telephone)
            return HttpResponse('注册成功')
        else:
            print(form.errors.get_json_data())
            return HttpResponse('注册出错')

