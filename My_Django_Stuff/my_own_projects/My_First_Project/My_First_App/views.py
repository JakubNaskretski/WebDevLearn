from django.shortcuts import render
# from django.http import HttpResponse
# import datetime
# Create your views here.

# def current_datetime(request):
#     now = datetime.datetime.now()
#     html = "<html><body>It is now %s.</body></html>" % now
#     return HttpResponse(html)

def firstview(request):
    my_dict = {'test':"Hello Im From My_First_App!"}
    return render(request,'My_First_App/firstview.html',context=my_dict)