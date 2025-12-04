from django.contrib import admin
from django.urls import path
from . import views

app_name='myapp'

urlpatterns = [
    path('',views.index,name='index'),
    path('<int:id>',views.detail,name='detail'),
    path('add/',views.create_items, name='create_item'),
    path('update/<int:update_id>/', views.update, name='update_item'),
]