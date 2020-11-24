from django.shortcuts import render,HttpResponse, redirect
from NST.models import Content
from NST.models import Style
import numpy as np
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from NST.forms import ContentForm
from NST.forms import StyleForm
import cv2 
from django.core.files import File
from django.contrib.auth.forms import UserCreationForm                                                               
from django.core.files.images import ImageFile
urls1=0
urls2=0
def index(request):
    return render(request, 'index.html')
def changepath(request):
    return render(request, 'index.html')

def redirect_view(request):
    response = redirect('/redirect-success/')
    return response

def content(request):
   
    data=Content.objects.all()
    context = {'display':data}
    return render(request, 'content.html', context)
def style(request):
    data=Style.objects.all()
    context = {'display':data}
    return render(request, 'style.html', context)

def contentfunc(request):
    if request.method == 'POST' or request.FILES == 'file':
        form = ContentForm(request.POST, request.FILES) 
        
        if form.is_valid(): 
            form.save() 
            return redirect('/')
            
    else: 
        form = ContentForm() 
    return render(request, 'NST/index.html',{'form':form}) 

def stylefunc(request):
    if request.method == 'POST' or request.FILES == 'file':
        form = StyleForm(request.POST, request.FILES) 
        
        if form.is_valid(): 
            form.save() 
            return redirect('/')
            
    else: 
        form = StyleForm() 
    return render(request, 'NST/index.html',{'form':form}) 
#<MultiValueDict: {'style': [<InMemoryUploadedFile: water_lilies_crop.jpg (image/jpeg)>]}>
def contentdisplay(request, pk_test):
    if(pk_test!='content/uploads/selfie.jpg'):
        user=Content.objects.get(content=pk_test)
        url1=pk_test
        return render(request, 'index.html', {'userprofile' : user})
    else:
        cam = cv2.VideoCapture(0)
        count=0
        result=True
        while(result):
            ret, img = cam.read()
            selfiefile='C:/Users/SUDIKSHA AGRAWAL/my_projects/NstWebPortal/static/media/content/uploads/selfie'+str(count)+'.jpg'
            cv2.imwrite(selfiefile, img)
            print(selfiefile)
            count +=1
            result=False
        cam.release
        cv2.destroyAllWindows
        url1=selfiefile[64:91]
        print(url1)
        
        m = Content()                                                                
        m.content = url1   
        m.save()

        user=Content.objects.filter(content= url1)
        #c=c+1
        return render(request, 'index.html',{'userprofile': user[0]})
    return render(request,'index.html')    
    

def styledisplay(request, pk_test):
    user=Style.objects.get(style=pk_test)
    url2=pk_test
    print(url2)
    return render(request, 'index.html', {'userprofile' : user})

def capturefunc(request):
    cam = cv2.VideoCapture(0)
    count = 0
    result=True
    while(result):
        ret, img = cam.read()
        selfiefile='C:/Users/SUDIKSHA AGRAWAL/my_projects/NstWebPortal/static/media/content/uploads/selfie.jpg'
        cv2.imwrite(selfiefile, img)
        print(selfiefile)
        count +=1
        result=False
        
    cam.release
    cv2.destroyAllWindows
    return render(request, 'index.html')

print(urls1)
print(urls2)
