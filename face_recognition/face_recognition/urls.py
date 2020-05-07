from django.contrib import admin
from django.urls import path, include
from fr import views

urlpatterns = [
    path('', include('fr.urls')),
    path('admin/', admin.site.urls),
]