import re
from django.shortcuts import render
from django.urls import is_valid_path
from matplotlib.style import context
from .forms import LoginForm
# Create your views here.
import requests

endpoint="http://127.0.0.1:5000/"

def login(request):
    context={
        'title':'Login'
    }
    return render(request,'login.html',context)

def home(request):
    contexto={
        'title':'Home'
    }
    return render(request, 'home.html', contexto)

def signin(request):
    contexto={}
    if request.method=='GET':
        form = LoginForm(request.GET)
        if form.is_valid():
            user= form.cleaned_data['username']
            passw=form.cleaned_data['password']
            r=requests.get(endpoint+'login/'+user+'/'+passw);
            #http://127.0.0.1:5000/login/jacks128/admin
            data=r.json()
            print(data['data'])
            if data['data']==True:
                contexto={
                    'title':'Home'
                }
    return render(request,'home.html',contexto)




