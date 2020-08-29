
from django.db import models


class TutorialDemoModelPersonalDetails(models.Model):
    Name = models.CharField(max_length=20,blank=False,default='')
    Address = models.CharField(max_length=200,blank=False,default='')
    Age = models.IntegerField(blank=False,default='')

class Tutorial(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200,blank=False, default='')
    published = models.BooleanField(default=False)

