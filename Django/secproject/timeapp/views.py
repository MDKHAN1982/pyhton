from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, timedelta

def current_datetime(request):
    now = datetime.now()
    return HttpResponse(f"<h1>Current Date and Time: {now}</h1>")




# Create your views here.
