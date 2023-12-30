from django.shortcuts import render
from django.http import HttpResponse

def index (request):
    return render(request,"index.html")

   
def about (request):
    return render(request,"about.html") 

def gifts (request):
    return render(request,"gifts.html") 

def shop (request):
    return render(request,"shop.html")

def contact (request):
    return render(request,"contact.html")  

