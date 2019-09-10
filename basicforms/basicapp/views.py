from django.shortcuts import render
from . import forms
from basicapp.models import User
from basicapp.forms import NewUserForm

# Create your views here.

def index(request):
    return render(request, 'basicapp/index.html')

def users(request):
    user_list = User.objects.all()
    user_dict = {'user_records':user_list}
    return render(request, 'basicapp/users.html', context=user_dict)

def formpage(request):
    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("ERROR FORM INVALID")

    return render(request, 'basicapp/form_page.html',context={'form':form})
