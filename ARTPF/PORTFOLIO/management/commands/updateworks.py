from django.core.management.base import BaseCommand

from django.db import models
from portfolio.models import Tags
from portfolio.models import Works
import pandas as pd

# obj = Works.objects.create(
#     title = "human tower", 
#     description = "watercolor painting.", 
#     img_path = "human_tower_s.jpg",
# )

# tag_fp, created = Tags.objects.get_or_create(name="fp")

# obj.tags.add(tag_fp)

class addNewWorks(BaseCommand):
    