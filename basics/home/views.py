from django.shortcuts import render,redirect
from .models import Members
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def index(request):
    m_list = Members.objects.all().values()
    print(m_list)
    return render(request, "home/index.html", context={"m_list":m_list})

def add(request):
    return render(request, "home/add.html")

def addrecord(request):
    a = request.POST['first']
    b = request.POST['last']
    member = Members(firstname = a, lastname = b)
    member.save()
    return redirect("/")

def delete(request, id):
    member = Members.objects.get(id=id)
    member.delete()
    return redirect("/")

def update(request, id):
    member = Members.objects.get(id=id)
    return render(request, "home/update.html", context = {"member":member})

def updaterecord(request, id):
    a = request.POST['first']
    b = request.POST['last']
    member = Members.objects.get(id=id)
    member.firstname = a
    member.lastname = b
    member.save()
    return redirect("/")