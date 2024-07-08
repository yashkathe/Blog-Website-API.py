from django.db import models

from django.utils import timezone
from django.utils.text import slugify

class Blog(models.Model):
    title = models.CharField(max_length=30, null=False)
    description = models.TextField(max_length=150, null=False)
    tags = models.CharField(max_length=30, null=False) # this is an array stored in string format
    content=models.TextField(null=True)
    date=models.DateField(default=timezone.now)

     # changing the display name on admin site
    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs" 

    # how the data is displayed
    def __str__(self):
        return f"title:{self.title}"
