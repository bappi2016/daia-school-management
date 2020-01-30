from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404
from blog.models import Blog
from photologue.models import Photo
from .models import Classes,Teacher
from events.models import Events
import datetime


# Create your views here.
class ClassListView(ListView):
    model = Classes
    template_name = 'home/index.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recent_blog"] = Blog.objects.order_by('pub_date')[:3]
        context['upcoming_events'] = Events.objects.filter(event_day__gte=datetime.date.today())[:6]
        context['photos'] = Photo.objects.all()[:6]
        print(context)
        return context
    


class ClassGridView(ListView):
    model = Classes
    template_name = 'class_grid.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recent_blog = Blog.objects.all().order_by('pub_date')
        context['recent_blog'] = recent_blog[:3]
        return context
    


class ClassDetailView(DetailView): ## this context will bring the Class corrospondint to that pk
    model = Classes
    template_name = 'home/class_detail.html'
    context_object_name = 'class'

    
    

    def get_context_data(self,*args,**kwargs):
        context = super(ClassDetailView,self).get_context_data(*args,**kwargs)# First get the existing context from our superclass ClassDetailView
        pk_url_kwarg = 'id'

        self.class_name = get_object_or_404(Classes,id=self.kwargs['pk']) #return the associate class name that belong to this pk

        self.class_teacher = get_object_or_404(Teacher,id=self.kwargs['pk']) #return class Teacher name which pk matches the urls pk, that is Albert Einstai = 4, 
        c = self.kwargs['pk'] # grab the current kwargs as pk that we passed in the urls
        current_class = self.class_name
        teachers = current_class.teacher
        e = Classes.objects.get(id=c) # return the current class object
        t = e.teacher # Returns the releted Teacher object,because of One-to-many relationship
        b = Teacher.objects.get(id=c) # return the teacher name of current class object
        bb = b.teachers.all() # will return a QuerySet of matches or related classes that belong to the current techer of this class object
        # Adding new context information
        context['current_class_name'] = current_class
        context['assosiate_teacher'] = e.teacher
        context['related_classes'] = b.teachers.all().exclude(id=c)
        context['popular_classes'] = Classes.objects.all()[:10]
        recent_blog = Blog.objects.all().order_by('pub_date')
        context['recent_blog'] = recent_blog[:3]
        # print(teachers,self.class_name,c,e,t,b,bb)
        return context # return new or updated context
        
        
class ContactView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super(ContactView,self).get_context_data(**kwargs)
        recent_blog = Blog.objects.all().order_by('pub_date')
        context['recent_blog'] = recent_blog[:3]
        return context
    
    


    

