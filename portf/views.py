from django.shortcuts import render,get_object_or_404, redirect
from .models import portfolio
from django.views.generic import ListView, CreateView 
from django.urls import reverse_lazy
from .form import PostForm

class CreatePostView(CreateView): # new
    model = portfolio
    form_class = PostForm
    template_name = 'writeimage.html'
    success_url = reverse_lazy('pf')
# Create your views here.

def pf(request):
    portfolios = portfolio.objects
    return render(request, 'portf/pf.html', {'portfolios':portfolios})


def writeimage(request):
    return render(request, 'writeimage.html')

