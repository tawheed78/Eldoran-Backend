from django.db import models

# Create your models here.
class Blog(models.Model):
    blog_title = models.CharField(max_length=250)
    blog_image = models.ImageField(upload_to ='uploads/blog_images/',null=True, blank=True)
    blog_content = models.TextField(max_length=1000, blank=False)
    def __str__(self):
        return self.blog_title