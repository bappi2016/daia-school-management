from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 
from django.urls import reverse
from django.db.models.signals import pre_save # right before we save  the model instance , we gonna  do something  

# Create your models here.

class BlogManager(models.Manager):
    """ Return all the active blog that post in past """
    def active(self,*args,**kwargs):
        return super(PostManager,self).filter(draft=False).filter(published__lte=timezone.now)



class BlogTagManager(models.Manager):
    def get_by_natural_key(self,slug):# the model manager's get_by_natural_key is used in deserialization and the natural_key is used in serialization.
        return self.get(slug=slug)


# tag -as a generalization of blog categories :one blog may have one or many tags, and one tag may contain one or more blog.

class BlogTag(models.Model):
    name = models.CharField(max_length=32)
    slug = models.SlugField(max_length=48)
    description = models.TextField(blank=True)
    active = models.BooleanField(default=True)

    objects = BlogTagManager()

    def __str__(self):
        return self.name

    def natural_key(self):
        return (self.slug)


class Blog(models.Model):
    blog_title = models.TextField(blank=False)
    tags = models.ManyToManyField(BlogTag,blank=True,related_name='tags')
    blog_description = models.TextField(blank=True)
    draft = models.BooleanField(default=False)
    slug = models.SlugField(unique=True,null=True,blank=True)
    image = models.ImageField(blank=True, null=True,upload_to = 'blog_image/%Y/%m/%d/')
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    published = models.DateField(auto_now=False,auto_now_add=False,default=timezone.now)

    objects =BlogManager()

    def __str__(self):
        return self.blog_title
    

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"slug": self.slug})
    

from .utils import unique_slug_generator

def create_unique_slug_for_blog(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(create_unique_slug_for_blog,sender=Blog) # by signal pre save will run the function every time a model is created