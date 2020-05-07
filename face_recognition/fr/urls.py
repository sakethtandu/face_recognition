from django.urls import path

from . import views

urlpatterns = [
  # /
  path('', views.home, name='home'),
  # TEMPORARY
  path('signin', views.home, name='signin'),
  path('register_face', views.register_face, name='register_face'),

]
