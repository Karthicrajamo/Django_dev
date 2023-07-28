from django.shortcuts import render
from . models import *

# Create your views here.
def home(request):
    return render(request,"items/index.html")

def calculate():
    x=1
    y=2 
    return x

def reg(request):
    x = calculate()
    return render(request, "items/register.html")

def collections(request):
    catagory = Catagory.objects.filter(status=0)
    return render(request, 'items/collections.html', {"catagory" : catagory})