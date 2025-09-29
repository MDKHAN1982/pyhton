from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    message = "<h1>Hello, welcome to the home page!</h1>"
    return HttpResponse(message)
def gmview(request):
    return HttpResponse("<H1 style='width:20px;height:20px;background-color:#ffcc00;'> WELCOME TO DEMO CABS </H1>")


# Create your views here.
