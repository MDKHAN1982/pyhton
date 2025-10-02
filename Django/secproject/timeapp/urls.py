from django.contrib import admin
from django.urls import path
from timeapp import views as time_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('current_datetime/', time_views.current_datetime, name='current_datetime'),
]
