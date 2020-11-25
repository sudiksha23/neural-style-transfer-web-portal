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
urls1=""
urls2=""

def delete(request, pk2):
    user=Content.objects.get(content=pk2)
    if request.method == 'POST':
        user.delete()
        return redirect('/')
    context = {'user': user}
    return render(request, 'delete.html', context)

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

#<MultiValueDict: {'style': [<InMemoryUploadedFile: water_lilies_crop.jpg (image/jpeg)>]}>

from pathlib import Path
def contentdisplay(request, pk_test,count):
    print(pk_test)
    if(pk_test!='content/uploads/selfie.jpg'):
        user=Content.objects.get(content=pk_test)
        path=Path(__file__).parent / "../static/media/"
        img_path="../static/media/"+pk_test
        with open(str(path)+"/content-file.txt",'w') as f:
            print("file opened")
            f.write(img_path)
        return render(request, 'index.html', {'userprofile' : user})
    else:
        print("in captires")
        cam = cv2.VideoCapture(0)
        
        ret, img = cam.read()
        #path=Path(__file__).parent
        path=Path(__file__).parent / "../static/media/"
        selfiefile='C:/Users/SUDIKSHA AGRAWAL/NstWebPortal/static/media/content/uploads/selfie'+str(count)+'.jpg'
        img_path = "../static/media/content/uploads/selfie" + str(count)+".jpg"
        
    
        cv2.imwrite(selfiefile, img)
        with open(str(path)+"/content-file.txt",'w') as f:
            print("file opened")
            f.write(img_path)
        print(selfiefile)
        print(img_path)
        cam.release
        cv2.destroyAllWindows
        url1=selfiefile[52:80]
        print("URLs: "+url1)
        
        m = Content()        
        m.content = url1   
        m.save()

        user=Content.objects.filter(content= url1)
        #c=c+1
        return render(request, 'index.html',{'userprofile': user[0]})
    
        
    return render(request,'index.html')    
    

def styledisplay(request, pk_test):
    user=Style.objects.get(style=pk_test)
    path=Path(__file__).parent / "../static/media/"    
    with open(str(path)+"/style-file.txt",'w') as f:
        f.write("models/"+pk_test[14:-3]+"model")
    # url2=pk_test
    return render(request, 'index.html', {'userprofile' : user})

import os
def merge(request):
    print("Merging...")
    path=Path(__file__).parent / "generate.py"
    print(str(path).replace(" ","/ "))
    os.system("python \""+str(path)+"\"")
    return render(request,'index.html')

