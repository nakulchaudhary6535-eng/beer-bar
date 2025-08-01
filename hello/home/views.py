from django.shortcuts import render,HttpResponse
from datetime import date
from home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    context= {"variable":"Nakul is great but they do all the task very very late"}
    return render(request, 'index.html' ,context)

    #return HttpResponse("this is a homepage")

def about(request):
    return render (request,'about.html')

def service(request):
   return render(request,'service.html')


def contact(request):
   if request.method =="POST":
       name= request.POST.get('name')
       email= request.POST.get('email')
       mobile=request.POST.get('mobile')
       desc=request.POST.get('desc')
       print("Name",name)
       print("Email",email)
       print("Mobile",mobile)
       print("Desc",desc)
       contact = Contact(name=name, email=email, mobile=mobile,desc=desc,date=date.today())
       contact.save()
       messages.success(request, "Your message has been sent!")
   return render(request,'contact.html')
