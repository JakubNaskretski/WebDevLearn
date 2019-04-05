from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "appone/MainSite.html")

def AboutMe(request):
    return render(request, "appone/AboutMe.html")

def Contact(request):
    return render(request, "appone/Contact.html")

def ProOne(request):
    return render(request, "appone/ProOne.html")
