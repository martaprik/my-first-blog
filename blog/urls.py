# Import of Django function path and all our views from the "blog" app
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]
