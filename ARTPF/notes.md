Models SQL

* open shell:
  * python manage.py shell
* open model:
  * from django.db import models
  * from [appname].models import [modelname]
* get all info from the return statement:
  * [modelname].objects.all()
* get item using id:
  * a = [modelname].obejcts.get(pk=2)