from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import StudentRecord
from .models import User
# Create your views here.
# add new data and show information
def add_show(request):
    if request.method == 'POST':
        fm = StudentRecord(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg=User(name=nm, email=em, password=pw)

            fm.save()
            fm=StudentRecord()
    else:
        fm=StudentRecord( )
        stud = User.objects.all()    #show all data
    return render(request,'enroll/addandshow.html',{'form':fm, 'stu':stud})
def delete(request, id):
   if request.method == 'POST':
       pi = User.objects.get(pk=id)
       pi.delete()
       return HttpResponseRedirect('/')
def update(request,id):
    if request.method =='POST':
        pi = User.objects.get(pk=id)
        fm = StudentRecord(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()

    else:
        pi = User.objects.get(pk=id)
        fm = StudentRecord(instance=pi)
    return render(request,'enroll/update.html',{'form':fm})
