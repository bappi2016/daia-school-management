from django.shortcuts import render,redirect,get_object_or_404,reverse

from django.views.generic import ListView,DetailView
from .models import Blog,BlogTag


# Create your views here.
class BlogGridView(ListView):
    model = Blog
    template_name = 'blog/blog_grid.html'
    context_object_name = 'blogs'
    ordering  = 'pub_date'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        recent_blog = Blog.objects.all().order_by('pub_date')
        context = super().get_context_data(**kwargs)
        context['recent_blog'] = recent_blog[:3]
        return context
    




class BlogDetailView(DetailView): 
    model = Blog
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blog'

    
    

    def get_context_data(self,*args,**kwargs):
        context = super(BlogDetailView,self).get_context_data(*args,**kwargs)# First get the existing context from our superclass ClassDetailView
        self.blog_name = get_object_or_404(Blog,slug=self.kwargs['slug'])

        current_blog = self.blog_name

        slug = self.kwargs['slug']
        recent_blog = Blog.objects.order_by('pub_date').exclude(slug=slug)
        all_tag_list = BlogTag.objects.all()
        tag_list = current_blog.tags.all()
        context['three_tag_list'] = tag_list[:3]
        context['all_tag_list'] = all_tag_list
        context['recent_blog'] = recent_blog[:3]
        print(recent_blog)
        return context
    


    





    