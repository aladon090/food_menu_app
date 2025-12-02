from django.contrib import admin
from django.urls import path
from . import views

app_name='myapp'

urlpatterns = [
    path('',views.index,name='index'),
    path('book/',views.book),
    path('<int:id>',views.detail,name='detail'),
]