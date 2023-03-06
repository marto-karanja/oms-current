from django.db import models

# Create your models here.
class Orders(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    email = models.CharField(max_length=70, blank=False, default='')
    paper_length = models.CharField(max_length=70, blank=False, default='')
    topic = models.CharField(max_length=70, blank=False, default='')
    audience = models.CharField(max_length=70, blank=False, default='')
    written_in = models.CharField(max_length=70, blank=False, default='')
    email = models.CharField(max_length=70, blank=False, default='')
    deadline = models.CharField(max_length=200,blank=False, default='')
    paid = models.BooleanField(default=False)


