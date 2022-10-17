
from django.urls import path
from . import views


urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('dogs/', views.dogs_index, name = 'dogs_index'),  
  path('dogs/<int:dog_id>/', views.dogs_detail, name='dogs_detail'),
  path('dogs/create', views.DogsCreate.as_view(), name='dogs_create'),
  path('dogs/<int:pk>/update/', views.DogsUpdate.as_view(), name ='dogs_update'),
  path('dogs/<int:pk>/delete/', views.DogsDelete.as_view(), name ='dogs_delete'),
  path('dogs/<int:dog_id>/add_feeding/', views.add_feeding, name ='add_feeding'),
  path('toy/create/', views.ToysCreate.as_view(), name='toys_create'),
  path('toys/', views.ToysIndex.as_view(), name='toys_index'),
  path('toys/<int:pk>/', views.ToysDetail.as_view(), name='toys_detail'),
  path('toys/<int:pk>/update/', views.ToysUpdate.as_view(), name='toys_update'),
  path('toys/<int:pk>/delete/', views.ToysDelete.as_view(), name='toys_delete'),
  path('dogs/<int:dog_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
  path('accounts/signup/', views.signup, name= 'signup'),
]

