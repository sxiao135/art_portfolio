from django.db import models

# Create your models here.

#creating a tag
class Tag(models.Model):
    name = models.CharField(max_length=50)
    #proj, fp, study

    def __str__(self):
        return self.name

#table with pieces
class Works(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=4000)
    img_path = models.CharField(max_length=1000)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.title}: {self.img_path}"

