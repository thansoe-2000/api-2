from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
     persons = Person.objects.all()
     context = {
          'persons':persons
     }
     return render(request, 'index.html', context)
