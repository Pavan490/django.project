from django.shortcuts import render
from django.http import HttpResponse

def pavan(request):
    return HttpResponse("Django is very powerful framework in python")

def demo(request):
    return HttpResponse("learning in django")