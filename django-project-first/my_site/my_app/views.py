from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
# view 1
def index(request):
    return HttpResponse("HELLO THIS IS MY VIEW LOR")

def simple_view (request):
    return HttpResponse("This is my simple_view")