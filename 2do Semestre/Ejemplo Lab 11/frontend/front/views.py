import re
from django.shortcuts import render
from django.urls import is_valid_path
from matplotlib.style import context
from .forms import AddForm, FileForm, LoginForm
# Create your views here.
import requests

endpoint="http://127.0.0.1:5000/"

def login(request):
    context={
        'title':'Login'
    }
    return render(request,'login.html',context)

def home(request):
    contexto = {
        'canciones' : []
    }
    try:
        response = requests.get(endpoint + 'canciones') # http://127.0.0.1:5000/canciones
        canciones=response.json()
        contexto['canciones']=canciones
    except:
        print('Error en la API')
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

def add(request):
    if request.method=='POST':
        form=AddForm(request.POST)
        if form.is_valid():
            json_data=form.cleaned_data
            response=request.post(endpoint+'agregarCancion/',json=json_data)
             #http://127.0.0.1:5000/agregarCancion
            if response.ok:
                return render(request,'add.html',{'form':form})
        return render(request,'add.html',{'form':form})
    return render(request,'add.html')

def cargaMasiva(request):
    ctx={
        'content':None,
        'response':None
    }
    if request.method=='POST':
        form= FileForm(request.POST,request.FILES)
        if form.is_valid():
            f=request.FILES['file']
            xml_binary=f.read
            xml=xml_binary.decode('utf-8')
            ctx['content']=xml
            response = request.post(endpoint+'agregarCanciones',data=xml_binary)
            #http://127.0.0.1:5000/agregarCanciones
            if response.ok:
                ctx['response']="Archivo XML Cargado correctamente"
            else:
                ctx['response']="Archivo enviado incorrectamente, o hubo un error en el servidor"
    else:
        return render(request, 'carga.html')
    return render(request, 'carga.html', ctx)
         



