from django.shortcuts import render
from apptwo.models import User
from apptwo.forms import UserForm

# Create your views here.

def index(request):
    return render(request, 'apptwo/index.html')


def users(request):

# call the user, grab all the objects, order by the 1st name.
    user_list = User.objects.order_by('first_name')
    user_dict = {'users':user_list}
    return render(request,'apptwo/users.html',context=user_dict)


def usersform(request):

    #form is an instance of class usersform
    form = UserForm()

    #If someone hit the submit button:
    if request.method == 'POST':
        #then we are passing the request.post
        form = UserForm(request.POST)

        #Check if form is valid(email is email etc)
        if form.is_valid():
            #saving posted thing
            form.save(commit=True)
            print ("Validation Success !")
            #if valid return index page
            return users(request)

        else:
            print ('ERROR FORM INVALID')

    return render(request, 'apptwo/forms.html', {'form':form})
