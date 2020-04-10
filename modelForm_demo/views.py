from django.shortcuts import render
from .forms import BookForm
from django.http import HttpResponse

# Create your views here.


def modelform_view(request):
    form = BookForm(request.POST)
    if form.is_valid():
        return HttpResponse('success')
    else:
        print(form.errors.get_json_data())
        return HttpResponse('FAIL')