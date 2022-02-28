from django.urls import path
from . import views # to import all the methods in views.py
# use . to access files in the same folder
# connect to the views.py

#urlpatterns = [
#    path('index/', views.index, name='index') #/my_apps -- > PROJECT urls.py
#]

urlpatterns = [
    path('', views.simple_view, name="simple_view"),
    path('index/', views.index, name="index"), #directory, call to view, name
    path('peking/', views.peking_duck, name="peking"),
    path('<topic>/', views.dynamic_view) ## dynamic view
]