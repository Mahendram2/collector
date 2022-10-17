from django.shortcuts import render, redirect
from .models import Dog, Toy
from .forms import FeedingForm
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Define the home view
def home(request):
  return render(request,'home.html')

def about(request):
  return render (request, 'about.html')

def dogs_index(request):
  dogs = Dog.objects.all()
  return render(request,'dogs/index.html', {'dogs': dogs})

def dogs_detail(request, dog_id):
  dog = Dog.objects.get(id=dog_id)
  feeding_form = FeedingForm()
  toys = Toy.objects.exclude(id__in=dog.toys.all().values_list('id'))
  return render(request, 'dogs/detail.html', {'dog':dog, 'feeding_form': feeding_form, 'toys': toys})

def add_feeding(request, dog_id):
  print(request.POST)
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.dog_id = dog_id
    new_feeding.save()
  else: 
    print(form.errors)
  return redirect('dogs_detail', dog_id=dog_id)

def assoc_toy(request, dog_id, toy_id):
    Dog.objects.get(id=dog_id).toys.add(toy_id)
    return redirect('dogs_detail', dog_id=dog_id)

def signup(request):
    error_message = None
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('cats_index')
        else:
            error_message = 'Signup input invalid - Please try again'
    form = UserCreationForm()
    context = { 'form': form, 'error': error_message }
    return render(request, 'registration/signup.html', context)

class DogsCreate(CreateView):
  model = Dog
  fields = ('name', 'breed', 'age', 'description' )

  def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class DogsUpdate(UpdateView):
    model = Dog
    fields = ('age', 'description')

class DogsDelete(DeleteView):
    model = Dog
    success_url = '/dogs/'

class ToysCreate(CreateView):
    model = Toy
    fields = ('name', 'color')

class ToysIndex(ListView):
    template_name = 'toys/index.html'
    model = Toy

class ToysDetail(DetailView):
    template_name = 'toys/detail.html'
    model = Toy

class ToysUpdate(UpdateView):
    model = Toy
    fields = ('name', 'color')

class ToysDelete(DeleteView):
    model = Toy
    success_url = '/toys/'