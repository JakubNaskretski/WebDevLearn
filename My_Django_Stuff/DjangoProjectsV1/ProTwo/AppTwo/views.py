from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User

# Create your views here.
def index0(request):
    return HttpResponse("<em>My Second App</em>")

def help(request):
    my_dict = {'Insert_me': "Insert_me from views.py",}
    return render(request, "AppTwo/Index.html", context=my_dict)
