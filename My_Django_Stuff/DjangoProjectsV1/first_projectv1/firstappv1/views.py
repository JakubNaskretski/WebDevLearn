from django.shortcuts import render
from django.http import HttpResponse
#step 1 MTV
from firstappv1.models import Topic,Webpage,AccessRecord

# Create your views here.

# def index0(request):
#     return HttpResponse("<B>Hello you are in main site.</B>"
#     "\nPlease choose index1 or index2 to specify")
def index0(request):
    webpages_list = AccessRecord.objects.order_by('date')

    #step 2 MTV
    date_dict = {'access_records':webpages_list}
    my_dict = {'insert_me0':"Index0 from views.py", 'insert_me1': "insert_me1 tryout"}
    return render(request, 'firstappv1/index0.html', context=date_dict)

def index1(request):
    return HttpResponse("Hello inside index 1")

def index2(request):
    return HttpResponse("Hello inside index 2")

def indexnumber(request, indexnumber):
    response = "You are looking at the index %s."
    return HttpResponse(response % indexnumber)
