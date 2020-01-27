from django.urls import path
from .views import BlogGridView,BlogDetailView


urlpatterns = [
    path('bloggrid',BlogGridView.as_view(),name='blog_list'),
    path('<slug:slug>',BlogDetailView.as_view(),name='blog_detail'),
]