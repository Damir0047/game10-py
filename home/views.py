from django.shortcuts import render
from .models import Mahsulot 

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
class Listview(ListView):
    model = Mahsulot
    Context_object_name = 'datas'
    template_name = 'index.html'

class  Detailview(DetailView):
    model = Mahsulot
    context_object_name = 'datas'
    template_name = 'single.html'
