from django.shortcuts import render
from django.views.generic import ListView
from .models import GeeksModel

class GeeksList(ListView):
    model = GeeksModel
    template_name = "geeks/geeksmodel_list.html"   # template path
    context_object_name = "object_list"            # list name in template
