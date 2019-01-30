from django.shortcuts import render
from django.views import View
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator

from .models import Post

from .forms import PostComment

# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

class CreaCommento(CreateView):
    model = Post
    template_name = 'main/post_create.html'
    form_class = PostComment
    success_url = '/'
    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()
        return super().form_valid(form)
