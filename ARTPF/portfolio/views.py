from django.shortcuts import render
# from django.http import HttpResponse
from .models import Works, Tag

# Create your views here.
# def testing(request):
#     return HttpResponse("Hello World!")

def about(request):
    return render(request, "portfolio/about.html")

def error(request):
    return render(request, "portfolio/error.html")

# def portfolio_page(request, tag):
#     tag_mapping = {
#         'fp': 1,
#         'study': 2,
#         'digital': 6,
#     }
#     print(tag)

#     tag_id = tag_mapping.get(tag, None)
#     tag_id = int(tag_id)
#     if tag_id is None:
#         # Handle invalid tag, you can raise a 404 or redirect to a default page
#         return render(request, "portfolio/error.html")
    
#     # print(tag_id)
#     objects_with_tag = Works.objects.filter(tags=tag_id) #.prefetch_related_related(Tag)
#     # print(f"Tag ID: {tag_id}, Works count: {objects_with_tag.count()}")
    
#     template_name = f"portfolio/{tag}.html"

#     context = {
#         "works": objects_with_tag
#     }

#     return render(request, template_name, context)

# def image_detail(request, image_id):
#     image = Works.objects.get(id=image_id)
#     return render(request, 'portfolio/image_detail.html', {'image':image})
#
#####OLD FUNCTIONS
def index(request):
    objects_with_tag_fp = Works.objects.filter(tags=1) #only works with id numbers
    return render(request, "portfolio/index.html", { #renders the first page with the studies
        "works": objects_with_tag_fp #include sql/django table with the titles and img_paths
    })

def studies(request):
    objects_with_tag_study = Works.objects.filter(tags=3) #only works with id numbers
    return render(request, "portfolio/study.html", { #renders the first page with the studies
        "works": objects_with_tag_study #include sql/django table with the titles and img_paths
    })

def digital(request):
    objects_with_tag_digital = Works.objects.filter(tags=4) #only works with id numbers
    return render(request, "portfolio/digital.html", { #renders the first page with the studies
        "works": objects_with_tag_digital #include sql/django table with the titles and img_paths
    })
