from django.shortcuts import render
from . import forms

# Create your views here.
def empview(request):
    form = forms.employeeform()
    empInfo = {'form': form}
    return render(request, 'fromapp/empform.html', context=empInfo)