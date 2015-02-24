from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required()
def user_account(request):
    return render(request, 'account.html')
def user_home(request):
    return render(request, 'home.html')


