from django.shortcuts import render,redirect

from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request):
    return render(request,'home/index.html')

