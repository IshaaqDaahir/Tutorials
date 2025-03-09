from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
)
from .models import Article
from .forms import ArticleModelForm
from django.urls import reverse

# Create your views here.

class ArticleCreateView(CreateView):
    template_name = 'blog/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()
    # success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
    # def get_success_url(self):
    #     return '/'

class ArticleListView(ListView):
    # template_name = 'blog/article_detail.html'
    queryset = Article.objects.all()

class ArticleDetailView(DetailView):
    template_name = 'blog/article_detail.html'
    # queryset = Article.objects.all()

    def get_object(self):
        id = self.kwargs.get('id')
        return get_object_or_404(Article, id=id)

class ArticleUpdateView(UpdateView):
    template_name = 'blog/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()

    def get_object(self):
        id = self.kwargs.get('id')
        return get_object_or_404(Article, id=id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
class ArticleDeleteView(DeleteView):
    template_name = 'blog/article_delete.html'

    def get_object(self):
        id = self.kwargs.get('id')
        return get_object_or_404(Article, id=id)
    
    def get_success_url(self):
        return reverse('blog:article-list')
    
    