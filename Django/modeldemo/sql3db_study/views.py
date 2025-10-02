from django.shortcuts import render
from sql3db_study.models import employee

# Create your views here.
def index(request):
    fmodel_emp = employee.objects.all()
    emp_dict = {'emp_key': fmodel_emp}
    return render(request, 'modeldemo/index.html', emp_dict)
    # return render(request, 'modeldemo/index.html') 
