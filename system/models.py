from django.db import models

# Create your models here.

class person(models.Model):
    sr_no=models.CharField(max_length=100,null="True")
    task = models.CharField(max_length=100,null="True")
    date = models.DateTimeField(null="True")
    task_type = models.CharField(max_length=100,null="True")



