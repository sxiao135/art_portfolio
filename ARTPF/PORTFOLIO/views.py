from django.shortcuts import render
from django.http import HttpResponse
from .models import Works

# Create your views here.
def testing(request):
    return HttpResponse("Hello World!")

def homepage(request):
    return render(request, "portfolio/hpart.html", { #renders the first page with the studies
        "works": Works.objects.all() #include sql/django table with the titles and img_paths
    })