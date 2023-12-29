from django.shortcuts import render
from django.http import HttpResponse
from .models import Works

# Create your views here.
def testing(request):
    return HttpResponse("Hello World!")

def homepage(request):
    objects_with_tag_fp = Works.objects.filter(tags=1) #only works with id numbers
    return render(request, "portfolio/hpart.html", { #renders the first page with the studies
        "works": objects_with_tag_fp #include sql/django table with the titles and img_paths
    })

def studies(request):
    objects_with_tag_study = Works.objects.filter(tags=2) #only works with id numbers
    return render(request, "portfolio/studies.html", { #renders the first page with the studies
        "studies": objects_with_tag_study #include sql/django table with the titles and img_paths
    })