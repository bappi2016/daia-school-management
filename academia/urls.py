from django.urls import path
from .views import ClassListView,ClassDetailView,ClassGridView,ContactView



urlpatterns = [
    path('',ClassListView.as_view(),name='class_list'),
    path('classgrid',ClassGridView.as_view(),name='class_grid'),
    path('<int:pk>',ClassDetailView.as_view(),name='class_detail'),
    path('contact/',ContactView.as_view(),name='contact'),
]

