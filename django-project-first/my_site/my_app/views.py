from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
# view 1
articles = {
    'sports' : 'Sports Page',
    'finance' : "Finance Page"
}

def index(request):
    return HttpResponse("HELLO THIS IS MY VIEW LOR")

def simple_view (request):
    return HttpResponse("This is my simple_view")

def peking_duck (request):
    return HttpResponse("I want a peking duck please pronto")

def dynamic_view (request, topic): ### dynamic view
    return HttpResponse(articles[topic])