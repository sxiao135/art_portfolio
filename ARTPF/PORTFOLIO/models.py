from django.db import models

# Create your models here.
class Works(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=4000)
    img_path = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.title}: {self.img_path}"

