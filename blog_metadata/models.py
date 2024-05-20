from django.db import models

from django.utils import timezone
from django.utils.text import slugify

class BlogMetaData(models.Model):
    title = models.CharField(max_length=30, null=False)
    description = models.TextField(max_length=150, null=False)
    tags = models.CharField(max_length=30, null=False) # this is an array stored in string format
    route=models.SlugField(null=False) # only store the extended route (except basename)
    componentName= models.CharField(max_length=25, null=False)
    date=models.DateField(default=timezone.now)

     # changing the display name on admin site
    class Meta:
        verbose_name = "Blog Metadata"
        verbose_name_plural = "Blog Metadata Entries" 

    # modify default save method to slugify the title
    def save(self, *args, **kwargs):
        self.route = slugify(self.title)
        super().save(*args, **kwargs)

    # how the data is displayed
    def __str__(self):
        return f"title:{self.title}"
