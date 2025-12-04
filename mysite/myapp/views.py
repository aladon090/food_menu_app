from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm

# Create your views here.

def index(request):
    #Getting items from the database
    list_items = Item.objects.all()
    #getting the context to parse the html with the method
    context = {
        'list_items': list_items # these two should be the same to prevent errors
    }
    print(context)

    return render(request,template_name="myapp/index.html",context=context)


def detail(request, id):
    print(id)
    item = get_object_or_404(Item, id=id)  # fetch a single item or 404 if not found

    context = {
        'item': item,  # match the template variable
    }

    return render(request, 'myapp/details.html', context)

def create_items(request):
    # if request is GET then its stay none if post then goes ahead
    form = ItemForm(request.POST or None)

    if request.method=="POST":

        if form.is_valid():
            form.save()
            return redirect('myapp:index')
    # if its get it return the the form on the page
    context = {
        'form':form
    }
    return render(request,'myapp/item-form.html', context)


def update(request, update_id):
    item = get_object_or_404(Item, id=update_id)

    form = ItemForm(request.POST or None ,instance=item)

    if request.method == "POST":

        if form.is_valid():
            form.save()
            return redirect('myapp:index')
    context = {
        'form': form,
        'item': item,
        'id': update_id,
    }
    return render(request, 'myapp/update.html',context)



def delete(request, delete_id):
    item = get_object_or_404(Item, id=delete_id)

    if request.method == "POST":  # user confirmed deletion
        item.delete()
        return redirect('myapp:index')

    context = {
        'item':item,
    }

    # GET request → show confirmation page
    return render(request, 'myapp/confirm_delete.html', context)







