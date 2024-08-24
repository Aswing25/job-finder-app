from django.db import models

# Create your models here.
class jobdb(models.Model):
    jobname = models.CharField(max_length=100,null=True,blank=True)
    jobplace = models.CharField(max_length=100,null=True,blank=True)
    description = models.CharField(max_length=100,null=True,blank=True)
    salary = models.IntegerField(null=True,blank=True)
    jobimage = models.ImageField(upload_to="jobs",null=True,blank=True)