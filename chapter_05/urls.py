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
from form_demo_app import views as form_view
from form_demo_register_app import views as register_view
from modelForm_demo import views as view3
urlpatterns = [
    path('', views.index),
    path('login', views.login, name='login'),
    path('ProfileView/', views.ProfileView.as_view(), name='ProfileView'),
    path('add_article', views.add_article, name='add_article'),
    path('download_csv', views.download_csv, name='download_csv'),
    path('download_csv_with_template', views.download_csv_with_template, name='download_csv_with_template'),
    path('add_car', views.add_car, name='add_car'),
    path('car_list', views.CarListView.as_view(), name='car_list'),
    path('board_view', form_view.BoardView.as_view(), name='board_view'),
    path('register_view', register_view.RegisterView.as_view(), name='register_view'),
    path('modelform_view', view3.modelform_view, name='modelFrom_View'),
    path('modelform_save_view', view3.modelform_save_view, name='modelform_save_view'),
    path('PlayerFormView', view3.PlayerFormView.as_view(), name='PlayerFormView'),
]
