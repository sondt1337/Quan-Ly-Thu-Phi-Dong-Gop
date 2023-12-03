from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .models import FamilyMember
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.models import Group
from .models import CustomUser


def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.kichhoat:
                login(request, user)
                return redirect('homepage') 
            else:
                return render(request, 'myapp/wait.html')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')  

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def homepage(request):
    return render(request, 'myapp/homepage.html')

def about(request):
    return render(request, 'myapp/about.html')

def contact(request):
    return render(request, 'myapp/contact.html')

def notification(request):
    return render(request, 'myapp/notification.html')

@login_required
def personal(request):
    user = request.user
    user_groups = user.groups.all()
    group_name = user_groups[0].name if user_groups else None
    context = {
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'group_name': group_name,
    }

    return render(request, 'myapp/personal.html', context)

@login_required
def changepassword(request):
    user = request.user
    user_groups = user.groups.all()
    group_name = user_groups[0].name if user_groups else None
    context = {
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'group_name': group_name,
    }

    return render(request, 'myapp/changepassword.html', context)

@login_required
def password_change_done(request):
    return render(request, 'myapp/homepage.html')

@login_required
def service(request):
    contributing_users = CustomUser.objects.filter(donggop__gt=0)
    user_names = [user.last_name for user in contributing_users]
    user_info_list = [
        {
            'last_name': user.last_name,
            'first_name': user.first_name,
            'donggop': user.donggop,
            'group': user.group,
            'sukien': user.sukien,
        }
        for user in contributing_users
    ]

    return render(request, 'myapp/service.html', {'user_info_list': user_info_list})

@login_required
def wait(request):
    form = CustomAuthenticationForm(data=request.POST)
    if form.is_valid():
        user = form.get_user()
        if user.kichhoat:
            login(request, user)
            return redirect('homepage')
        else:
            return render(request, 'myapp/hompage.html')
    else:
        return redirect('homepage') 