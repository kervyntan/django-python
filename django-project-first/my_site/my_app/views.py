from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.urls import reverse

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
    try: #exception catching for error 404 pages
        result = articles[topic]
        return HttpResponse(articles[topic])
    except:
        result = 'No Page for the topic la dei'
        raise Http404("404 GENERIC ERROR") #404.html

        # return HttpResponseNotFound(result)

def add_view (request, num1, num2):
    #domain.com/my_app/num1/num2
    result = num1 + num2
    return HttpResponse(str(result))



#Redirects
#domain.com/my_app/0 -- > redirect to -- > domain.com/my_app/sports
# convert each key-value pair in the dictionary to a key-list pair (where each value is a list)\

def num_page_view (request, num_page):
    topics_list =  list(articles.keys()) # ['sports', 'finance']
    topic = topics_list[num_page] # for eg. topics_list[0] = 'sports'

    webpage = reverse('dynamic_view', args[topic])
    return HttpResponseRedirect(topic)

def html_view(request):
    return render(request, 'templates/my_app/example.html')