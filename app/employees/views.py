from django.http import HttpResponse


# from django.shortcuts import render


# Create your views here.
def index(request):
    """Employees index homepage method"""
    return HttpResponse("test")
