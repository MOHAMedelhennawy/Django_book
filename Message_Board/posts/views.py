from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

class PostPageView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_posts_list'

# def PostPageView(request):
#     return render(request, 'home.html', {'all_posts_list': Post.objects.all()})