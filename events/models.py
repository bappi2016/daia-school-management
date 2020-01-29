from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 
from django.urls import reverse
from django.db.models.signals import pre_save # right before we save  the model instance , we gonna  do something  

# Create your models here.

class EventManager(models.Manager):
    """ Return all the active blog that post in past """
    def active(self,*args,**kwargs):
        return super(EventManager,self).filter(draft=False).filter(published__lte=timezone.now)


class Events(models.Model):
    event_day = models.DateTimeField()
    event_title = models.TextField(blank=False)
    event_description = models.TextField(blank=True)
    draft = models.BooleanField(default=False)
    slug = models.SlugField(unique=True,null=True,blank=True)
    event_small_image = models.ImageField(blank=True, null=True,upload_to = 'blog_image/%Y/%m/%d/')
    event_large_image = models.ImageField(blank=True, null=True,upload_to = 'blog_image/%Y/%m/%d/')
    pub_date = models.DateTimeField(auto_now_add=True)
    published = models.DateField(auto_now=False,auto_now_add=False,default=timezone.now)
    event_manager = models.CharField(max_length=48,blank=True, null=True)
    event_managers_role = models.CharField(max_length=48,blank=True, null=True)
    event_organaization = models.CharField(max_length=48,blank=True, null=True)
    event_location = models.CharField(max_length=48,blank=True, null=True)
    event_time = models.CharField(max_length=48,blank=True, null=True)
    contact_num = models.CharField(max_length=48,blank=True, null=True)
    contact_email = models.EmailField(blank=True, null=True)
    web_address = models.URLField(blank=True, null=True)


    objects = EventManager()

    def __str__(self):
        return self.event_title

    def eventsday(self):
        return self.event_day.strftime("%d")

    def eventsmonth(self):
        return self.event_day.strftime("%B")
    
    def eventsyear(self):
        return self.event_day.strftime("%Y")
    

    def get_absolute_url(self):
        return reverse("event_detail", kwargs={"slug": self.slug})
    

from blog.utils import unique_slug_generator

def create_unique_slug_for_event(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(create_unique_slug_for_event,sender=Events) # by signal pre save will run the function every time a model is created
