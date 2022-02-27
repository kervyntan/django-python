from django.http import HttpResponse

def home_view (request):
    return HttpResponse("home view from site folder")