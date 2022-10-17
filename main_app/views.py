from django.shortcuts import render
from .models import Dog


# Define the home view
def home(request):
  return render(request,'home.html')

def about(request):
  return render (request, 'about.html')

def dogs_index(request):
  dogs = Dog.objects.all()
  return render(request,'dogs/index.html', {'dogs': dogs})

def dogs_detail(request, dog_id):
  dog = Dog.objects.get(dog_id)
  return render(request, {'dog':dog})