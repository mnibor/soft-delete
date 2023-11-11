from django.views.generic import ListView, DetailView
from .models import Post

class HomeView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        # Filtrar los posts que no están borrados y tienen autor y categoría
        return Post.objects.filter(deleted=False, author__isnull=False, category__isnull=False)

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
