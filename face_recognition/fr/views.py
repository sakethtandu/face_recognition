from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

def home(request):
  context = initialize_context(request)

  return render(request, 'fr/home.html', context)

def initialize_context(request):
  context = {}

  # Check for any errors in the session
  error = request.session.pop('flash_error', None)

  if error != None:
    context['errors'] = []
    context['errors'].append(error)

  # Check for user in the session
  context['user'] = request.session.get('user', {'is_authenticated': False})
  return context

def sign_in(request):

  return render('fr/sign_in.html')


def register_face(request):


#Please place the face_recognition code here



  return render(request, 'fr/register_face.html')
