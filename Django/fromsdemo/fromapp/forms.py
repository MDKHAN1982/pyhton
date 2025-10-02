from django import forms

# Register your models here.
class employeeform(forms.Form):
    eno = forms.IntegerField()
    ename = forms.CharField(max_length=50)
    esal = forms.FloatField()
    eaddr = forms.CharField(max_length=100)
