from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Events
from blog.models import Blog 
from academia.models import Classes
from django.utils import timezone
import datetime
from django.utils.timezone import get_current_timezone


# Create your views here.
class EventListView(ListView):
    model = Events
    template_name = 'events/event_list.html'
    context_object_name = 'events'
    ordering  = 'pub_date'
    paginate_by = 3


class EventDetailView(DetailView):
    model = Events
    template_name = 'events/event_detail.html'
    context_object_name = 'event'

    def get_context_data(self, **kwargs):
        context = super(EventDetailView, self).get_context_data(**kwargs)
        recent_blog = Blog.objects.all().order_by('pub_date')
        context['recent_blog'] = recent_blog[:3]
        context['upcoming_events'] = Events.objects.filter(event_day__gte=datetime.date.today())
        context['popular_classes'] = Classes.objects.all()[:10]
        print(context)
        return context
    