from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def rohit(request):
    return render(request,'rohit.html')
def boomra(request):
    return HttpResponse('<h1> boom boom kaboom</h1>')
