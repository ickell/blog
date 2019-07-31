from django.db import models

# Create your models here.

class portfolio(models.Model):
    title = models.CharField(max_length = 200)
    image = models.ImageField(upload_to ='images/')
    description = models.TextField(max_length = 500)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
        
