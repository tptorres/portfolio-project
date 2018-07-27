from django.db import models

class Job(models.Model):
    image = models.ImageField(upload_to='images/')     # django model field; 
    summary = models.CharField(max_length=200)  # puts a cap on the amount of text below the image