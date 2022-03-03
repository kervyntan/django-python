from django.urls import path
from . import views # to import all the methods in views.py
# use . to access files in the same folder
# connect to the views.py

#urlpatterns = [
#    path('index/', views.index, name='index') #/my_apps -- > PROJECT urls.py
#]

#urlpatterns = [
#    path('', views.simple_view, name="simple_view"),
 #   path('index/', views.index, name="index"), #directory, call to view, name
  #  path('peking/', views.peking_duck, name="peking"),
   # path('<int:num_page>/', views.num_page_view),
    #path('<str:topic>/', views.dynamic_view, name="dynamic_view")## dynamic view)## dynamic view, path converter 
#]

### Connecting view to a HTML template ###

urlpatterns = [
    path('', views.html_view) #domain.com/my_app/
]