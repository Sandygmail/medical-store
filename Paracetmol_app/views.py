
from django.shortcuts import render, redirect
from .models import Registation
from .forms import RegistationForm
# Create your views here.


def RegisterForm(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = RegistationForm()
        else:
            editUser = Registation.objects.get(pk=id)
            form = RegistationForm(instance=editUser)
        return render(request, "registe_form.html", {'userData': form})
    else:
        if id == 0:
            form = RegistationForm(request.POST)
        else:
            editUser = Registation.objects.get(pk=id)
            form = RegistationForm(request.POST, instance=editUser)
        if form.is_valid():
            form.save()
        return redirect('login')


def login(request):
    if request.method == 'POST':
        name = request.POST['user']
        if name == "premchand@gmail.com":
            return redirect('user_details')

    return render(request, "login.html")


def user_details(request):
    users = Registation.objects.all
    return render(request, "register_details.html", {'userData': users})


def user_delete(request, id):
    user = Registation.objects.get(pk=id)
    user.delete()
    return redirect('user_details')
