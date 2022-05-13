from django.db import models
from django.utils.text import slugify
from django_mysql.models import ListCharField

# Create your models here.

class Stories(models.Model):
    story_id = models.IntegerField("Story ID", null=True)
    title = models.TextField("Title", null=True)
    story_type = models.CharField("Type of item", max_length=15, null=True)
    synced = models.DateTimeField(auto_now_add=True)
    author = models.CharField("Author", max_length=50, null=True)
    kids= ListCharField(base_field=models.IntegerField(),max_length=(30*40),null=True)
    slug = models.SlugField(max_length=2000, null=True)
    time = models.CharField("Date created", max_length=1000, null=True)
    text = models.TextField("The comment, story or poll text.", null=True)
    dead = models.BooleanField(default=False)
    url = models.URLField("URL", max_length=1000, null=True, default="" ) 
    score = models.IntegerField("Score", null=True)
    descendants = models.IntegerField("Descendants",blank=True, null=True)




    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Stories, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title
class Comment(models.Model):
    title = models.TextField("Title", null=True)
    comment_id = models.IntegerField("Story ID", null=True, unique=True)
    story = models.ForeignKey(Stories, on_delete=models.CASCADE, related_name="comments", null=True)
    author = models.CharField("Author", max_length=50, null=True)
    time = models.CharField("Date created",max_length=1000,  null=True)
    text = models.TextField("Text", null=True)
    dead = models.BooleanField(default=False)
    comment_url = models.URLField("URL", max_length=1000, null=True)
    score = models.IntegerField("Score", null=True)
    

    def __str__(self):
        return self.title