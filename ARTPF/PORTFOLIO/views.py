from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Works, Tag

# Create your views here.
def testing(request):
    return HttpResponse("Hello World!")

def about(request):
    return render(request, "portfolio/about.html")

def error(request):
    return render(request, "portfolio/error.html")

def portfolio_page(request, tag):
    tag_mapping = {
        'fp': 1,
        'study': 2,
        'digital': 6,
    }
    print(tag)

    tag_id = tag_mapping.get(tag, None)
    tag_id = int(tag_id)
    if tag_id is None:
        # Handle invalid tag, you can raise a 404 or redirect to a default page
        return render(request, "portfolio/error.html")
    
    # print(tag_id)
    objects_with_tag = Works.objects.filter(tags=tag_id) #.prefetch_related_related(Tag)
    # print(f"Tag ID: {tag_id}, Works count: {objects_with_tag.count()}")
    
    template_name = f"portfolio/{tag}.html"

    context = {
        "works": objects_with_tag
    }

    return render(request, template_name, context)

# def image_detail(request, image_id):
#     image = Works.objects.get(id=image_id)
#     return render(request, 'portfolio/image_detail.html', {'image':image})
