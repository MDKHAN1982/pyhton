from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
    date = datetime.now()
    hour = int(date.strftime('%H'))
    if hour < 12:
        message = 'GOOD Morning'
    else:
        message = 'GOOD EVENING' 
    date_dict = {'current_date': date,'greeting': message }
    return render(request, 'temp_demo/index.html', date_dict)