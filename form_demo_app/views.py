from django.shortcuts import render
from django.views.generic import View
from .forms import MessageBoardForm
from django.http import HttpResponse


class BoardView(View):
    def get(self, request):
        form = MessageBoardForm()
        return render(request, "form_demo_app/board.html", context={'form': form})

    def post(self, request):
        form = MessageBoardForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            context = form.cleaned_data.get('context')
            email = form.cleaned_data.get('email')
            reply = form.cleaned_data.get('reply')
            print("="*30)
            print("{},{},{},{}".format(title, context, email, reply))
            return HttpResponse('success')
        else:
            print(form.errors.get_json_data())
            return HttpResponse("error")
