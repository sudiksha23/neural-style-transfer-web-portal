from django.db import models
class Content(models.Model):
    content = models.ImageField(upload_to='content/uploads',verbose_name="", default='img1.jpg')
    
class Style(models.Model):
    style = models.ImageField(upload_to='style/uploads',verbose_name="", default='img2.jpg')
    

    

    