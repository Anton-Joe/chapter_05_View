"""chapter_05 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from article import views
urlpatterns = [
    path('', views.index),
    path('login', views.login, name='login'),
    path('ProfileView/', views.ProfileView.as_view(), name='ProfileView'),
    path('add_article', views.add_article, name='add_article'),
    path('download_csv', views.download_csv, name='download_csv'),
    path('download_csv_with_template', views.download_csv_with_template, name='download_csv_with_template'),
    path('add_car', views.add_car, name='add_car'),
    path('car_list', views.CarListView.as_view(), name='car_list'),

]
