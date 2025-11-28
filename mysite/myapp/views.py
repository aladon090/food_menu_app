from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello world ")

def book(request):
    return HttpResponse("<h2>Book in today</h2>")