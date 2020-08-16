from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView
from .models import Post
from .forms import PostForm
from django.http import Http404, HttpResponseNotFound
from django.shortcuts import redirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.db.models import Q


# def home(request):
#    return render(request, 'new_wiki/index.html', {})


class IndexView(ListView):
    model = Post
    template_name = 'new_wiki/index.html'


def detail(request, pk):
    try:
        p = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return render(request, 'new_wiki/404.html', status=404)
    return render(request, 'new_wiki/instance.html', {'post': p})


class InstanceView(DetailView):
    model = Post
    template_name = 'new_wiki/instance.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'new_wiki/create.html'
    # fields = ('title', 'content')


class EditPost(UpdateView):
    model = Post
    template_name = 'new_wiki/edit_post.html'
    form_class = PostForm
    # fields = ('title', 'content')


class SearchView(ListView):
    model = Post
    template_name = 'new_wiki/search_result.html'

    def get_queryset(self):  # new
        query = self.request.GET.get('q')
        list_objects = Post.objects.filter(
            Q(title__icontains=query)
        )
        return list_objects
