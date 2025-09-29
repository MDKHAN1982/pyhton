from django.shortcuts import render
from django.http import HttpResponse
def insurance(request):
    message = "<h1>Welcome to the Insurance Page!</h1>"
    return HttpResponse(message)

# Create your views here.
# http://127.0.0.1:8000/insurance/