from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def summary(self):
        return self.body[:100]
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y') # ? allows you to change the way time looks
    def __str__(self):
        return self.title # in the admin page it changes the name from blog objects to the actual titles 

    

