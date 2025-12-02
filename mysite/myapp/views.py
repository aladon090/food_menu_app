from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

# Create your views here.

def index(request):
    #Getting items from the database
    list_items = Item.objects.all()
    #getting the context to parse the html with the method
    context = {
        'list_items': list_items
    }

    return render(request,template_name="myapp/index.html",context=context)

def detail(request, id):
    items = Item.objects.filter(id=id)
    print(items)
    food = Item.objects.filter(item_name='eggs')
    context = {
        'item':items,
        'food':food
    }

    return render(request,template_name='myapp/food.html',context=context)

def book(request):
    return HttpResponse("<h2>Book in today</h2>")