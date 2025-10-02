from django.contrib import admin
from django.urls import path
from demoapp import views as home_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_views.home, name='home'),
    path('gmview/', home_views.gmview, name='gmview'),
]

