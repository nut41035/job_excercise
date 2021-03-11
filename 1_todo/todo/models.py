from django.db import models
from django.forms import ModelForm

class items(models.Model):
    item = models.CharField(max_length=200)
    complete = models.CharField(default='todo',max_length=9)
    def __str__(self):
        return self.item
# Create your models here.
