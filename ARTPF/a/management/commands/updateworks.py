#NOT WORKING

import pandas as pd
from django.core.management.base import BaseCommand

from django.db import models
from portfolio.models import Tag as Tg
from portfolio.models import Works


# obj = Works.objects.create(
#     title = "human tower", 
#     description = "watercolor painting.", 
#     img_path = "human_tower_s.jpg",
# )

# tag_fp, created = Tags.objects.get_or_create(name="fp")

# obj.tags.add(tag_fp)

#this function assumes all ttags are already created
class Command(BaseCommand):

    def handle(self, *args, **options):
        fn = "122923.csv" #changes depending on file

        df = pd.read_csv(fn)
        for TITLE,DESCR,IP,TAGS in zip(df.Title,df.Description,df.Img_path,df.Tags):
            # obj = Works.objects.create(title=TITLE, description=DESCR, img_path=IP, tags.set([]))
            obj = Works.objects.create(title=TITLE)
            obj.description = DESCR
            obj.img_path = IP
            #idk if this will work
            TAG_LIST = (TAGS.split(','))
            for TAG in TAG_LIST:
                print(TAG, "\n")
                T = Tg.objects.get(name=TAG)
                print(T,"\n")
                obj.tags.add(T)
            
            obj.save()

