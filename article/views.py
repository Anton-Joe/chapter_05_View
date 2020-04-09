# -*-coding:utf-8 -*-
from django.shortcuts import render, redirect, reverse
from .models import Article, Car
from django.views.decorators.http import require_GET, require_http_methods
from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView, View
from django.utils.decorators import method_decorator
import csv, codecs
# Create your views here.

# @require_GET
@require_http_methods(['GET'])
def index(request):
    articles = Article.objects.all()
    return render(request, 'index1.html', context={'articles': articles})


@require_http_methods(['POST', 'GET'])
def add_article(request):
    if request.method == 'GET':
        return render(request, 'add_article.html')
    else:
        title = request.POST.get('title')
        content = request.POST.get('content')
        Article.objects.create(title=title, content=content)
        return HttpResponse('success')


def download_csv(request):
    response = HttpResponse(content_type='text/csv')
    response.write(codecs.BOM_UTF8)
    response['Content-Disposition'] = "attachment;filename=test_download.csv"
    writer = csv.writer(response)
    writer.writerow(['姓名', '年龄'])
    writer.writerow(['叶敬轩', '18'])
    return response


def download_csv_with_template(request):
    response = HttpResponse(content_type='text/csv')
    response.write(codecs.BOM_UTF8)
    response['Content-Disposition'] = "attachment;filename=test_download_with_template.csv"
    context = {
        'rows': [
            ['name', 'age'],
            ['jett', '18'],
        ]
    }
    template = loader.get_template('download_csv_template')
    csv_template = template.render(context)
    response.content = csv_template
    return response


def add_car(request):
    cars = []
    for i in range(1000):
        car = Car(owner=str(i))
        cars.append(car)
    Car.objects.bulk_create(cars)
    return HttpResponse('车辆信息添加成功')


def login(request):
    return HttpResponse('登录页面')


def login_required(func):
    def wrapper(request, *args, **kwargs):
        username = request.GET.get('username')
        print(username)
        if username:
            return func(request, *args, **kwargs)
        else:
            return redirect(reverse('login'))
    return wrapper


@method_decorator([login_required], name='dispatch')
class ProfileView(View):
    def get(self, request):
        return HttpResponse("个人中心页面")

    # @method_decorator(login_required)
    # def dispatch(self, request, *args, **kwargs):
    #     return super(ProfileView, self).dispatch(request, *args, **kwargs)


class CarListView(ListView):
    # 对应模型
    model = Car
    # 对应模板名字
    template_name = 'car_list.html'
    # 每一页多少个模型
    paginate_by = 10
    # 模板中变量的名字
    context_object_name = 'Cars'
    # 排序规则
    ordering = 'buy_date'
    # URL中分页使用的参数关键字
    page_kwarg = 'p'

    # 此方法可以得到传递给模板的context，可以再次修改context内容
    def get_context_data(self, **kwargs):
        context = super(CarListView, self).get_context_data(**kwargs)
        pagination_data = self.get_pagination_data(context.get('paginator'), context.get('page_obj'))
        context.update(pagination_data)
        return context

    # 此方法类似于SQL的WHERE条件
    def get_queryset(self):
        # return Car.objects.filter(owner__gte=10)
        return Car.objects.all()

    # 分页算法
    def get_pagination_data(self, paginator, page_obj, around_count=2):
        current_page = page_obj.number
        num_pages = paginator.num_pages

        left_has_more = False
        right_has_more = True

        if current_page <= around_count + 2:
            left_pages = range(1, current_page)
        else:
            left_pages = range(current_page - around_count, current_page)
            left_has_more = True

        if current_page >= num_pages - around_count + 1:
            right_pages = range(current_page+1, num_pages+1)
        else:
            right_pages = range(current_page+1, current_page+around_count+1)
            right_has_more = True

        return {
            'left_pages': left_pages,
            'left_has_more': left_has_more,
            'right_pages': right_pages,
            'right_has_more': right_has_more,
            'current_page': current_page,
            'num_pages': num_pages
        }
